import psycopg2

c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
cur = c.cursor()


cur.execute("DROP TABLE IF EXISTS similar_customers CASCADE")

cur.execute("""CREATE TABLE similar_customers
                (id VARCHAR PRIMARY KEY,
                 sim_id_1 VARCHAR);""")

c.commit()
cur.close()
c.close()
