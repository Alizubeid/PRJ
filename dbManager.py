import psycopg2
from config import config
import queries as q

class dbManager():
    def __init__(self):
        self.connect = psycopg2.connect(**config())

    def __enter__(self):
        self.cursor = self.connect.cursor()
        [self.cursor.execute(i) for i in q.CREATE_ALL_TABLE]
        self.connect.commit()
        return self.cursor

    def __exit__(self, exc_type, exc_val, traceback):
        self.connect.commit()
        self.connect.close()
