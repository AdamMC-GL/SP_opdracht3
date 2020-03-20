import psycopg2
from pprint import pprint
import random


def get_cursor():
    c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    cur = c.cursor()

    return cur


def get_all_customers():
    cur = get_cursor()
    cur.execute("SELECT id, segment FROM profiles WHERE segment IS NOT NULL;")
    myresult = cur.fetchall()
    random.shuffle(myresult)  # so every products has a chance to be recommended

    return myresult


def get_similar_items(all_customers):
    list_similar_cust_id = []
    for All_cust in all_customers:
        similar_cust_id = [All_cust[0]]  # Always starts with id for primary key
        for comparing_item in all_customers:
            if All_cust[1] == comparing_item[1] and All_cust[0] != comparing_item[0]:  # if segments are the same, but the id's are not the same
                similar_cust_id.append(comparing_item[0])
                list_similar_cust_id.append(similar_cust_id)
                break
    
    return list_similar_cust_id


def insert_similar_customers(list_similar_cust_id):
    cur = get_cursor()
    cur.execute("DELETE FROM similar_customers")
    for similar_customers in list_similar_cust_id:
        values = tuple(similar_customers)
        sql = "INSERT INTO similar_customers VALUES (%s, %s)"
        cur.execute(sql, values)


def close_everything():
    c = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc")
    c.commit()
    c.close()


def main():
    all_customers = get_all_customers()
    list_similar_cust_id = get_similar_items(all_customers[:50000])
    insert_similar_customers(list_similar_cust_id)
    close_everything()


if __name__ == "__main__":
    main()
