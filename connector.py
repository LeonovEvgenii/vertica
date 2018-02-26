import psycopg2

try:
    conn = psycopg2.connect("dbname='vertica_db' user='vertica'" \
                            " host='localhost' password='123'")
except:
    print("Connection error")
  
sql = 'SELECT * FROM "склад";'

try:
    cur = conn.cursor()
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # by column name
    cur.execute(sql)
    data = cur.fetchall()
except Exception as e:
    print("Query error: ", e)
    
print(data)