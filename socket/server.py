# This program can be found at https://www.geeksforgeeks.org/socket-programming-python/

# First of all import the socket library
import socket

# Next create a socket object
s = socket.socket()
print("Socket successfully created")

# Reserve a port on your computer in our
# case it is 12345
port = 12345

# Next bind the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("Socket binded to %s" %(port))

# Put the socket into listening mode
s.listen(5)
print("Socket is listening")

# An infinite loop intil we interupt it or
# an error occurs
while True:
    
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client
    msg = 'Hello client! Thank you for connecting.\n'
    byt = msg.encode()
    c.send(byt)

    # Close the connection with the client
    c.close()
