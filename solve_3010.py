import socket
import select
import re
import sys
import time

HOST = "chals.uscc-cyberbowl-2025.ctf.institute"
PORT = 3010

NUM_WORDS = {
    "ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5,
    "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10,
    "ELEVEN": 11, "TWELVE": 12, "THIRTEEN": 13, "FOURTEEN": 14,
    "FIFTEEN": 15, "SIXTEEN": 16, "SEVENTEEN": 17, "EIGHTEEN": 18,
    "NINETEEN": 19, "TWENTY": 20, "THIRTY": 30, "FORTY": 40,
    "FIFTY": 50, "SIXTY": 60, "SEVENTY": 70, "EIGHTY": 80, "NINETY": 90,
}

SCALE_WORDS = {
    "HUNDRED": 100,
}

def parse_number(text: str) -> int:
    t = text.strip().upper()
    # Allow digits directly
    if re.fullmatch(r"-?\d+", t):
        return int(t)
    # Remove punctuation except dash and space
    t = re.sub(r"[^A-Z0-9\- ]", "", t)
    # Handle hyphenated or spaced words including simple scales ("one hundred")
    parts = re.split(r"[\- ]+", t)
    total = 0
    current = 0
    for p in parts:
        if not p:
            continue
        if re.fullmatch(r"\d+", p):
            current += int(p)
            continue
        if p in NUM_WORDS:
            current += NUM_WORDS[p]
            continue
        if p in SCALE_WORDS:
            if current == 0:
                current = 1
            current *= SCALE_WORDS[p]
            continue
        # Unknown token; raise so caller can debug
        raise ValueError(f"Unknown number token: {p!r} from {text!r}")
    total += current
    return total


def compute(expr: str):
    m = re.search(r"([A-Za-z0-9 \-]+)\s+(plus|minus|times)\s+([A-Za-z0-9 \-]+)\?", expr, re.I)
    if not m:
        return None
    a, op, b = m.group(1), m.group(2).lower(), m.group(3)
    A = parse_number(a)
    B = parse_number(b)
    if op == "plus":
        return A + B
    if op == "minus":
        return A - B
    if op == "times":
        return A * B
    return None


def main():
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect((HOST, PORT))
    except BlockingIOError:
        pass  # expected for nonblocking connect

    buf = ""
    answered = set()
    start = time.time()
    # Run up to 60 seconds or until we see a flag
    while time.time() - start < 60:
        # Wait a short time for readability
        rlist, _, _ = select.select([s], [], [], 0.2)
        if rlist:
            try:
                data = s.recv(8192)
                if not data:
                    break
                buf += data.decode(errors="ignore")
            except BlockingIOError:
                pass

        # Find all math questions prefixed by the prompt marker
        for m in re.finditer(r"\u2753\s*([A-Za-z0-9\- ]+\?)", buf):  # '❓'
            q = m.group(1)
            if q in answered:
                continue
            ans = compute(q)
            if ans is None:
                continue
            try:
                s.sendall((str(ans) + "\n").encode())
                answered.add(q)
            except (BrokenPipeError, OSError):
                break

        # Also handle questions that may not include the symbol
        for m in re.finditer(r"([A-Za-z0-9 \-]+\?)\s*\nYour answer", buf, re.I):
            q = m.group(1)
            if q in answered:
                continue
            ans = compute(q)
            if ans is None:
                continue
            try:
                s.sendall((str(ans) + "\n").encode())
                answered.add(q)
            except (BrokenPipeError, OSError):
                break

        # Trim buffer
        if len(buf) > 6000:
            buf = buf[-3000:]
        if re.search(r"(USCC\{|CTF\{|FLAG\{)", buf, re.I):
            print(buf)
            break

    s.close()


if __name__ == "__main__":
    main()
