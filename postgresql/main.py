from mongo.main import MENU_STR
from funcs.crud_postgresql import (list_db_columns, insert,
                                   delete, update)

MENU_STR = """
    Choose from the options:
    1 - List
    2 - Insert
    3 - Update
    4 - Delete
    Enter to leave.
    """

while True:
    print('Welcome to PostgreSQL CRUD')
    print(MENU_STR)
    try:
        opt = int(input('Option: '))
    except ValueError:
        print('Invalid option.')
        opt2 = input('Do you want to leave ? y-yes, n-no.\n')
        if opt2.lower() == 'y':
            print('Leaving now.')
            break
        else:
            print('Try again!')
            print(MENU_STR)
            opt = int(input('Option: '))
        
    if opt == 1:
        list_db_columns()
    if opt == 2:
        insert()
    if opt == 3:
        obj_id = int(input('Insert the object id: '))
        obj_property = input('Which property do you want to change?\n')
        try:
            name = True if obj_property == 'name' else False
            price = True if obj_property == 'price' else False
            stock = True if obj_property == 'stock' else False
            update(obj_id, name, price, stock)
        except psycopg2.errors.UndefinedColumn as e:
            print(f'{e}')
    if opt == 4:
        obj_id = int(input('Insert the object id: '))
        delete(obj_id)
