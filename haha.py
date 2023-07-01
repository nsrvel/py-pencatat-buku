import sqlite3
import src.models.book as model_book
import src.database.books_query as query

conn = sqlite3.connect("22572004.db")
cursor = conn.cursor()

def find_by_isbn(isbn: str):
        try:
            cursor.execute(query.q_find_by_isbn, isbn)
            buku = cursor.fetchone()
            print(buku)
            return model_book.Buku(buku[0], buku[1], buku[2], buku[3], buku[4], buku[5], buku[6], buku[7], buku[8])
        except sqlite3.Error as error:
            return error
        
res = find_by_isbn("123456789")
print(res)