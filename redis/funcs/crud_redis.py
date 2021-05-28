import os
import redis
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connect():
    """Connects to PostgreSQL database."""
    return redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

def disconnect(connection):
    """Disconnects to MySQL database."""
    connection.connection_pool.disconnect()
    # print('Connection Closed.')

def id_generator():
    conn = connect()
    try:
        key = conn.get('key')
        if key:
            key = conn.incr('key')
            return key
        else:
            conn.set('key', 1)
            return 1
    except redis.exceptions.ConnectionError as e:
        print(f'Connection error. {e}')

def insert():
    conn = connect()

    name = input('Enter the product name: ')
    price = float(input('Enter the product price: '))
    stock = int(input('Enter the product stock: '))

    product = {"name": name, "price": price, "stock": stock}
    key = f'product:{id_generator()}'
    try:
        result = conn.hmset(key, product)
        if result:
            print(f'Product {name} inserted on the database.')
        else:
            print('Not possible to insert the product.')
    except redis.exceptions.ConnectionError as e:
        print(e)


def list_db_itens():
    """List DB columns."""
    conn = connect()
    try:
        data = conn.keys(pattern='product:*')
        if len(data) > 0:
            for key in data:
                products = conn.hgetall(key)
                print(f"\nId: {str(key, 'utf-8', 'ignore')}")
                print(f"Product: {str(products[b'name'], 'utf-8', 'ignore')}")
                print(f"Price: {str(products[b'price'], 'utf-8', 'ignore')}")
                print(f"Stock: {str(products[b'stock'], 'utf-8', 'ignore')}\n")
        else:
            print('There isn`t any product in this database.')
    except redis.exceptions.ConnectionError as e:
        print(f'Not possible to list the itens. {e}')
    disconnect(conn)

def update(name=False, price=False, stock=False):
    """Update an item selected by id."""
    conn = connect()
    key = input('Enter your product key: ')
    if name:
        new_name = input('Enter new product name: ')
        result = conn.hset(key, "name", new_name)
        if result:
            print('Product name successfully updated.')
            return
    if price:
        new_price = float(input('Enter new product price: '))
        result = conn.hset(key, "price", new_price)
        if result:
            print('Product price successfully updated.')
            return
    if stock:
        new_stock = int(input('Enter new product stock: '))
        result = conn.hset(key, "stock", new_stock)
        if result:
            print('Product stock successfully updated.')
            return
    else:
        print('No items have been updated.')

def delete():
    """Delete an item selected by id."""
    conn = connect()
    key = input('Enter product key: ')
    result = conn.delete(key)
    if result:
        print('Item delect successfully.')