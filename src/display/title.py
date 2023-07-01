from rich.console import Console
from pyfiglet import Figlet

console = Console()

# Menampilkan judul aplikasi
def display_title():
    title = "Pencatat Buku"
    f = Figlet(font='standard')
    ascii_text = f.renderText(title)
    
    author = "by: putra rama"
    formatted_author = f"\n\n [yellow]{author}[/yellow]\n"
    
    console.print(ascii_text.rstrip() + formatted_author)