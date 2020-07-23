# An example script to connect to Google using socket
# programming in Python.
#
# This program can be found at https://www.geeksforgeeks.org/socket-programming-python/
import socket # for the socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

# Default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # This means the host could not be resolved
    print("There was an error resolving the host")
    sys.exit()

# Connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google \
on port == %s" %(host_ip))
