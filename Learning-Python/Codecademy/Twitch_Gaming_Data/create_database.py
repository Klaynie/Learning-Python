import os
import sqlite3
import pandas as pd
from pathlib import Path

# Create database
db_name = 'gaming_data.db'
db_path = os.path.dirname(__file__)
full_db_path = os.path.join(db_path, db_name)
if os.path.exists(full_db_path):
  os.remove(full_db_path)
Path(full_db_path).touch()
# Create database connection and cursor
conn = sqlite3.connect(full_db_path)
c = conn.cursor()
# Create chat table and load data
c.execute('''
          CREATE TABLE chat (
              time numeric,
              device_id text,
              login text,
              channel text,
              country text,
              player text,
              game text)
          ''')
chat_file_name = 'chat.csv'
chat_file_path = os.path.dirname(__file__)
full_chat_file_path = os.path.join(chat_file_path, chat_file_name)
users = pd.read_csv(full_chat_file_path)
users.to_sql('chat', conn, if_exists='append', index = False)
# Create stream table and load data
c.execute('''
          CREATE TABLE stream (
              time numeric,
              device_id text,
              login text,
              channel text,
              country text,
              player text,
              game text,
              stream_format text,
              subscriber text
              )
          ''')
stream_file_name = 'stream.csv'
stream_file_path = os.path.dirname(__file__)
full_stream_file_path = os.path.join(stream_file_path, stream_file_name)
users = pd.read_csv(full_stream_file_path)
users.to_sql('stream', conn, if_exists='append', index = False)