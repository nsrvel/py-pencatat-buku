from datetime import datetime

# Entity Book
class Buku:
    def __init__(self, id: int, no_isbn: str, judul: str, pengarang: str, penerbit: str, kota: str, tahun: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.no_isbn = no_isbn
        self.judul = judul
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.kota = kota
        self.tahun = tahun
        self.created_at = created_at
        self.updated_at = updated_at

# Model untuk payload create book
class CreateBukuRequest():
    def __init__(self,  no_isbn: str, judul: str, pengarang: str, penerbit: str, kota: str, tahun: str):
        self.no_isbn = no_isbn
        self.judul = judul
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.kota = kota
        self.tahun = tahun
        
class UpdateBukuRequest():
    def __init__(self,  no_isbn: str, judul: str, pengarang: str, penerbit: str, kota: str, tahun: str):
        self.no_isbn = no_isbn
        self.judul = judul
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.kota = kota
        self.tahun = tahun

