import src.constants.command as command
from src.display.display import Display
import src.utils.toast as u_toast
from src.database.books_service import BooksService
import src.constants.decorator as decorator

class Stages():
    def __init__(self, display: Display, books_service: BooksService):
        self.display = display
        self.books_service = books_service
        self.page = 1
        self.page_size = 10
        self.stage = 0
        self.is_show_list = False
        self.search = ""
        self.is_run = True
        self.is_toast = False
        self.toast = ""
        
    
    def choose(self, output):
        self.output = output
        
        self.reset_toast()
        if u_toast.is_toast(output):            
            self.toast = output
            self.output = ""
            
        if self.stage == 0:
            self._stage_home()
        elif self.stage == 1:
            self._stage_add_book()
        elif self.stage == 2:
            self._stage_filter_list_book()
        elif self.stage == 3:
            self._stage_search_input()
        elif self.stage == 4:
            self._stage_page_input()
            
    def reset_toast(self):        
        if self.toast != "":
            self.toast = ""
                
    def _stage_home(self):
        if self.output == command.S0 or self.output == command.S1:
            self.display.display_out()
        elif self.output == command.M1:
            self.is_show_list = True
        elif self.output == command.M2:
            self.is_show_list = False
        elif self.output == command.M5:
            self.stage = 1
        elif self.output == command.M6:
            self.stage = 2

    def _stage_add_book(self):
        if self.output == command.S1:
            self.stage = 0
        else:
            try:
                self.books_service.insert_book([
                    self.output.isbn,
                    self.output.judul_buku, 
                    self.output.pengarang, 
                    self.output.penerbit, 
                    self.output.kota, 
                    self.output.tahun
                ])
                self.toast = f"{decorator.toast_success}Sukses menambahkan buku"
            except Exception as error:
                return error
            self.stage = 0

    def _stage_filter_list_book(self):
        if self.output == command.S1:
            self.stage = 0
        elif self.output == command.C1:
            self.page -= 1
        elif self.output == command.C2:
            self.page += 1
        elif self.output == command.C3:
            self.stage = 3
        elif self.output == command.C4:
            self.page = 1
            self.search = ""
        elif self.output == command.C5:
            self.stage = 4

    def _stage_search_input(self):
        if self.output == command.S1:
            self.stage = 2
        else:
            self.search = self.output
            self.page = 1
            self.stage = 2

    def _stage_page_input(self):
        if self.output == command.S1:
            self.stage = 2
        else:
            if self.output == 0:
                self.page = 1
            else:
                self.page = int(self.output)
                self.stage = 2
