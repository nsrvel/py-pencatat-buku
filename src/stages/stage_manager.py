import src.constants.command as command
from src.display.display import Display
from src.database.books_service import BooksService
import src.constants.decorator as decorator
import src.models.book as m_book

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
        self.target = ""
        self.pre_stage = 0
        self.pre_output = None
        self.confirm = None
    
    def choose(self):
        
        self._reset_toast()
        
        if self.stage == 6:
            self._stage_confirm()
            
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
        elif self.stage == 5:
            self._stage_delete_book()
        elif self.stage == 7:
            self._stage_update_book()
                    
                
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
        elif self.output == command.M8:
            self.stage = 5
        elif self.output == command.M7:
            self.stage = 7
            
    def _stage_confirm(self):
        self.stage = self.pre_stage
        self.confirm = self.output
        self.output = self.pre_output
        
    def _throw_toast(self, toast: str):
        if self.toast == "":
            self.toast = toast
            self.pre_output = self.output
        
    def _reset_toast(self):
        if self.toast != "":
            self.toast = ""
        
            
    def _stage_delete_book(self):
        if self.target == "":
            if self.output == command.S1:
                self.stage = 0
            else:
                if self.confirm == None:
                    try:
                        book = self.books_service.find_by_no_isbn(self.output)
                        if book == None:
                            self._throw_toast(f"{decorator.toast_err}Buku tidak ditemukan")
                        else:
                            self.is_show_list = True
                            self.pre_output = self.output
                            self.search = self.pre_output
                            self.target = book.no_isbn
                            self.pre_stage = self.stage
                            self.stage = 6
                    except Exception as error:
                        self._throw_toast(f"{decorator.toast_err}{str(error)}")
        else:
            if self.confirm == True:
                try:
                    self.books_service.delete_book(self.target)
                    self._throw_toast(f"{decorator.toast_success}Sukses menghapus data")
                except Exception as error:
                    self._throw_toast(f"{decorator.toast_err}{str(error)}")
                self.stage = 0
            else:
                self.stage = 5
                self.is_show_list = False
                
            self.target = ""
            self.page = 1
            self.search = ""
            self.confirm = None
                
    def _stage_update_book(self):
        if self.target == "":
            if self.output == command.S1:
                self.stage = 0
            else:
                try:
                    book = self.books_service.find_by_no_isbn(self.output)
                    if book == None:
                        self._throw_toast(f"{decorator.toast_err}Buku tidak ditemukan")
                    else:
                        self.is_show_list = True
                        self.pre_output = self.output
                        self.search = self.pre_output
                        self.target = book.no_isbn
                except Exception as error:
                    self._throw_toast(f"{decorator.toast_err}{str(error)}")
        else:
            if self.output == command.S1:
                self.stage = 7
                self.target = ""
                self.search = ""
                self.page = 1
                self.is_show_list = False
            else:
                if self.confirm == None:
                    self.pre_output = self.output
                    self.pre_stage = self.stage
                    self.stage = 6
                else:
                    if self.confirm == True:
                        try:
                            self.books_service.update_book([
                                self.output.judul, 
                                self.output.pengarang, 
                                self.output.penerbit, 
                                self.output.kota, 
                                self.output.tahun,
                                self.output.no_isbn
                            ])
                            self._throw_toast(f"{decorator.toast_success}Sukses mengedit data")
                        except Exception as error:
                            self._throw_toast(f"{decorator.toast_err}{str(error)}")
                    self.stage = 0
                    self.page = 1
                    self.search = ""
                    self.confirm = None
                    self.target = ""
                
    def _stage_add_book(self):
        if self.output == command.S1:
            self.stage = 0
        else:
            if self.confirm == None:
                self.pre_output = self.output
                self.pre_stage = self.stage
                self.stage = 6
            else:
                if self.confirm == True:
                    book = None
                    try:
                        book = self.books_service.find_by_no_isbn(self.output.no_isbn)
                    except Exception as error:
                        self._throw_toast(f"{decorator.toast_err}{str(error)}")
                        
                    if book != None:
                        self._throw_toast(f"{decorator.toast_err}Buku dengan ISBN tersebut sudah ada")
                    else:
                        try:
                            self.books_service.insert_book([
                                self.output.no_isbn,
                                self.output.judul, 
                                self.output.pengarang, 
                                self.output.penerbit, 
                                self.output.kota, 
                                self.output.tahun
                            ])
                            self._throw_toast(f"{decorator.toast_success}Sukses menambahkan buku")
                        except Exception as error:
                            self._throw_toast(f"{decorator.toast_err}{str(error)}")
                                
                self.stage = 0
                self.confirm = None

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
    
