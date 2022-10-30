# 361-Microservice

Purpose: Generate a Random Number between 10 and 20, inclusively.

Summary: The client sends a request to the server. The server generates a random number and sends the data to the client.

Library Requirements: Import Random, Import Socket in Python

Files Included: There are two files: server_random.py and client_random.py. 

# server_random.py:
 -------First---------
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

First, The host could be a specific computers IP address, localhost, or the address provided by the sockets website, as listed above. The port can also be chosen to any port not in use. The port included was also provided by the sockets website. 

 -------Second--------
s = socket.socket()
s.bind((HOST, PORT))
s.listen()

Second, the server creates a socket. Once the socket is created, it binds a tuple of the host and port. Next, it waits and listens for the client to send a request to connect. 

 -------Third---------
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    data = bytes(str(random.randint(10, 20)), 'UTF-8')
    conn.send(data)
    conn.close()

Third, the server uses a while loop to connect with the client as many times as the client sends a request to connect. Once the connection is established by the address expected. It prints a statement, for example, "Connected by 127.0.0.1". The server sends the data as a byte type to the client. Once the client receives the data, the connection is closed. The server continues to wait for a new connection.

# client_random.py:

 -------First---------
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

First, like the server, the client established the Host and Port to be used. 

 -------Second--------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

Second, a socket is created on the client's side and a connection is established with the Host and Port. The client then receives the information sent from the server and stores it in the variable 'data'. The connection with the server is closed, until a connection is sent to the server again. 

 -------Third-------
print(int(data))

Third, the data variable contains the byte type of the random number and needs to be converted to an int type.

# How to Use:
Open both programs. Run server_random.py. Run client_random.py to receive random number. 

For more information on how it works: https://realpython.com/python-sockets/

 
