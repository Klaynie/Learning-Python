import sqlite3
import os
import csv
from enum import IntEnum

class Encodings(IntEnum):
    UTF8 = 0

class FileNames(IntEnum):
    DATABASE = 0
    STATE_CLIMATE = 1

class CreateQueries(IntEnum):
    STATE_CLIMATE = 0

class InsertQueries(IntEnum):
    STATE_CLIMATE = 0

encodings = [
    'utf8'
]

file_names = [
    'state_climate.db',
    'state_climate.csv'
]

create_queries = [
    'CREATE TABLE state_climate (state TEXT, year INTEGER, tempf REAL, tempc REAL);'
]

insert_queries = [
    'INSERT INTO state_climate (state, year, tempf, tempc) VALUES (?, ?, ?, ?);'
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
    create_state_climate_table(cursor)

def populate_tables(script_dir, cursor):
    populate_state_climate_table(script_dir, cursor)

def create_state_climate_table(cursor):
    cursor.execute(create_queries[CreateQueries.STATE_CLIMATE])

def populate_state_climate_table(script_dir, cursor):
    file_name = file_names[FileNames.STATE_CLIMATE]
    data = read_data_from_file(script_dir, file_name)
    query = insert_queries[InsertQueries.STATE_CLIMATE]
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