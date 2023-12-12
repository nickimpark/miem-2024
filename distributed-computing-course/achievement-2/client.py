import socket

s = socket.socket()
host = socket.gethostname()
port=9600
s.connect((host, port))
number = input("Input your number: ")
s.send(number.encode("utf-8"))
number = s.recv(1024).decode("utf-8")
print(number)

s.close()
