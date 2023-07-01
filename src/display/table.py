from rich.table import Table
from rich.console import Console
import src.models.pagination as page
import src.display.general as d_general

console = Console()

# Menampilkan tampilan tabel untuk list buku
def display_list(books: list, page_info: page.Pagination):

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
    
    counter = 1

    for book in books:
        table.add_row(
            str(counter),
            book.isbn,
            book.judul_buku,
            book.pengarang,
            book.penerbit,
            book.kota,
            book.tahun
        )
        counter += 1

    console.print(table)

    # Hitung estimasi panjang tabel
    length = 8
    for attr in table._calculate_column_widths(console, console.options):
        length += attr

    _display_detail_list(page_info, length)
    d_general.display_empty()


# Menampilkan detail informasi terkait pagination
def _display_detail_list(page_info: page.Pagination, estimation_table_legth: int):

    data_text = f" Showing {page_info.page}-{page_info.page+page_info.size-1} from {page_info.total_row} data"
    data_text_length = len(data_text)

    page_text = f"{_setcolor(page_info.page, 'magenta')} from {page_info.total_page}"
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

def _setcolor(text: str, color: str):
    return f"[{color}]{text}[/{color}]"
