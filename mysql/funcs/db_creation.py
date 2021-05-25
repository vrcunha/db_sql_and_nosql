from sqlalchemy import (create_engine, MetaData, Column, 
                        Table, Integer, String, DECIMAL
                        )
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql+mysqldb://Isaac:123qwe@localhost/mysql_python.db', echo=False)

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(bind=engine)

produtos = Table('produtos', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False),
    Column('preco', DECIMAL(8,2), nullable=False),
    Column('estoque', String(50), nullable=False)
)

metadata.create_all()