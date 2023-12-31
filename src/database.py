from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

conn_string = os.getenv("DB_CONNECTION_STRING", "postgresql://postgres:postgres@localhost:5432/rinha")
SQLALCHEMY_DATABASE_URL = conn_string

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
