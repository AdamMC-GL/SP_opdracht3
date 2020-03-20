import psycopg2

c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
cur = c.cursor()


cur.execute("DROP TABLE IF EXISTS similar_products CASCADE")

cur.execute("""CREATE TABLE similar_products
                (id VARCHAR PRIMARY KEY,
                 sim_id_1 VARCHAR,
                 sim_id_2 VARCHAR,
                 sim_id_3 VARCHAR,
                 FOREIGN KEY (sim_id_1) REFERENCES products(id),
                 FOREIGN KEY (sim_id_2) REFERENCES products(id),
                 FOREIGN KEY (sim_id_3) REFERENCES products(id));""")

c.commit()
cur.close()
c.close()
