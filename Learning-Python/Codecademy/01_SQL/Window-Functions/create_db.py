import sqlite3
import os
import csv
from numpy.random import uniform

def create_database():    
    script_dir = os.path.dirname(__file__)
    database_name = 'original.db'
    abs_file_path = os.path.join(script_dir, database_name)
    if os.path.exists(abs_file_path):
        os.remove(abs_file_path)
    connection = sqlite3.connect(abs_file_path)
    cursor = connection.cursor()

    create_social_media_table(cursor)
    populate_social_media_table(script_dir, cursor)
    
    create_streams_table(cursor)
    populate_streams_table(script_dir, cursor)

    cursor.close()    
    connection.commit()
    connection.close()

def create_social_media_table(cursor):
    cursor.execute('''CREATE TABLE social_media (
                    username TEXT,
                    month INTEGER,
                    change_in_followers REAL,
                    change_in_following INTEGER,
                    posts INTEGER
                    )''')

def create_streams_table(cursor):
    cursor.execute('''CREATE TABLE streams (
                    artist TEXT,
                    week INTEGER,
                    streams_millions REAL,
                    chart_position INTEGER
                    )''')

def populate_social_media_table(script_dir, cursor):
    file_name = 'social_media.csv'
    data = read_data(script_dir, file_name)
    query = "INSERT INTO social_media (username, month, change_in_followers, change_in_following, posts) VALUES (?, ?, ?, ?, ?);"
    populate_table(cursor, query, data)

def populate_streams_table(script_dir, cursor):
    file_name = 'streams.csv'
    data = read_data(script_dir, file_name)
    query = "INSERT INTO streams (artist, week, streams_millions, chart_position) VALUES (?, ?, ?, ?);"
    populate_table(cursor, query, data)

def populate_table(cursor, query, data):
    for row in data:
        cursor.execute(query, row)

def read_data(script_dir, file_name):
    data_file_path = os.path.join(script_dir, file_name)
    result = csv.reader(open(data_file_path, encoding='utf8'))
    next(result) # skip header
    return result

create_database()