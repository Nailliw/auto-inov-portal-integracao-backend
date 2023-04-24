import os
from abc import ABC


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

os.environ["AWS_REGION"] = "us-east-1"


def create_postgres_engine():

    credentials = {
        "host": "localhost:5432",
        "user": "root",
        "password": "root",
        "database": "test_db",
    }

    host = credentials["host"]
    user = credentials["user"]
    password = credentials["password"]

    database_name = credentials["database"]
    conn = f'{user}:{password}@{host}/{database_name}'
    print(conn)

    return create_engine(f'postgresql+psycopg2://{conn}')


class AbstractRepository(ABC):
    def __init__(self):
        self.session = sessionmaker(create_postgres_engine())()

    def get_all(self, model):
        return self.session.query(model).all()
