from sqlalchemy import select, update, delete, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class ConnectionHandler:
    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}/{}".format(
            'postgresql+psycopg',
            'postgres',
            '123456',
            'localhost',
            'db_clientes', )

        self.__engine = self.__create_db_engine()
        self.session = None

    def __create_db_engine(self):
        engine = create_engine(self.__connection_string, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
