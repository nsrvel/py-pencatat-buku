import sqlite3
from pyfiglet import Figlet
import src.model as model

conn = sqlite3.connect("22572004.db")
c = conn.cursor()


def create_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn text,
            judul_buku text,
            pengarang text,
            penerbit text,
            kota text,
            tahun text,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )          
    """)


def insert_book(params: list):
    try:
        c.execute("""
            INSERT INTO books (isbn, judul_buku, pengarang, penerbit, kota, tahun)
            VALUES(?,?,?,?,?,?)          
        """, params)
        conn.commit()
    except sqlite3.Error as e:
        return f"Error occured: {e}"


def get_all_book(search: str, page: int, size: int):
    try:

        limit = size
        offset = (page-1)*size

        query = """
            SELECT * FROM books
        """
        count_query = """
            SELECT COUNT(*) FROM books
        """

        query_filter = ""
        if search != "":
            # UPPER(column_name) LIKE UPPER(?)
            query_filter += f" WHERE UPPER(isbn) LIKE UPPER(?) OR UPPER(judul_buku) LIKE UPPER(?)"

        # Mencari total data sebenarnya
        count_query += query_filter
        c.execute
        if search != "":
            c.execute(count_query, (f"%{search}%", f"%{search}%"))
        else:
            c.execute(count_query)
        total = c.fetchone()[0]

        # Mencati data
        query += query_filter
        query += f" LIMIT {limit} OFFSET {offset}"

        if search != "":
            c.execute(query, (f"%{search}%", f"%{search}%"))
        else:
            c.execute(query)

        result_list = []
        for row in c.fetchall():
            instance = model.Buku(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            result_list.append(instance)

        return result_list, model.Pagination(total, page, size)

    except sqlite3.Error as e:
        print(e)
        return f"Error occured: {e}"
