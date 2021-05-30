from funcs.crud_mongo import (list_itens, insert, make_connection,
                              create_db, create_collections, menu,
                              get_db, get_collection, delete, update)

DB, COLLECTION = make_connection(
    input('DB name: '), input('Collection name: ')
)

while True:
    opt = menu()
    if opt == 1:
        list_itens(COLLECTION)
    if opt == 2:
        insert(COLLECTION)
    if opt == 3:
        update(COLLECTION)
    if opt == 4:
        delete(COLLECTION)
    if opt == None:
        break
