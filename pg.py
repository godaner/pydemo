import psycopg2

conn = psycopg2.connect(
    dbname="zdns",
    user="zdns",
    password="zdns",
    host="202.173.9.26",
    port="5432"
)
cur = conn.cursor()
cur.execute('select * from zc_zdnsuser;')
rows = cur.fetchall()
for row in rows:
    print(row, end="\r\n")
