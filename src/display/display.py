import src.display.general as d_general
import src.display.title as d_title
import src.display.table as d_table
import src.display.selection as d_select
import src.display.input as d_input
import src.display.toast as d_toast
import src.models.pagination as page

class Display():
    
    def show(self, books: list, page_info: page.Pagination, is_show_list: bool, stage: int, toast: str):
        
        self._display_title()
        
        if is_show_list:
            self._display_list(books, page_info)
            self.display_empty()
            
        if toast != "":
            self._display_toast(toast)
        else:
            if stage == 0:
                try:
                    return self._display_main_select(is_show_list, len(books))
                except Exception as error:
                    return str(error)
                
            if stage == 1:
                try:
                    return self._display_tambah_input()
                except Exception as error:
                    return str(error)
            if stage == 2:
                try:
                    return self._display_filter_select(page_info)
                except Exception as error:
                    return str(error)
            if stage == 3:
                try:
                    return self._display_search_input()
                except Exception as error:
                    return str(error)
            if stage == 4:
                try:
                    return self._display_change_page_input()
                except Exception as error:
                    return str(error)
    
    def display_empty(self): 
        d_general.display_empty()
    def display_clear(self):
        d_general.display_clear()
    def display_out(self):
        d_general.display_out()
    def _display_title(self):
        d_title.display_title()
    def _display_toast(self, toast_message: str):
        d_toast.display_toast(toast_message)
    def _display_list(self, books: list, page_info: page.Pagination):
        d_table.display_list(books, page_info)
    def _display_main_select(self, is_show_list: bool, books_length: int):
        return d_select.display_main_select(is_show_list, books_length)
    def _display_filter_select(self, page_info):
        return d_select.display_filter_select(page_info)
    def _display_search_input(self):
        return d_input.display_search_input()
    def _display_change_page_input(self):
        return d_input.display_change_page_input()
    def _display_tambah_input(self):
        return d_input.display_tambah_input()


























