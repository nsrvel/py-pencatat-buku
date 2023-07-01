q_create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        no_isbn VARCHAR(15),
        judul VARCHAR(50),
        pengarang VARCHAR(30),
        penerbit VARCHAR(30),
        kota VARCHAR(25),
        tahun VARCHAR(4),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

q_insert_book = """
    INSERT INTO books (no_isbn, judul, pengarang, penerbit, kota, tahun)
    VALUES (?,?,?,?,?,?)
"""

q_select_books = """
    SELECT * FROM books
"""

q_count_books = """
    SELECT COUNT(*) FROM books
"""

q_find_by_no_isbn = """
    SELECT * FROM books WHERE no_isbn = ?
"""

q_delete_no_isbn = """
    DELETE FROM books WHERE no_isbn = ?
"""

q_update_book = """
    UPDATE books
    SET judul = ?,
        pengarang = ?,
        penerbit = ?,
        kota = ?,
        tahun = ?,
        updated_at = datetime('now')
    where no_isbn = ?
"""