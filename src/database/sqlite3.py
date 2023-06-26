import sqlite3

def connect_sqlite3(addr):
    try:
        conn = sqlite3.connect(addr)