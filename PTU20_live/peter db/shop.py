import sqlite3

connector = sqlite3.connect('shop_py.db')
cursor = connector.cursor()

def create_tables(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    queries = [
        '''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(50) NOT NULL,
            price DECIMAL(10,2) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS bill (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purchase_time DATETIME NOT NULL,
            cashier_id INTEGER NOT NULL,
            customer_id INTEGER REFERENCES customer(id)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS bill_line (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_id INTEGER REFERENCES bill(id),
            product_id INTEGER REFERENCES product(id),
            quantity DECIMAL(10,2)
        );
        '''
    ]

    for query in queries:
        cursor.execute(query)

    connector.commit()

def customer_exists(cursor: sqlite3.Cursor, first_name: str, last_name: str):
    cursor.execute("SELECT COUNT(*) FROM customer WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    count = cursor.fetchone()[0]
    return count > 0

def insert_customer(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Įvedami pirkėjo duomenys' )
    first_name = input('Įveskite savo vardą: ')
    last_name = input('įveskite savo pavardę: ')
    if customer_exists(cursor, first_name, last_name):
        print('Pirkėjas su tokiu vardu ir pavarde jau yra duomenų bazėje.')
    else:
        with connector:
            cursor.execute("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
            print('Pirkėjo duomenys sėkmingai įvesti.')    
    
def default_products(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute("SELECT COUNT(*) FROM product")
        count = cursor.fetchone()[0]
        if count == 0:
            default_products = [
            ('Big Tasty', 5.15),
            ('Big mac', 4,20),
            ('McChickeN', 4,10),
            ('Filet-o-Fish', 4,20),
            ('McWrap', 5.10),
            ('Mėsainis su sūriu', 1.60),
            ('Bulvytės didelė porcija', 2.55),
            ('Bulvytės vidutinė porcija', 2,20),
            ('Coca Cola', 2.60),
            ('Kava', 2.20),
            ('Sultys', 2.65),
        ]

            with connector:
                cursor.executemany("INSERT INTO product (product_name, price) VALUES (?, ?)", default_products)
                print('Numatytieji produktai sėkmingai įvesti.')
        else:
            print('Produktai jau yra duomenų bazėje. Numatytieji produktai nebuvo įvesti.')

def check_products(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    if products:
        print("Produktai duomenų bazėje:")
        for product in products:
            print(product)
    else:
        print("Duomenų bazėje nėra produktų.")


connector = sqlite3.connect('your_database.db')
cursor = connector.cursor()

# Patikriname, ar produktai jau yra duomenų bazėje
check_products(connector, cursor)

def create_bill():
    pass

def create_bill_line():
    pass







