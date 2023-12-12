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

cur.execute("DROP TABLE IF EXISTS num_data;")
cur.execute("CREATE TABLE num_data (id SERIAL PRIMARY KEY, number integer NOT NULL);")
cur.execute("SELECT * FROM num_data;")
print(cur.fetchone())
