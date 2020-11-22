from sqlalchemy import create_engine
import pandas as pd
import psycopg2

#engine = create_engine('postgresql://postgres:password@localhost:5432/sp500xxx')

#conn = psycopg2.connect()
conn = psycopg2.connect(
    database = "sp500xxx",
    user = "postgres",
    password = "password",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()

#cur.excute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")
#cur.execute("INSERT INTO student (name) VALUES(%s)",
#            ("Anthony",))

cur.execute("select * from wikitablescrapexxx where ticker = 'GOOG'")
#print(cur.fetchall())
yankees= cur.fetchall()

for x in yankees:
    print(x[1:13])












#conn.close()

#print(cur.fetchall())

#cur.execute("SELECT * FROM student WHERE id = ")

#conn.commit()

#cur.close()

#conn.close()