from funcs.crud_mysql import (list_db_columns, insert,
                              delete, update)


while True:
    print('Bem vindo ao CRUD - MySQL')
    print("""
    Escolha entre as opções:
    1 - Listar
    2 - Inserir
    3 - Update
    4 - Delete
    Enter para Sair
    """)
    try:
        opt = int(input('Opção: '))
    except ValueError:
        print('Opção inválida.')
        opt2 = input('Deseja Sair? s-sim, n-não. ')
        if opt2.lower() == 's':
            print('Saindo.')
            break
        else:
            print('Tente de novo!')
            print("""
                Escolha entre as opções:
                1 - Listar
                2 - Inserir
                3 - Update
                4 - Delete
                Enter para Sair
                """)
            opt = int(input('Opção: '))
        
    if opt == 1:
        list_db_columns()
    if opt == 2:
        insert()
    if opt == 3:
        obj_id = int(input('Insira o id do objeto: '))
        print('Qual propriedade deseja alterar?')
        obj_property = input('')
        name = True if obj_property == 'nome' else False
        price = True if obj_property == 'preco' else False
        stock = True if obj_property == 'estoque' else False
        update(obj_id, name, price, stock)
    if opt == 4:
        obj_id = int(input('Insira o id do objeto: '))
        delete(obj_id)
