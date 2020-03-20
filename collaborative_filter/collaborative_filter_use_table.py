import psycopg2
import random


def get_cursor():
    cur = psycopg2.connect("dbname=Huwebshop user=postgres password=1qaz2wsx3edc").cursor()
    return cur


def get_random_customer():
    cur = get_cursor()
    query = "SELECT * FROM profiles_previously_viewed;"
    cur.execute(query)
    all_customers = cur.fetchall()

    random_customer = all_customers[random.randint(1, 101)]
    return random_customer


def get_sim_cust_ids(id):
    cur = get_cursor()
    id = "\'" + id + "\'"
    query = "SELECT sim_id_1 FROM similar_customers WHERE id= " + str(id)
    cur.execute(query)
    myresult = cur.fetchall()

    return myresult


def get_items_via_sim_cust(id):
    cur = get_cursor()
    id = "\'" + id + "\'"
    query = "SELECT prodid FROM profiles_previously_viewed WHERE profid= " + str(id)
    cur.execute(query)
    myresult = cur.fetchall()

    return myresult


def main():
    while True:
        customer = get_random_customer()
        similar_customer = get_sim_cust_ids(customer[0])
        if len(similar_customer) > 0:
            break

    rec_item = get_items_via_sim_cust(similar_customer[0][1])

    print('Customer: ' + str(customer[0]) + ' might also like: ')
    print(rec_item)


if __name__ == "__main__":
    main()
