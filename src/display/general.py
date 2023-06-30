import os
from rich.console import Console

console = Console()

# Tampilan saat exit program
def display_out():
    display_clear()
    console.print("Terimakasih")
    quit()

# Menampilkan text kosong
def display_empty():
    print()

# Membersihkan console
def display_clear():
    os.system('cls||clear')