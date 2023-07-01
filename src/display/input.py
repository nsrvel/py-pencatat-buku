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

# Menampilkan form no_isbn
def display_no_isbn_input():
    answer =  prompt.question_input("Nomor ISBN : ", ["required", "type:str"])
    if answer == None:
        return command.S1
    else:
        return answer

# Menampilkan form penambahan buku
def display_tambah_input():
    console.print("Silahkan isi data-data berikut")
    
    no_isbn = prompt.question_input("Nomor ISBN : ", ["required", "type:str", "min:8", "max:15"])
    if no_isbn == None:
        return command.S1
    
    judul = prompt.question_input("Judul Buku : ", ["required", "type:str", "max:50"])
    if judul == None:
        return command.S1
    
    pengarang = prompt.question_input("Nama Pengarang : ", ["required", "type:str", "max:30"])
    if pengarang == None:
        return command.S1
    
    penerbit = prompt.question_input("Nama Penerbit : ", ["required", "type:str", "max:30"])
    if penerbit == None:
        return command.S1
    
    kota = prompt.question_input("Nama Kota Terbit : ", ["required", "type:str", "max:25"])
    if kota == None:
        return command.S1
    
    tahun = prompt.question_input("Tahun Terbit : ", ["required", "type:str", "len:4"])
    if tahun == None:
        return command.S1
    
    return m_book.CreateBukuRequest(no_isbn=no_isbn, judul=judul, pengarang=pengarang, penerbit=penerbit, kota=kota, tahun=tahun)

# Menampilkan form edit buku
def display_edit_input(book: m_book.Buku):
    console.print("Silahkan edit data-data berikut")
    
    judul = prompt.question_input("Judul Buku : ", ["required", "type:str", "max:50"], book.judul)
    if judul == None:
        return command.S1
    
    pengarang = prompt.question_input("Nama Pengarang : ", ["required", "type:str", "max:30"], book.pengarang)
    if pengarang == None:
        return command.S1
    
    penerbit = prompt.question_input("Nama Penerbit : ", ["required", "type:str", "max:30"], book.penerbit)
    if penerbit == None:
        return command.S1
    
    kota = prompt.question_input("Nama Kota Terbit : ", ["required", "type:str", "max:25"], book.kota)
    if kota == None:
        return command.S1
    
    tahun = prompt.question_input("Tahun Terbit : ", ["required", "type:str", "len:4"], book.tahun)
    if tahun == None:
        return command.S1
    
    return m_book.UpdateBukuRequest(no_isbn=book.no_isbn, judul=judul, pengarang=pengarang, penerbit=penerbit, kota=kota, tahun=tahun)
