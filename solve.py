import re
import socket
import sys
import time
import select
import ast
import operator
from typing import Optional


class SafeEvaluator(ast.NodeVisitor):
	ALLOWED_BINOPS = {
		ast.Add: operator.add,
		ast.Sub: operator.sub,
		ast.Mult: operator.mul,
		ast.Div: operator.truediv,
		ast.FloorDiv: operator.floordiv,
		ast.Mod: operator.mod,
		ast.Pow: operator.pow,
	}

	def visit(self, node):  # type: ignore[override]
		if isinstance(node, ast.Expression):
			return self.visit(node.body)
		if isinstance(node, ast.BinOp):
			left = self.visit(node.left)
			right = self.visit(node.right)
			op_type = type(node.op)
			if op_type not in self.ALLOWED_BINOPS:
				raise ValueError("Unsupported operator")
			return self.ALLOWED_BINOPS[op_type](left, right)
		if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
			operand = self.visit(node.operand)
			return +operand if isinstance(node.op, ast.UAdd) else -operand
		if isinstance(node, ast.Num):  # py<3.8
			return node.n  # type: ignore[attr-defined]
		if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
			return node.value
		if isinstance(node, ast.Paren) or isinstance(node, ast.Tuple):
			raise ValueError("Parentheses/Tuple nodes not expected explicitly")
		raise ValueError("Unsupported expression")


NUMBER_WORDS_UNITS = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	"ten": 10,
	"eleven": 11,
	"twelve": 12,
	"thirteen": 13,
	"fourteen": 14,
	"fifteen": 15,
	"sixteen": 16,
	"seventeen": 17,
	"eighteen": 18,
	"nineteen": 19,
}


NUMBER_WORDS_TENS = {
	"twenty": 20,
	"thirty": 30,
	"forty": 40,
	"fifty": 50,
	"sixty": 60,
	"seventy": 70,
	"eighty": 80,
	"ninety": 90,
}


NUMBER_WORDS_MAGNITUDES = {
	"hundred": 100,
	"thousand": 1000,
	"million": 1_000_000,
}


OPERATOR_WORDS = {
	"plus": "+",
	"add": "+",
	"added": "+",
	"sum": "+",
	"and": "+",  # sometimes used like "sum of two and three"
	"minus": "-",
	"subtract": "-",
	"subtracted": "-",
	"difference": "-",
	"times": "*",
	"multiplied": "*",
	"multiply": "*",
	"product": "*",
	"x": "*",
	"×": "*",
	"*": "*",
	"divided": "/",
	"divide": "/",
	"over": "/",
	"÷": "/",
	"/": "/",
	"mod": "%",
	"modulo": "%",
	"power": "**",
	"pow": "**",
	"^": "**",
}


def normalize_text(input_text: str) -> str:
	t = input_text.strip()
	t = t.replace("\u00d7", "×").replace("\u00f7", "÷")
	t = t.replace("–", "-").replace("—", "-")
	return t


def is_number_word(token: str) -> bool:
	t = token.lower()
	return (
		t in NUMBER_WORDS_UNITS
		or t in NUMBER_WORDS_TENS
		or t in NUMBER_WORDS_MAGNITUDES
		or t == "and"
	)


def parse_number_words(tokens: list[str], start_index: int) -> tuple[Optional[int], int]:
	total_value = 0
	current_group_value = 0
	index = start_index
	consumed_any = False
	while index < len(tokens):
		token = tokens[index].lower()
		if token == "and":
			index += 1
			continue
		if token in NUMBER_WORDS_UNITS:
			current_group_value += NUMBER_WORDS_UNITS[token]
			consumed_any = True
			index += 1
			continue
		if token in NUMBER_WORDS_TENS:
			current_group_value += NUMBER_WORDS_TENS[token]
			consumed_any = True
			index += 1
			continue
		if token in NUMBER_WORDS_MAGNITUDES:
			magnitude = NUMBER_WORDS_MAGNITUDES[token]
			if current_group_value == 0:
				current_group_value = 1
			total_value += current_group_value * magnitude
			current_group_value = 0
			consumed_any = True
			index += 1
			continue
		break
	if not consumed_any:
		return None, start_index
	return total_value + current_group_value, index


TOKEN_RE = re.compile(r"[A-Za-z]+|\d+|[()+\-*/^×÷]")


def words_to_expression(question_text: str) -> Optional[str]:
	text = normalize_text(question_text)
	text = text.replace("-", " ")
	tokens = TOKEN_RE.findall(text)
	output_tokens: list[str] = []
	index = 0
	while index < len(tokens):
		token = tokens[index]
		lower_token = token.lower()
		if lower_token in OPERATOR_WORDS:
			output_tokens.append(OPERATOR_WORDS[lower_token])
			index += 1
			continue
		if token.isdigit():
			output_tokens.append(token)
			index += 1
			continue
		if is_number_word(lower_token):
			num_value, next_index = parse_number_words(tokens, index)
			if num_value is None:
				index += 1
				continue
			output_tokens.append(str(num_value))
			index = next_index
			continue
		if token in {"(", ")"}:
			output_tokens.append(token)
			index += 1
			continue
		# Skip unrelated words
		index += 1
	if not output_tokens:
		return None
	# Remove trailing operators if any
	while output_tokens and output_tokens[-1] in {"+", "-", "*", "/", "%", "**"}:
		output_tokens.pop()
	if not output_tokens:
		return None
	return " ".join(output_tokens)


def safe_eval_expression(expr: str) -> float:
	node = ast.parse(expr, mode="eval")
	return SafeEvaluator().visit(node)


def compute_answer_for_question(question_text: str) -> str:
	q = question_text.strip()
	if q.startswith("❓"):
		q = q.split("❓", 1)[1].strip()
	# Try arithmetic expression using words/digits
	expr = words_to_expression(q)
	if expr:
		try:
			result = safe_eval_expression(expr)
			if abs(result - int(result)) < 1e-9:
				return str(int(result))
			return str(result)
		except Exception:
			pass
	# Try direct digits arithmetic extraction
	try:
		digits_expr = re.sub(r"[^0-9+\-*/()%]", " ", q)
		digits_expr = re.sub(r"\s+", " ", digits_expr).strip()
		if digits_expr:
			result = safe_eval_expression(digits_expr)
			if abs(result - int(result)) < 1e-9:
				return str(int(result))
			return str(result)
	except Exception:
		pass
	# Heuristic: if contains the word minus/plus etc but failed, try simple two-operand pattern
	two_op = re.search(
		r"([A-Za-z0-9 -]+)\s+(plus|minus|times|multiplied by|divided by|over)\s+([A-Za-z0-9 -]+)",
		q,
		re.IGNORECASE,
	)
	if two_op:
		left_text, op_word, right_text = two_op.groups()
		left_expr = words_to_expression(left_text) or left_text
		right_expr = words_to_expression(right_text) or right_text
		op_symbol = OPERATOR_WORDS.get(op_word.lower(), "+")
		try:
			result = safe_eval_expression(f"{left_expr} {op_symbol} {right_expr}")
			if abs(result - int(result)) < 1e-9:
				return str(int(result))
			return str(result)
		except Exception:
			pass
	# As a last resort, return an empty string
	return ""


def run_solver(host: str, port: int) -> None:
	with socket.create_connection((host, port), timeout=5.0) as sock:
		sock.setblocking(False)
		buffer = ""
		last_print_pos = 0
		question_count = 0
		last_question_sent: Optional[str] = None
		while True:
			readable, _, _ = select.select([sock], [], [], 0.2)
			if readable:
				chunk = sock.recv(4096)
				if not chunk:
					break
				buffer += chunk.decode("utf-8", errors="replace")
				# Print any new data
				if last_print_pos < len(buffer):
					print(buffer[last_print_pos:], end="", flush=True)
					last_print_pos = len(buffer)
			# Detect question and prompt for answer (send once per unique question)
			if "Your answer" in buffer:
				# Extract the last question line prefixed by the emoji or a question mark line
				question_line = None
				lines = buffer.splitlines()
				for i in range(len(lines) - 1, -1, -1):
					line = lines[i]
					if line.strip().startswith("❓") or line.strip().endswith("?"):
						question_line = line.strip()
						break
				if question_line is None and lines:
					question_line = lines[-1].strip()
				# Only send if this is a new question we haven't answered
				if question_line and question_line != last_question_sent:
					answer = compute_answer_for_question(question_line)
					if not answer:
						answer = "0"
					sock.sendall((answer + "\n").encode())
					last_question_sent = question_line
					question_count += 1
					print(f"[sent answer: {answer}]\n", end="", flush=True)
			# Stop if a flag-like token appears
			if re.search(r"(?i)uscc\{|flag\{", buffer):
				break


def main() -> int:
	if len(sys.argv) != 3:
		print("Usage: solve.py <host> <port>", file=sys.stderr)
		return 2
	host = sys.argv[1]
	try:
		port = int(sys.argv[2])
	except ValueError:
		print("Port must be an integer", file=sys.stderr)
		return 2
	try:
		run_solver(host, port)
		return 0
	except Exception as exc:
		print(f"Error: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	sys.exit(main())

