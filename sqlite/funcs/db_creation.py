import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.sql.sqltypes import Integer, REAL, TEXT
from sqlalchemy import (create_engine, MetaData, Column, Table)
from sqlalchemy_utils import database_exists, create_database

load_dotenv(find_dotenv())

engine = create_engine(f"sqlite:///{os.getenv('SQLITE_DB_NAME')}", echo=False)

if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(bind=engine)

produtos = Table('products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', TEXT(50), nullable=False),
    Column('price', REAL(8,2), nullable=False),
    Column('stock', TEXT(50), nullable=False)
)

metadata.create_all()