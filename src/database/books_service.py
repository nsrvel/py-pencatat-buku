import sqlite3
import src.database.db as db
import src.database.books_query as query
import src.models.book as model_book
import src.models.pagination as model_page
from src.database.initial_data import books_list
import sys

class BooksService:
    def __init__(self, db_manager: db.DatabaseManager):
        self.db_manager = db_manager
        self.create_table()
        if "--init" in sys.argv:
            self.add_initial_data()
        
    # function untuk memebuat tabel buku
    def create_table(self):
        try:
            self.db_manager.cursor.execute(query.q_create_books_table)
        except sqlite3.Error as error:
            return error
        
    # function untuk mengisi data awal
    def add_initial_data(self):
        try: 
            for book in books_list:
                self.insert_book(book)
        except sqlite3.Error as error:
            return error

    # function untuk membuat data buku baru
    def insert_book(self, params: list):
        try:
            self.db_manager.cursor.execute(query.q_insert_book, params)
        except sqlite3.Error as error:
            return error
    
    # function untuk mendapatkan list buku dan informasi pagenya
    def get_all_book(self, search: str, page: int, size: int):

        # define limit & offset
        limit = size
        offset = (page-1)*size
        
        # define base query
        q_select = query.q_select_books
        q_count = query.q_count_books

        # Set Filter
        q_filter = ""
        if search != "":
            q_filter += f" WHERE UPPER(isbn) LIKE UPPER(?) OR UPPER(judul_buku) LIKE UPPER(?)"

        # Mencari total data sebenarnya
        q_count += q_filter
        if search != "":
            try:
                self.db_manager.cursor.execute(q_count, (f"%{search}%", f"%{search}%"))
            except sqlite3.Error as error:
                return error
        else:
            try:
                self.db_manager.cursor.execute(q_count)
            except sqlite3.Error as error:
                return error
        total = self.db_manager.cursor.fetchone()[0]
        
        # Mencati data
        q_select += q_filter
        q_select += f" LIMIT {limit} OFFSET {offset}"
        if search != "":
            try:
                self.db_manager.cursor.execute(q_select, (f"%{search}%", f"%{search}%"))
            except sqlite3.Error as error:
                return error
        else:
            try:
                self.db_manager.cursor.execute(q_select)
            except sqlite3.Error as error:
                return error
        data = self.db_manager.cursor.fetchall()

        # Get data
        result_list = []
        for row in data:
            instance = model_book.Buku(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            result_list.append(instance)

        return result_list, model_page.Pagination(total, page, size)