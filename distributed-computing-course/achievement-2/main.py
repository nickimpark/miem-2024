import os
import sys
import psycopg2
from flask import Flask, request, redirect


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


@app.route('/redirect_error_1')
def redirect_error_1(number):
    return f"ERROR: Number {number} has already been received"
    
@app.route('/redirect_error_2')
def redirect_error_2(number):
    return f"ERROR: Number {number} is less by one than one of received numbers"


@app.route('/redirect_success')
def redirect_error(number):
    return f'{number}'

@app.route('/', methods=['POST'])
def main():
    number = request.form.get('number')
    conn = connect_db()

    result = check_number(conn,int(number))
    if result is not None:
        return redirect(number)('/redirect_error_1')

    result = check_number(conn, int(number) + 1)
    if result is not None:
        return redirect(number)('/redirect_error_2')

    cur = conn.cursor()
    cur.execute(f"INSERT INTO num_data (number) VALUES ({number})")

    return redirect(number)('/redirect_success')


if __name__ == "__main__":
    app = Flask(__name__)
    app.run()
