import src.display.general as d_general
import src.display.home as d_home
import src.display.table as d_table
import src.display.selection as d_select
import src.display.input as d_input
import src.models.pagination as page

class Display():
    
    def show(self, books: list, page_info: page.Pagination, is_show_list: bool, stage: int):
        
        self._display_title()
        self._display_author()
        
        if is_show_list:
            self._display_list(books, page_info)
            self.display_empty()
        if stage == 0:
            return self._display_main_select(is_show_list, len(books))
        if stage == 1:
            return self._display_tambah_input()
        if stage == 2:
            return self._display_filter_select(page_info)
        if stage == 3:
            return self._display_search_input()
        if stage == 4:
            return self._display_change_page_input()
    
    def display_empty(self): 
        d_general.display_empty()
    def display_clear(self):
        d_general.display_clear()
    def display_out(self):
        d_general.display_out()
    def _display_title(self):
        d_home.display_title()
    def _display_author(self):
        d_home.display_author()
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


























