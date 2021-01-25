import os
import csv

script_dir = os.path.dirname(__file__)
file_name = 'books.csv'
abs_file_path = os.path.join(script_dir, file_name)

with open(abs_file_path, newline='') as books_csv:
    isbn_list = []
    books_reader = csv.DictReader(books_csv, delimiter='@')
    for row in books_reader:
        isbn_list.append(row['ISBN'])

print(isbn_list)