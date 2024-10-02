import socket

#The IP of this machine
SERVER = "127.0.0.1"
PORT = 8080

#Making a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server
client.connect((SERVER,PORT))

#infintie loop
while True:
    print("Example: 4 + 5")
    #Getting user input
    UserInput = input("Enter the operation in \
the form opreand operator oprenad: ")
    #User uses "Over" to terminate
    if UserInput == "Over":
        break

    #Send the user input to the server socket
    client.send(UserInput.encode())

    #Receives output from the server socket
    answer = client.recv(1024)
    print("Answer is "+ answer.decode())
    print("Type 'Over' to termainate")

client.close()
