import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connect():
    """Connects to PostgreSQL database."""
    client = MongoClient(os.getenv('MONGODB_HOST'), int(os.getenv('MONGODB_PORT')))
    print('Connection Succefully')
    return client

def disconnect(client):
    """Disconnects to MySQL database."""
    client.close()
    # print('Connection Closed.')

def create_db(client, db_name):
    db = client[f'{db_name}']
    return db

def delete_db(client, db_name):
    client.drop_database(f'{db_name}')
    print(f'The {db_name} database was excluded.')

def create_collections(db, collection_name):
    collection = db[f'{collection_name}']
    return collection

def get_db(db_name):
    client = connect()
    if db_name in client.list_database_names():
        print(f"The database {db_name} exists.")
        db = client[f"{db_name}"]
        return db

def get_collection(db, collection):
    if collection in db.list_collection_names():
        print("This collection exists.")
        return db[f'{collection}']

def insert(collection):
    quant = int(input('How many itens you want to insert: '))
    itens_input = [{
        "name": input('Enter product name: '),
        "price": input('Enter product price: '),
        "stock": input('Enter product stock: ')
        } for i in range(quant)]
    if quant == 1:
        collection.insert_one(itens_input[0])
    if quant > 1:
        collection.insert_many(itens_input)

def list_db_itens(collection):
#     """List DB columns."""
    db_list = collection.find()
    if collection.count_documents({}) > 0:
        for item in db_list:
            result = f"Id: {item['_id']} | Nome: {item['name']} |"\
                     f" Preco: R$ {item['price']} | Estoque: {item['stock']}"
            print(len(result)*'-')
            print(result)
    else:
        print('This collection is empty.')


def update(collection, name=False, price=False, stock=False):
    """Update an item selected by id."""
    db_list = collection.find({})
    for idx, item in enumerate(db_list, start=1):
            result = f"{idx} - Id: {item['_id']} | Nome: {item['name']} |"\
                        f" Preco: R$ {item['price']} | Estoque: {item['stock']}"
            print(len(result)*'-')
            print(result)
    db_list = collection.find({})
    idx = int(input('Select the object to update by index: '))
    prod_id = {'_id': db_list[idx-1]['_id']}
    if name:
        new_name = {'name': input('Enter new product name: ')}
        update_result = collection.update_one(prod_id, {'$set': new_name})
        if update_result.modified_count == 1:
            print('Product name successfully updated.')
    if price:
        new_price = {'price': input('Enter new product price: ')}
        update_result = collection.update_one(prod_id, {'$set': new_price})
        if update_result.modified_count == 1:
            print('Product price successfully updated.')
    if stock:
        new_stock = {'stock': input('Enter new product stock: ')}
        update_result = collection.update_one(prod_id, {'$set': new_stock})
        if update_result.modified_count == 1:
            print('Product stock successfully updated.')
    else:
        print('No items have been updated.')

def delete(collection):
    """Delete an item selected by id."""
    db_list = collection.find({})
    for idx, item in enumerate(db_list, start=1):
            result = f"{idx} - Id: {item['_id']} | Nome: {item['name']} |"\
                        f" Preco: R$ {item['price']} | Estoque: {item['stock']}"
            print(len(result)*'-')
            print(result)
    db_list = collection.find({})
    idx = int(input('Select the object to update by index: '))
    prod_id = {'_id': db_list[idx-1]['_id']}
    del_result = collection.delete_one(prod_id)
    if del_result.deleted_count > 1:
        print('Item delect successfully.')