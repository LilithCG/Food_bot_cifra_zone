import sqlite3

cursor = None
connection = None


def connect_database():
    global cursor, connection
    connection = sqlite3.connect("modules/db/delivery_bot.db")
    cursor = connection.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users
    (
        id integer NOT NULL PRIMARY KEY,
        name character varying(250) NOT NULL,
        ref character varying(250) NOT NULL,
        phone string
        
        
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pizza_cheddar (
        id integer PRIMARY KEY,
        category string NOT NULL,
        name string NOT NULL,
        description string NOT NULL,
        price string NOT NULL,
        image string NOT NULL,
        link string NOT NULL
    )
    """)
    cursor.execute('DROP TABLE orders')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
	    order_id integer PRIMARY KEY,
	    creator_chat_id string NOT NULL,
	    creator_ref string NOT NULL,
	    delivery_name string NOT NULL,
	    delivery_table string NOT NULL,
	    status string NOT NULL
	)
    """)
    cursor.execute('DROP TABLE basket')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS basket (
	    id integer PRIMARY KEY,
	    order_id integer,
	    chat_id string,
	    name string,
	    food_id string
    )
    """)

    connection.commit()


def insert_user(chat_id, name, ref):
    new_user = (chat_id, name, ref)
    cursor.execute("INSERT INTO users VALUES(?, ?, ?)", new_user)
    connection.commit()


def insert_food(food_data):
    cursor.executemany("INSERT INTO pizza_cheddar(category,name,description,price,image,link) VALUES(?,?,?,?,?,?);",
                       food_data)
    connection.commit()


def insert_order(order_id, creator_chat_id, creator_ref, delivery_name, delivery_table, status):
    new_order = (order_id, creator_chat_id, creator_ref, delivery_name, delivery_table, status)
    cursor.execute("INSERT INTO orders VALUES(?,?,?,?,?,?)", new_order)
    connection.commit()


def insert_to_basket(order_id, chat_id, name, food_id):
    basket_pos_data = (order_id, chat_id, name, food_id)
    cursor.execute("INSERT INTO basket(order_id,chat_id,name,food_id) VALUES(?,?,?,?);", basket_pos_data)
    connection.commit()


def delete_product_from_basket(order_id, chat_id, product_id):
    cursor.execute(f"DELETE FROM basket WHERE order_id='{order_id}' and chat_id='{chat_id}' and id='{product_id}'")
    connection.commit()


def select_all_current_orders():
    cursor.execute("SELECT * FROM orders WHERE status='new';")
    all_results = cursor.fetchall()
    return all_results


def select_all_food_from_category(category_name):
    cursor.execute(f"SELECT id,name, price, image FROM pizza_cheddar WHERE category='{category_name}'")
    all_results = cursor.fetchall()
    return all_results


def get_product_name(product_id):
    cursor.execute(f"SELECT name FROM pizza_cheddar WHERE id='{product_id}'")
    all_results = cursor.fetchall()
    return all_results[0][0]


def select_basket_user(chat_id):
    cursor.execute(f"SELECT id, name, food_id FROM basket WHERE chat_id = {chat_id}")
    all_results = cursor.fetchall()
    return all_results


def select_all_basket():
    cursor.execute(f"SELECT chat_id, name, food_id FROM basket")
    all_results = cursor.fetchall()
    return all_results


def select_all_users():
    cursor.execute("SELECT id FROM users;")
    all_chat_ids = cursor.fetchall()
    return all_chat_ids


def select_link(id):
    cursor.execute(f"SELECT link FROM pizza_cheddar WHERE id = {id}")
    all_results = cursor.fetchall()
    return all_results[0][0]


def select_price(id):
    cursor.execute(f"SELECT price FROM pizza_cheddar WHERE id = {id}")
    all_results = cursor.fetchall()
    return all_results[0][0]


def select_ref(chat_id):
    cursor.execute(f"SELECT ref FROM users WHERE id = {chat_id}")
    all_results = cursor.fetchall()
    return all_results[0][0]


def delete_all_basket():
    cursor.execute(f"DELETE FROM basket")
    connection.commit()

def close_order():
    cursor.execute(f"UPDATE orders SET status = 'old', order_id=random() WHERE order_id = 1")
    connection.commit()
