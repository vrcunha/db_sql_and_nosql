import os
from dotenv import load_dotenv, find_dotenv

from sqlalchemy import (create_engine, MetaData, Column, 
                        Table, Integer, String, DECIMAL
                        )
from sqlalchemy_utils import database_exists, create_database

load_dotenv(find_dotenv())

engine = create_engine(f"mysql+mysqldb://{os.getenv('MYSQL_USER_NAME')}:" \
                       f"{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/" \
                       f"{os.getenv('MYSQL_DB_NAME')}", echo=False)

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