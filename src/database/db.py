import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('HOST'),
            user=config('USER'),
            password=config('PASS'),
            database=config('DATABASE')
        )

    except DatabaseError as ex:
        raise ex

