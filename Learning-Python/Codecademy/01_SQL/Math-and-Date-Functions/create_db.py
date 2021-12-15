import sqlite3
import os
import csv
from enum import IntEnum

class Encodings(IntEnum):
    UTF8 = 0

class FileNames(IntEnum):
    DATABASE = 0
    BAKERY = 1
    GUESSES = 2

class CreateQueries(IntEnum):
    BAKERY = 0
    GUESSES = 1

class InsertQueries(IntEnum):
    BAKERY = 0
    GUESSES = 1

encodings = [
    'utf8'
]

file_names = [
    'math-and-date.db',
    'bakery.csv',
    'guesses.csv'
]

create_queries = [
    'CREATE TABLE bakery (id INTEGER, item_name TEXT, price REAL, quantity INTEGER, discount TEXT, order_date DATETIME);',
    'CREATE TABLE guesses (id INTEGER, first_name TEXT, last_name TEXT, guess INTEGER)'
]

insert_queries = [
    'INSERT INTO bakery (id, item_name, price, quantity, discount, order_date) VALUES (?, ?, ?, ?, ?, ?);',
    'INSERT INTO guesses (id, first_name, last_name, guess) VALUES (?, ?, ?, ?);'
]

def create_database():    
    script_dir = os.path.dirname(__file__)
    database_name = file_names[FileNames.DATABASE]
    abs_file_path = os.path.join(script_dir, database_name)
    if os.path.exists(abs_file_path):
        os.remove(abs_file_path)
    
    connection = sqlite3.connect(abs_file_path)
    cursor = connection.cursor()

    create_tables(cursor)
    populate_tables(script_dir, cursor)

    cursor.close()    
    connection.commit()
    connection.close()

def create_tables(cursor):
    create_bakery_table(cursor)
    create_guesses_table(cursor)

def populate_tables(script_dir, cursor):
    populate_bakery_table(script_dir, cursor)
    populate_guesses_table(script_dir, cursor)

def create_bakery_table(cursor):
    cursor.execute(create_queries[CreateQueries.BAKERY])

def create_guesses_table(cursor):
    cursor.execute(create_queries[CreateQueries.GUESSES])

def populate_bakery_table(script_dir, cursor):
    file_name = file_names[FileNames.BAKERY]
    data = read_data_from_file(script_dir, file_name)
    query = insert_queries[InsertQueries.BAKERY]
    populate_table(cursor, query, data)

def populate_guesses_table(script_dir, cursor):
    file_name = file_names[FileNames.GUESSES]
    data = read_data_from_file(script_dir, file_name)
    query = insert_queries[InsertQueries.GUESSES]
    populate_table(cursor, query, data)

def read_data_from_file(script_dir, file_name):
    data_file_path = os.path.join(script_dir, file_name)
    result = csv.reader(open(data_file_path, encoding=encodings[Encodings.UTF8]))
    next(result) # skip header
    return result

def populate_table(cursor, query, data):
    for row in data:
        cursor.execute(query, row)

create_database()