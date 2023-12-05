import requests
import psycopg2


def process_request(request):
    number = int(request.data)

    cur.execute(f"SELECT * FROM data WHERE number = {number}")

    if cur.fetchone() is not None:
        return f"ERROR: Number {number} has already been received"

    cur.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
    last_number = cur.fetchone()[1]

    if number != last_number + 1:
        return f"ERROR: Incremented number has already been received"

    cur.execute(f"INSERT INTO data (number) VALUES {number + 1}")
    conn.commit()
    return str(number + 1)


if __name__ == '__main__':
    while True:
        conn = psycopg2.connect(
        host     = "localhost",
        database = "mydb",
        user     = "admin",
        password = "password"
            )
        
        cur = conn.cursor()
        request  = requests.get("http://localhost:8000")
        response = process_request(request)
        requests.post("http://localhost:8000", data=response)
