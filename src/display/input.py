import questionary as question
from rich.console import Console
import src.models.book as model_book
import src.constants.command as command

console = Console()

# Menampilkan form search
def display_search_input() -> str:
    answer = question.text("ISBN / Judul Buku : ").ask()
    if answer == None:
        return command.S1
    else:
        return answer

# Menampilkan form page
def display_change_page_input() -> int:
    answer =  question.text("Page : ").ask()
    if answer == None:
        return command.S1
    else:
        return answer

# Menampilkan form penambahan buku
def display_tambah_input():
    console.print("Silahkan isi data-data berikut")
    
    isbn = question.text("Nomor ISBN : ").ask()
    if isbn == None:
        return command.S1
    
    judul_buku = question.text("Judul Buku : ").ask()
    pengarang = question.text("Nama Pengarang : ").ask()
    penerbit = question.text("Nama Penerbit : ").ask()
    kota = question.text("Nama Kota Terbit : ").ask()
    tahun = question.text("Tahun Terbit : ").ask()
    
    # return model_book.CreateBukuRequest(isbn=isbn, judul_buku=judul_buku, pengarang=pengarang, penerbit=penerbit, kota=kota, tahun=tahun)
