import socket
import psycopg2

conn = psycopg2.connect(
        host     = "localhost",
        database = "mydb",
        user     = "postgres",
        password = "password",
        port=5432
            )
conn.autocommit = True
        
cur = conn.cursor()
print("Connected to PostgreSQL")

def process_request(number: int):
    cur.execute(f"SELECT * FROM num_data WHERE number = {number}")
    if cur.fetchone() is not None:
        return f"ERROR: Number {number} has already been received"
    
    cur.execute(f"SELECT * FROM num_data WHERE number = {number + 1}")
    if cur.fetchone() is not None:
        return f"ERROR: Number {number} is less by one than one of received numbers"

    cur.execute(f"INSERT INTO num_data (number) VALUES ({number})")
    return (number + 1)

s = socket.socket()
host = socket.gethostname()
port=9600
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    #c.send(b"Thanks for connecting")
    number = int(c.recv(1024))
    print(f"Received number: {number}")
    new_number = process_request(number)
    print(new_number)
    c.send(str(new_number).encode("utf-8"))
    c.close()
