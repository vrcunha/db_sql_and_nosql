import os
import socket
import couchdb
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connect():
    """Connects to PostgreSQL database."""
    conn = couchdb.Server(f"http://{os.getenv('COUCHDB_USER')}:"\
                          f"{os.getenv('COUCHDB_PASSWORD')}@"\
                          f"{os.getenv('COUCHDB_HOST')}:"\
                          f"{os.getenv('COUCHDB_PORT')}")
    db_name = 'productsdb'
    if db_name in conn:
        return conn[db_name]
    else:
        try:
            return conn.create(db_name)
        except socket.gaierror as e:
            print(f'Connection Error. {e}')
        except couchdb.http.Unauthorized as f:
            print(f'Unauthorized Connection. {f}')
        except ConnectionRefusedError as g:
            print(g)

def insert():
    db = connect()

    if db:
        product = {"name": input('Enter the product name: '), 
                   "price": float(input('Enter the product price: ')), 
                   "stock": int(input('Enter the product stock: '))}
        result = db.save(product)
        if result:
            print(f"Product {product['name']} inserted on the database.")
        else:
            print('Not possible to insert the product.')
    else:
        print('Connection Error.')


def list_db_itens():
    """List DB columns."""
    db = connect()
    if db:
        if db.info()['doc_count'] > 0:
            for doc in db:
                print(f"\nId: {db[doc]['_id']}")
                print(f"Rev: {db[doc]['_rev']}")
                print(f"Product: {db[doc]['name']}")
                print(f"Price: {db[doc]['price']}")
                print(f"Stock: {db[doc]['stock']}\n")
        else:
            print('There isn`t any product in this database.')
    else:
        print('Connection Error.')

def update(name=False, price=False, stock=False):
    """Update an item selected by id."""
    db = connect()
    if db:
        key = input('Enter your product id: ')
        try:
            doc = db[key]
            if name:
                doc['name'] = input('Enter new product name: ')
                db[doc.id] = doc
                print('Product name successfully updated.')
                return
            if price:
                doc['price'] = float(input('Enter new product price: '))
                db[doc.id] = doc
                print('Product price successfully updated.')
                return
            if stock:
                doc['price'] = int(input('Enter new product stock: '))
                db[doc.id] = doc
                print('Product stock successfully updated.')
                return
            else:
                print('No items have been updated.')
        except couchdb.http.ResourceNotFound as e:
            print(f'Product not found. {e}')
    else:
        print('Connection Error.')

def delete():
    """Delete an item selected by id."""
    db = connect()
    if db:
        key = input('Enter product id: ')
        try:
            db.delete(db[key])
            print('Product successfully deleted.')
        except couchdb.http.ResourceNotFound as e:
            print('Operation failed.')
    else:
        print('Connection Error.')
