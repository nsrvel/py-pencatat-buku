import sqlite3
import sys
import os  

class DatabaseManager:
    def __init__(self, db_name):
        db_path = db_name+".db"
        
        if "--reset" in sys.argv:
            if os.path.exists(db_path):
                os.remove(db_path)
                
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
    
    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
