from datetime import datetime
import math


class Buku:
    def __init__(self, id: int, isbn: str, judul_buku: str, pengarang: str, penerbit: str, kota: str, tahun: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.isbn = isbn
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.kota = kota
        self.tahun = tahun
        self.created_at = created_at
        self.updated_at = updated_at


class CreateBukuRequest():
    def __init__(self,  isbn: str, judul_buku: str, pengarang: str, penerbit: str, kota: str, tahun: str):
        self.isbn = isbn
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.kota = kota
        self.tahun = tahun


class Pagination:
    def __init__(self, total_row: int, page: int, size: int):

        total_page = int
        if size > 0:
            total_page = math.ceil(total_row / size)
        else:
            total_page = 1

        if total_page == 0:
            total_page = 1

        has_more = bool
        if total_page-page < 1:
            has_more = False
        else:
            has_more = True

        self.total_row = total_row
        self.total_page = total_page
        self.page = page
        self.size = size
        self.has_more = has_more
