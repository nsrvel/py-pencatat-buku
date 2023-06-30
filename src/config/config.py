import os
from dotenv import load_dotenv

class Config():
    def __init__(self, path: str):
        
        load_dotenv(dotenv_path=path)
        
        self.db_name = os.getenv("DB_NAME")
        self.author_name = os.getenv("AUTHOR_NAME")