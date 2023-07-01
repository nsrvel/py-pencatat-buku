import questionary as question
from rich.console import Console
import src.constants.command as command
import src.utils.prompt as prompt
import src.models.book as m_book

console = Console()

# Menampilkan form search
def display_search_input():
    answer =  prompt.question_input("ISBN / Judul Buku : ", ["required", "type:str"])
    if answer == None:
        return command.S1
    else:
        return answer

# Menampilkan form page
def display_change_page_input():
    answer =  prompt.question_input("Page : ", ["required", "type:int"])
    if answer == None:
        return command.S1
    else:
        return answer

# Menampilkan form penambahan buku
def display_tambah_input():
    console.print("Silahkan isi data-data berikut")
    
    isbn = prompt.question_input("Nomor ISBN : ", ["required", "type:str"])
    if isbn == None:
        return command.S1
    
    judul_buku = prompt.question_input("Judul Buku : ", ["required", "type:str"])
    if judul_buku == None:
        return command.S1
    
    pengarang = prompt.question_input("Nama Pengarang : ", ["required", "type:str"])
    if pengarang == None:
        return command.S1
    
    penerbit = prompt.question_input("Nama Penerbit : ", ["required", "type:str"])
    if penerbit == None:
        return command.S1
    
    kota = prompt.question_input("Nama Kota Terbit : ", ["required", "type:str"])
    if kota == None:
        return command.S1
    
    tahun = prompt.question_input("Tahun Terbit : ", ["required", "type:str"])
    if tahun == None:
        return command.S1
    
    return m_book.CreateBukuRequest(isbn=isbn, judul_buku=judul_buku, pengarang=pengarang, penerbit=penerbit, kota=kota, tahun=tahun)
