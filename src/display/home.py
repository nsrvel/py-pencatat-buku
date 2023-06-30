from rich.console import Console
from pyfiglet import Figlet

console = Console()

# Menampilkan judul aplikasi
def display_title():
    title = "Pencatat Buku"
    f = Figlet(font='standard')
    ascii_text = f.renderText(title)
    console.print(ascii_text)

# Menampilkan author
def display_author():
    authorText = "by: putra rama\n"
    console.print(f"[yellow]{authorText}[/yellow]")