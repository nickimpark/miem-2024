import socket
from threading import Thread

mySocket = socket.socket()
mySocket.connect("127.0.0.1", 8000)

def send_func():
    while True:
        number = input("Число для отправки: ")
        mySocket.send(number.encode("utf-8"))
        
def ans_func():
    while True:
        ans = mySocket.recv(1024)
        print(ans.decode("utf-8"))

thread1 = Thread(target=send_func)
thread2 = Thread(target=ans_func)
thread1.start()
thread2.start()
