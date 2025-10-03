import socket
import sys
import time
import select


def recv_all(host: str, port: int, overall_timeout: float = 5.0, idle_timeout: float = 1.5) -> bytes:
	start_time = time.time()
	data_chunks: list[bytes] = []
	with socket.create_connection((host, port), timeout=3.0) as sock:
		sock.setblocking(False)
		last_data_time = time.time()
		while True:
			# Stop if overall time exceeded
			if time.time() - start_time > overall_timeout:
				break
			# Use select to wait for readability with a short timeout
			readable, _, _ = select.select([sock], [], [], 0.2)
			if readable:
				try:
					chunk = sock.recv(4096)
					if not chunk:
						break
					data_chunks.append(chunk)
					last_data_time = time.time()
				except (BlockingIOError, InterruptedError):
					pass
			else:
				# If idle for too long, stop
				if time.time() - last_data_time > idle_timeout:
					break
	return b"".join(data_chunks)


def main() -> int:
	if len(sys.argv) != 3:
		print("Usage: probe.py <host> <port>", file=sys.stderr)
		return 2
	host = sys.argv[1]
	try:
		port = int(sys.argv[2])
	except ValueError:
		print("Port must be an integer", file=sys.stderr)
		return 2

	try:
		data = recv_all(host, port)
		# Print raw output
		try:
			text = data.decode("utf-8", errors="replace")
		except Exception:
			text = repr(data)
		print(text)
		return 0
	except Exception as exc:
		print(f"Error: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	sys.exit(main())

