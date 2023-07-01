from rich.console import Console
from pyfiglet import Figlet

console = Console()

# Menampilkan judul aplikasi
def display_title():
    title = "Pencatat Buku"
    f = Figlet(font='smslant')
    ascii_text = f.renderText(title)    
    console.print(f"[white]{ascii_text.rstrip()}[/white]")
    
def display_author():
    author = "putra rama"
    formatted_author = f"[yellow]{author}[/yellow]"
    
    github = "https://github.com/nsrvel/py-pencatat-buku"
    formatted_github = f"[italic white]{github}[italic white]"
    console.print(f"\nby: {formatted_author} | {formatted_github}\n")