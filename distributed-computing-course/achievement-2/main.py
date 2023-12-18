import os
import sys
import psycopg2
from flask import Flask, request, redirect, render_template


app = Flask(__name__)


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="password",
        port=5432
        )
    conn.autocommit = True
    return conn


def check_number(conn, number):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM num_data WHERE number = {number}")
    result = cur.fetchone()

    return result


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/success', methods=['GET', 'POST'])
def sucess():
    error = ''
    number = int(request.form.get('number'))
    conn = connect_db()
    result = check_number(conn,int(number))
    if result is not None:
        error = f"ERROR: Number {number} has already been received"
        return render_template('index.html', answer=error)

    result = check_number(conn, int(number) + 1)
    if result is not None:
        error = f"ERROR: Number {number} is less by one than one of received numbers"
        return render_template('index.html', answer=error)

    cur = conn.cursor()
    cur.execute(f"INSERT INTO num_data (number) VALUES ({number})")
    
    new_number = number + 1

    return render_template('index.html', answer=new_number)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
