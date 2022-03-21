import sqlite3
import os

class SuperheroDB():
    
    def __init__(self):
        
        """
        initialise datastore
        """
        
        self.filename = "superhero_db.db"
        
        if not os.path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
            self.create_superhero_db()
        else:
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
        
    
    def create_superhero_db(self):
        self.cursor.execute("""
                            CREATE TABLE Superhero(
                                super_hero_id INTEGER 
                            )
                            """)
