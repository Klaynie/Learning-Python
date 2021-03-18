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
def create_database():    
    script_dir = os.path.dirname(__file__)
    database_name = 'original.db'
    abs_file_path = os.path.join(script_dir, database_name)
    if os.path.exists(abs_file_path):
        os.remove(abs_file_path)
    connection = sqlite3.connect(abs_file_path)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE Pressure (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reading REAL NOT NULL)''')
    random_numbers = uniform(low=10.0, high=25.0, size=100000)
    query = "INSERT INTO Pressure (reading) VALUES (?);"
    for number in random_numbers:
        cursor.execute(query, [number])
        
    cursor.close()    
    connection.commit()
    connection.close()


@measure
def create_file():    
    script_dir = os.path.dirname(__file__)
    file_name = 'original.txt'
    abs_file_path = os.path.join(script_dir, file_name)
    random_numbers = uniform(low=10.0, high=25.0, size=100000)
    if os.path.exists(abs_file_path):
        os.remove(abs_file_path)
    with open(abs_file_path, 'w') as f:
        for number in random_numbers:
            f.write(f"{number}\n")

create_file()            
create_database()