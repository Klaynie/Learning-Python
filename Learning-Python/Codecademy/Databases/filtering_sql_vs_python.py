from functools import wraps
from time import process_time
from numpy.random import uniform
import sqlite3
import os

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(process_time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(process_time() * 1000)) - start
            print(
                f"Total execution time {func.__name__}: {end_ if end_ > 0 else 0} ms"
            )

    return _time_it

@measure
def filter_sql():    
    script_dir = os.path.dirname(__file__)
    database_name = 'original.db'
    original_file_path = os.path.join(script_dir, database_name)
    connection_original = sqlite3.connect(original_file_path)
    cursor = connection_original.cursor()
    query = "SELECT * FROM Pressure WHERE reading >= 20.0;"
    result_set = cursor.execute(query).fetchall()
    cursor.close()
    connection_original.close()
    backup_database_name = 'backup.db'
    backup_file_path = os.path.join(script_dir, backup_database_name)
    if os.path.exists(backup_file_path):
        os.remove(backup_file_path)
    connection_new = sqlite3.connect(backup_file_path)
    cursor_new = connection_new.cursor()
    cursor_new.execute('''CREATE TABLE Pressure (
                    id INTEGER PRIMARY KEY,
                    reading REAL NOT NULL)''')
    cursor_new.executemany('''INSERT INTO Pressure VALUES (?,?)''', result_set)   
    connection_new.commit()
    connection_new.close()

@measure
def filter_python():
    script_dir = os.path.dirname(__file__)
    database_name = 'original.db'
    original_file_path = os.path.join(script_dir, database_name)
    connection_original = sqlite3.connect(original_file_path)
    cursor = connection_original.cursor()
    query = "SELECT * FROM Pressure;"
    all_results = cursor.execute(query).fetchall()
    result_set =[]
    for entry in all_results:
        if entry[1] >= 20.0:
            result_set.append(entry)
    cursor.close()
    connection_original.close()
    backup_database_name = 'backup2.db'
    backup_file_path = os.path.join(script_dir, backup_database_name)
    if os.path.exists(backup_file_path):
        os.remove(backup_file_path)
    connection_new = sqlite3.connect(backup_file_path)
    cursor_new = connection_new.cursor()
    cursor_new.execute('''CREATE TABLE Pressure (
                    id INTEGER PRIMARY KEY,
                    reading REAL NOT NULL)''')
    cursor_new.executemany('''INSERT INTO Pressure VALUES (?,?)''', result_set)   
    connection_new.commit()
    connection_new.close()

filter_sql()
filter_python()