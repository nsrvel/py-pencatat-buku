from src.display.display import Display
from src.config.config import Config
from src.database.db import DatabaseManager
from src.database.books_service import BooksService
from src.stages.stage_manager import Stages

def main():
    
    # get config
    cfg = Config(".env")
    # define display
    display = Display()
    # clear console
    display.display_clear()    
    # Inisialisasi database manager
    db_manager = DatabaseManager(cfg.db_name)
    # initial books service
    books_service = BooksService(db_manager)        
        
    # initial stages
    stages = Stages(display, books_service)

    while stages.is_run:
        try:
            # mancari data untuk ditampilkan
            books, page_info = books_service.get_all_book(stages.search, stages.page, stages.page_size)
            # clear console
            display.display_clear()
            # menampilkan core visual
            output = display.show(books, page_info, stages.is_show_list, stages.stage, stages.toast)
            stages.choose(output)
            
        except Exception as error:
            stages.is_run = False
            print(error)

main()
