import socket

#The IP of this machine
SERVER = "127.0.0.1"
PORT = 8080

#Making a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to