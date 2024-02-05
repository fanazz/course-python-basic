import sqlite3

connector = sqlite3.connect('gptshop_py.db')
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

def insert_data(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    product_data = [
        ('Big Tasty', 5.15),
        ('Big mac', 4.20),
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
    for product_entry in product_data:
        product_name, price = product_entry
        

    cursor.execute("INSERT INTO product (product_name, price) VALUES (?, ?)", product_data)

    customer_data = [
        ('Keenan', 'Evans'),
        ('Brady', 'Manek'),
        ('Andrea', 'Trinchieri'),
        ('Tautvydas', 'Sabonis')
    ]

    cursor.executemany("INSERT INTO customer (first_name, last_name) VALUES (?, ?)", customer_data)

    bill_data = [
        ('2024-01-25 12:30:17', 1, 3),
        ('2024-01-02 9:00:45', 1, 2),
        ('2023-12-31 11:59:33', 2, 3),
        ('2024-01-07 04:25:01', 4, 1),
        ('2024-01-13 10:15:59', 1, 4),
        ('2024-01-18 21:45:44', 1, 2),
        ('2024-01-04 16:15:07', 3, 1),
        ('2024-01-08 18:25:14', 2, 3),
        ('2024-01-30 18:40:33', 1, 2),
        ('2024-01-22 07:30:48', 3, 4),
        ('2024-01-19 19:42:51', 4, 1),
        ('2024-01-20 18:37:19', 2, 2),
        ('2024-01-27 13:13:13', 2, 3)
    ]

    cursor.executemany("INSERT INTO bill (purchase_time, cashier_id, customer_id) VALUES (?, ?, ?)", bill_data)

    bill_line_data = [
        (6, 1, 1),
        (6, 7, 1),
        (6, 10, 1),
        (1, 6, 5),
        (1, 2, 5),
        (1, 8, 5),
        (1, 9, 5),
        (4, 5, 3),
        (3, 3, 2),
        (12, 9, 4),
        (8, 7, 0.7),
        (7, 2, 8),
        (7, 8, 8),
        (5, 1, 1),
        (5, 10, 1),
        (2, 9, 3),
        (2, 5, 3),
        (9, 6, 15),
        (9, 11, 13),
        (10, 11, 3),
        (11, 7, 7),
        (13, 4, 4)
    ]

    cursor.executemany("INSERT INTO bill_line (bill_id, product_id, quantity) VALUES (?, ?, ?)", bill_line_data)

   
    connector.commit()

connector = sqlite3.connect('gptshop_py.db')
cursor = connector.cursor()

create_tables(connector, cursor)

insert_data(connector, cursor)

connector.close()


