import socket

#localhost ip
LOCALHOST = "127.0.0.1"
PORT = 8080

#creating a server socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((LOCALHOST, PORT))

server.listen(1)
print("Server started")
print("Waiting for client request.. ")

#Server socket is ready of input from user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''

while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'Over':   
        print("Connection is Over")
        break

    print("Equation is received")
    result = 0
    operation_list = msg.split()
    oprend1 = operation_list[0]
    operation = operation_list[1]
    oprend2 = operation_list[2]

    #convert oprend 1 & 2 to int
    num1 = int(oprend1)
    num2 = int(oprend2)

    #Match operation to a result
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '/':
            result = num1 / num2
        case '*':
            result = num1 * num2

    print("Sent result to client")

    #Convert result from a int to a string
    output = str(result)
    clientConnection.send(output.encode())

clientConnection.close()

