import sqlite3
import os

class SuperheroDB():
    
    def __init__(self):
        
        """
        initialise datastore
        """
        
        self.filename = "superhero_db.db"
        
        if not os.path.exists(self.filename):
            # if db is not present create it then connect to it
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
            self.create_superhero_db()
        else:
            # if db is present connect to it
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
        
    
    def create_superhero_db(self):
        # create publisher table
        self.cursor.execute("""
                            CREATE TABLE Publisher(
                                pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL
                            )
                            """)
        
        # create alignment table
        self.cursor.execute("""
                            CREATE TABLE alignmnet(
                                align_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL
                            )
                            """)   
        
        
        # create superhero table
        self.cursor.execute("""
                            CREATE TABLE Superhero(
                                super_hero_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                intelligence INTEGER NOT NULL,
                                strength INTEGER NOT NULL,
                                speed INTEGER NOT NULL,
                                durability INTEGER NOT NULL,
                                power INTEGER NOT NULL,
                                combat INTEGER NOT NULL,
                                image TEXT NOT NULL,
                                publisher INTEGER NOT NULL,
                                alignment INTEGER NOT NULL,
                                FOREIGN KEY(publisher) REFERENCES Publisher(pub_id),
                                FOREIGN KEY (alignment) REFERENCES Alignment(align_id)
                            )
                            """)
        
        # create alias id
        self.cursor.execute("""
                            CREATE TABLE Alias(
                                alias_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL                                
                            )
                            """)
