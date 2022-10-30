import random
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    data = bytes(str(random.randint(10, 20)), 'UTF-8')
    conn.send(data)
    conn.close()
