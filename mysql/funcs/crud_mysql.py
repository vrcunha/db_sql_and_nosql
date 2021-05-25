import MySQLdb


def connect(db_name, user_name, password, host_name='localhost'):
    """Connects to MySQL database."""
    try:
        connection = MySQLdb.connect(
            db=db_name,
            host=host_name,
            user=user_name,
            passwd=password
        )
        # print('Connection Succefully')
        return connection
    except MySQLdb.Error as e:
        print(f'Connection Error to MySQL server: {e}')


def disconnect(connection):
    """Disconnects to MySQL database."""
    connection.close()
    # print('Connection Closed.')

def list_db_columns():
    """List DB columns."""
    connection = connect(db_name='mysql_python.db', 
                        user_name='Isaac', 
                        password='123qwe'
                        )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    if len(produtos) > 0 :
        print('Table name: produtos')
        for produto in produtos:
            result = f'Id: {produto[0]} | Nome: {produto[1]} |'\
                     f' Preco: R$ {produto[2]} | Estoque: {produto[3]}'
            print(len(result)*'-')
            print(result)
    else:
        print('Table name: produtos is empty.')
    disconnect(connection)

def check_operation(connection, cursor):
    connection.commit()
    if cursor.rowcount == 1:
        print(f'Operação realizada com sucesso.')
    else:
        print(f'A operação falhou.')

def insert():
    """Insert new item in table."""
    connection = connect(db_name='mysql_python.db', 
                        user_name='Isaac', 
                        password='123qwe'
                        )
    cursor = connection.cursor()
    nome = input('Insira o Nome do produto: ')
    preco = input('Insira o Preço do produto: ')
    estoque = input('Insira o Estoque do produto: ')
    cursor.execute(f"INSERT INTO produtos" \
                   f"(nome, preco, estoque) VALUES " \
                   f"('{nome}', {preco}, {estoque})")
    check_operation(connection, cursor)
    disconnect(connection)

def update(id, name=False, price=False, stock=False):
    """Update an item selected by id."""
    connection = connect(db_name='mysql_python.db', 
                        user_name='Isaac', 
                        password='123qwe'
                        )
    cursor = connection.cursor()
    if name:
        new_name = input('Insira o novo nome do produto: ')
        cursor.execute(f"UPDATE produtos SET nome='{new_name}' WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('O nome do produto foi atualizado com sucesso.')
    if price:
        new_price = input('Insira o novo preço do produto: ')
        cursor.execute(f"UPDATE produtos SET preco={new_price} WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('O preço do produto foi atualizado com sucesso.')
    if stock:
        new_stock = input('Insira o novo estoque do produto: ')
        cursor.execute(f"UPDATE produtos SET estoque={new_stock} WHERE id = {int(id)}")
        check_operation(connection, cursor)
        print('O estoque do produto foi atualizado com sucesso.')
    else:
        print('Nenhum item foi atualizado.')
    disconnect(connection)

def delete(id):
    """Delete an item selected by id."""
    connection = connect(db_name='mysql_python.db', 
                        user_name='Isaac', 
                        password='123qwe'
                        )
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM produtos WHERE id = {int(id)}")
    check_operation(connection, cursor)
    disconnect(connection)