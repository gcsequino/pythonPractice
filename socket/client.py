# This program can be found at https://www.geeksforgeeks.org/socket-programming-python/

# Import socket module
import socket

# Create socket object
s = socket.socket()

# Define port you want to connect to
port = 12345

# Connect to server on local computer
s.connect(('127.0.0.1', port))

# Recieve data from the server
byt = s.recv(4096)
msg = byt.decode()
print(msg)

# Close the connection
s.close()
