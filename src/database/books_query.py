q_create_books_table = """
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
"""

q_insert_book = """
    INSERT INTO books (isbn, judul_buku, pengarang, penerbit, kota, tahun)
    VALUES (?,?,?,?,?,?)
"""

q_select_books = """
    SELECT * FROM books
"""

q_count_books = """
    SELECT COUNT(*) FROM books
"""

q_find_by_isbn = """
    SELECT * FROM books WHERE isbn = ?
"""

q_delete_isbn = """
    DELETE FROM books WHERE isbn = ?
"""

q_update_book = """
    UPDATE books
    SET judul_buku = ?,
        pengarang = ?,
        penerbit = ?,
        kota = ?,
        tahun = ?,
        updated_at = datetime('now')
    where isbn = ?
"""