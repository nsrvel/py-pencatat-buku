import os
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich.text import Text
import questionary as question
import src.model as model
import src.database as database
import src.command as command

console = Console()


def show(books: list, page_info: model.Pagination, is_show_list: bool, stage: int):
    display_title()
    display_author()
    if is_show_list:
        display_list(books, page_info)
        display_empty()
    if stage == 0:
        return display_main_select(is_show_list)
    if stage == 1:
        return display_tambah_select()
    if stage == 2:
        return display_filter_select(page_info)
    if stage == 3:
        return display_cari_insert_value()


def display_out():
    display_clear()
    console.print("Terimakasih")
    quit()


def display_empty():
    print()


def display_clear():
    os.system('cls||clear')


def display_title():
    title = "Pencatat Buku"
    f = Figlet(font='standard')
    ascii_text = f.renderText(title)
    console.print(ascii_text)


def display_author():
    authorText = "by: putra rama\n"
    console.print(f"[yellow]{authorText}[/yellow]")


def display_list(books: list, page_info: model.Pagination):

    table = Table(
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("#", style="dim", min_width=4, max_width=100)
    table.add_column("ISBN", min_width=10, max_width=13, justify="left")
    table.add_column("Judul", min_width=12, justify="left")
    table.add_column("Pengarang", min_width=12, justify="left")
    table.add_column("Penerbit", min_width=12, justify="left")
    table.add_column("Kota", min_width=12, justify="left")
    table.add_column("Tahun", min_width=12, justify="left")

    for book in books:
        table.add_row(
            str(book.id),
            book.isbn,
            book.judul_buku,
            book.pengarang,
            book.penerbit,
            book.kota,
            book.tahun
        )

    console.print(table)

    # Hitung estimasi panjang tabel
    length = 8
    for attr in table._calculate_column_widths(console, console.options):
        length += attr

    display_detail_list(page_info, length)
    display_empty()


def display_detail_list(page_info: model.Pagination, estimation_table_legth: int):

    data_text = f" Showing {page_info.page}-{page_info.page+page_info.size-1} from {page_info.total_row} data"
    data_text_length = len(data_text)

    page_text = f"{setcolor(page_info.page, 'magenta')} from {page_info.total_page}"
    page_text_length = len(page_text)

    color_style_text_length = 19

    empty_text = " " * (
        estimation_table_legth -
        data_text_length -
        page_text_length +
        color_style_text_length - 1
    )

    result = data_text + empty_text + page_text

    console.print(result)


def setcolor(text: str, color: str):
    return f"[{color}]{text}[/{color}]"


def question_select(options):
    try:
        selected_option = question.select(
            "Menu \n", choices=options, instruction=" ", ).ask()
        if selected_option == None:
            return command.C0
        else:
            return selected_option
    except:
        return command.C0


def display_main_select(is_show_list: bool):
    options = []
    if is_show_list:
        options.append(command.M2)
        options.append(command.M6)
    else:
        options.append(command.M1)

    options.extend([
        command.M5,
        "Update data",
        command.M0
    ])

    return question_select(options)


def display_filter_select(page_info):
    options = []

    if page_info.page - 1 != 0:
        options.append(command.C1)
    if page_info.has_more:
        options.append(command.C2)
    options.append(command.C3)
    options.append(command.C4)
    options.append(command.M4)

    return question_select(options)


def display_cari_insert_value() -> str:
    return question.text("ISBN / Judul Buku : ").ask()


def display_tambah_select():
    console.print("Silahkan isi data-data berikut")

    isbn = question.text("Nomor ISBN : ").ask()
    judul_buku = question.text("Judul Buku : ").ask()
    pengarang = question.text("Nama Pengarang : ").ask()
    penerbit = question.text("Nama Penerbit : ").ask()
    kota = question.text("Nama Kota Terbit : ").ask()
    tahun = question.text("Tahun Terbit : ").ask()

    return model.CreateBukuRequest(isbn=isbn, judul_buku=judul_buku, pengarang=pengarang, penerbit=penerbit, kota=kota, tahun=tahun)
