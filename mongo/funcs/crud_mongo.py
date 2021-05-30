from pymongo import MongoClient

def menu():
    MENU_STR = """
        Choose from the options:
        1 - List
        2 - Insert
        3 - Update
        4 - Delete
        Enter to leave.
        """
    print('Welcome to MongoDB CRUD')
    print(MENU_STR)
    try:
        opt = int(input('Option: '))
    except ValueError:
        print('Invalid option.')
        opt2 = input('Do you want to leave ? y-yes, n-no.\n')
        if opt2.lower() == 'y':
            print('Leaving now.')
            return None
        else:
            print('Try again!')
            print(MENU_STR)
            opt = int(input('Option: '))
    return opt

def get_enviroments_variables():
    """Get os enviroments varible.

    returns -> host(MONGODB_HOST) and port(MONGODB_PORT).
    """
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    host = os.getenv('MONGODB_HOST')
    port = int(os.getenv('MONGODB_PORT'))

    return host, port

host, port = get_enviroments_variables()

def connect(host, port):
    """Connect to MongoDB system and return a client.

    Keyword arguments:
    host -- database host address
    port -- database port

    Return -> client (instance of MongoClient)
    """

    return MongoClient(host, port)

def disconnect(client):
    """Disconnects from MongoDB system."""
    client.close()

def create_db(db_name):
    """Create a db.

    Keyword arguments:
    db_name -- Name to create db (str)

    Return -> db
    """
    client = connect(host, port)
    db = client[f'{db_name}']
    return db

def delete_db(db_name):
    """Delete a db.

    Keyword arguments:
    client -- MongoClient instance
    db_name -- Name to delete db (str)
    """
    client = connect(host, port)
    client.drop_database(f'{db_name}')
    print(f'The {db_name} database was excluded.')

def create_collections(db, collection_name):
    """Create a collection.

    Keyword arguments:
    db -- Database from MongoDB.
    collection_name -- Name to create a collection. (str)

    Return -> Collection
    """
    collection = db[f'{collection_name}']
    return collection

def get_db(db_name=None):
    """Get a db if exists on MongoDB system.

    Keyword arguments:
    db_name -- Name to search inside MongoDB.

    Return -> db
    """
    client = connect(host, port)
    if db_name in client.list_database_names():
        print(f"The database {db_name} exists.")
        db = client[f"{db_name}"]
        return db
    if db_name == None:
        print(client.list_database_names())
        return None

def make_connection(db_name,  collec_name):
    try:
        DB = get_db(db_name)
        COLLECTION = get_collection(DB, collec_name)
    except AttributeError as f:
        print('DB Not Found.')
        try:
            # if DB == None and COLLECTION == None:
            DB = create_db(input('Enter new name to create DB: '))
            COLLECTION = create_collections(DB,
                                            input('Enter new name to a collection: '))
        except UnboundLocalError as e:
            print(e)
    return DB, COLLECTION

def get_collection(db, collection):
    """Get a collection if exists on MongoDB system.

    Keyword arguments:
    db -- Database from MongoDB
    collection -- Name to search inside MongoDB.

    Return -> collection
    """
    if collection in db.list_collection_names():
        print("This collection exists.")
        return db[f'{collection}']
    if collection not in db.list_collection_names():
        print("This collection doesn't exists.")
        return None

def insert(collection):
    """Insert item inside collection in database.

    insert_one: insert one item in the collection.
    insert_many: insert many itens in the collection.

    Keyword arguments:
    collection -- Name of the collection on database.
    """
    quant = int(input('How many itens you want to insert: '))
    properties = int(input('How much properties this item have? '))
    itens_input = [{
    input('Enter key name: '): input('Enter value: ') for x in range(properties)
    } for i in range(quant)]
    if quant == 1:
        collection.insert_one(itens_input[0])
    if quant > 1:
        collection.insert_many(itens_input)

def list_itens(collection):
    """List itens from database.

    Keyword arguments:
    collection -- Name of the collection on database.
    """
    db_list = collection.find()
    if collection.count_documents({}) > 0:
        for item in db_list:
            print(len(item)*'-')
            print(item)
    else:
        print('This collection is empty.')


def update(collection):
    """Update an item selected by id."""
    db_list = collection.find({})
    for idx, item in enumerate(db_list, start=1):
            print(len(item)*'-')
            print(idx, item)
    db_list = collection.find({})
    idx = int(input('Select the object to update by index: '))
    prod_id = {'_id': db_list[idx-1]['_id']}

    update_result = collection.update_one(prod_id, {'$set':
                    {input('Enter property name: '):
                     input('Enter new property value: ')}
                     })
    if update_result.modified_count == 1:
        print('Product name successfully updated.')

    else:
        print('No items have been updated.')

def delete(collection):
    """Delete an item selected by id."""
    db_list = collection.find({})
    for idx, item in enumerate(db_list, start=1):
            print(len(item)*'-')
            print(idx, item)
    db_list = collection.find({})
    idx = int(input('Select the object to update by index: '))
    prod_id = {'_id': db_list[idx-1]['_id']}
    del_result = collection.delete_one(prod_id)
    if del_result.deleted_count > 1:
        print('Item delect successfully.')
