import os
import pyrebase
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def connect():
    """Connects to PostgreSQL database."""
    config = {
        "apiKey": {os.getenv('FIREBASE_APIKEY')},
        "authDomain": {os.getenv('FIREBASE_AUTHDOMAIN')},
        "databaseURL": "https://cursodb-160cb-default-rtdb.firebaseio.com",
        "storageBucket": {os.getenv('FIREBASE_STORAGE')}
    }
    conn = pyrebase.initialize_app(config)
    return conn.database()

def insert():
    db = connect()
    product = {"name": input('Enter the product name: '), 
               "price": float(input('Enter the product price: ')), 
               "stock": int(input('Enter the product stock: '))}
    result = db.child('products').push(product)
    if 'name' in result:
        print(f"Product {product['name']} inserted on the database.")
    else:
        print('Not possible to insert the product.')


def list_db_itens():
    """List DB columns."""
    db = connect()

    products = db.child('products').get()
    if products.val():
        for product in products.each():
            print(f"\nId: {product.key()}")
            print(f"Product: {product.val()['name']}")
            print(f"Price: {product.val()['price']}")
            print(f"Stock: {product.val()['stock']}\n")
    else:
        print('There isn`t any product in this database.')

def update(name=False, price=False, stock=False):
    """Update an item selected by id."""
    db = connect()

    key = input('Enter your product id: ')
    product = db.child('products').child(key).get()
    if product.val():
        if name:
            db.child('products').child(key).update({"name":input('Enter new product name: ')})
            print('Product name successfully updated.')
            return
        if price:
            db.child('products').child(key).update({"price":float(input('Enter new product price: '))})
            print('Product price successfully updated.')
            return
        if stock:
            db.child('products').child(key).update({"stock":int(input('Enter new product stock: '))})
            print('Product stock successfully updated.')
            return
        else:
            print('No items have been updated.')

def delete():
    """Delete an item selected by id."""
    db = connect()

    key = input('Enter product id: ')

    product = db.child('products').child(key).get()
    if product.val():
        db.child('products').child(key).remove()
        print('Product deleted.')
    else:
        print('Product not found.')
