from funcs.crud_mongo import (list_db_itens, insert,
                              get_db, get_collection,
                              delete, update)

DB = get_db('productsDB')
COLLECTION = get_collection(DB, 'products')
MENU_STR = """
    Choose from the options:
    1 - List
    2 - Insert
    3 - Update
    4 - Delete
    Enter to leave.
    """

while True:
    print('Welcome to MongoDB CRUD')
    print(MENU_STR)
    try:
        opt = int(input('Option: '))
    except ValueError:
        print('Invalid option.')
        opt2 = input('Do you want to leave ? y-yes, n-no.\n')
        if opt2.lower() == 's':
            print('Leaving now.')
            break
        else:
            print('Try again!')
            print(MENU_STR)
            opt = int(input('Option: '))
        
    if opt == 1:
        list_db_itens(COLLECTION)
    if opt == 2:
        insert(COLLECTION)
    if opt == 3:
        obj_property = input('Which property do you want to change?\n')
        name = True if obj_property == 'name' else False
        price = True if obj_property == 'price' else False
        stock = True if obj_property == 'stock' else False
        update(COLLECTION, name, price, stock)
    if opt == 4:
        delete(COLLECTION)
