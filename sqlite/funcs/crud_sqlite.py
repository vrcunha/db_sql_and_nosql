import os
import sqlite3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connect():
    """Connects to PostgreSQL database."""
    try:
        connection = sqlite3.connect('sqlite_python.db')
        # print('Connection Succefully')
        return connection
    except sqlite3.Error as e:
        print(f'Connection Error to SQLite server: {e}')


def disconnect(connection):
    """Disconnects to MySQL database."""
    connection.close()
    # print('Connection Closed.')

def list_db_columns():
    """List DB columns."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    produtos = cursor.fetchall()
    if len(produtos) > 0 :
        print('Table name: products')
        for produto in produtos:
            result = f'Id: {produto[0]} | Name: {produto[1]} |'\
                     f' Price: R$ {produto[2]} | Stock: {produto[3]}'
            print(len(result)*'-')
            print(result)
    else:
        print('Table name: products is empty.')
    disconnect(connection)

def check_operation(connection, cursor):
    connection.commit()
    if cursor.rowcount == 1:
        print(f'Operação realizada com sucesso.')
    else:
        print(f'A operação falhou.')

def insert():
    """Insert new item in table."""
    connection = connect()
    cursor = connection.cursor()
    nome = input('Enter product name: ')
    preco = input('Enter product price: ')
    estoque = input('Enter product stock: ')
    cursor.execute(f"INSERT INTO products" \
                   f"(name, price, stock) VALUES " \
                   f"('{nome}', {preco}, {estoque})")
    check_operation(connection, cursor)
    disconnect(connection)

def update(id, name=False, price=False, stock=False):
    """Update an item selected by id."""
    connection = connect()
    cursor = connection.cursor()
    if name:
        new_name = input('Enter new product name: ')
        cursor.execute(f"UPDATE products SET name='{new_name}' WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('Product name successfully updated.')
    if price:
        new_price = input('Enter new product price: ')
        cursor.execute(f"UPDATE products SET price={new_price} WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('Product price successfully updated.')
    if stock:
        new_stock = input('Enter new product stock: ')
        cursor.execute(f"UPDATE products SET stock={new_stock} WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('Product stock successfully updated.')
    else:
        print('No items have been updated. ')
    disconnect(connection)

def delete(id):
    """Delete an item selected by id."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM products WHERE id = {int(id)}")
    check_operation(connection, cursor)
    disconnect(connection)