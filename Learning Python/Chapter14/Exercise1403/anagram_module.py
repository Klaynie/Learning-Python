'''
Created on 04.03.2020

@author: coiz
'''
from anagram_sets import *
import dbm
import pickle
import os

def open_db_connection():
    '''Opens connection to a file database
    
    db: Database
    '''
    db = dbm.open('anagrams.db', 'c')
    return db

def store_anagrams(d):
    ''' Stores all anagrams into a file database
    
    db: Database
    d: Dictionary with anagrams
    '''
    db = open_db_connection()
    for key, value in d.items():
        db[key] = pickle.dumps(value)

def read_anagrams(word):
    db = open_db_connection()
    return pickle.loads(db[signature(word)])


if not os.path.exists('anagrams.db.dat'):
    store_anagrams(all_anagrams('words.txt'))
else:
    print(read_anagrams('stop'))