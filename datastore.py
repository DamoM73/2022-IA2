from ctypes import alignment
import sqlite3
import os
import csv

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
            self.populate_superhero_db()
        else:
            # if db is present connect to it
            self.conn = sqlite3.connect(self.filename)
            self.cursor = self.conn.cursor()
        
    
    def create_superhero_db(self):
        """
        Creates the data structure for the superhero database
        """
        # create publisher table
        self.cursor.execute("""
                            CREATE TABLE Publisher(
                                pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL
                            )
                            """)
        
        # create alignment table
        self.cursor.execute("""
                            CREATE TABLE Alignment(
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
                                name TEXT NOT NULL, 
                                superhero INTEGER,
                                FOREIGN KEY(superhero) REFERENCES Superhero(superhero_id)                                
                            )
                            """)


    def populate_superhero_db(self):
        """
        Loads values from superhero.csv into superhero database
        """
        with open("superhero.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for index, hero in enumerate(csv_reader):
                # read the values for a single hero 
                if index > 0:
                    name = hero[0]
                    intel = hero[1]
                    strgth = hero[2]
                    speed = hero[3]
                    dura = hero[4]
                    power = hero[5]
                    combat = hero[6]
                    aliases = hero[9]
                    pub = hero[12]
                    align = hero[13]
                    
                    # add new published to database
                    if self.get_publisher_id(pub) == []:
                        self.add_publisher(pub)
                    
                    # add new alignment to database
                    if self.get_alignment_id(align) == []:
                        self.add_alignment(align)
                        
                    # get foriegn keys for superhero table
                    pub_id = self.get_publisher_id(pub)
                    align_id = self.get_alignment_id(align)
                    
                    # add superhero to Superhero table
                    self.add_superhero((name,
                                        intel,
                                        strgth,
                                        speed,
                                        dura,
                                        power,
                                        combat,
                                        aliases,
                                        pub_id,
                                        align_id))
                    
                    
                    
                    
    # ----- queries ----- #                
                    
    def get_publisher_id(self,pub_name):
        """"
        Returns the publisher id for given publisher 
        """
        self.cursor.execute("""
                            SELECT pub_id
                            FROM Publisher
                            WHERE name = :name
                            """,
                            {"name":pub_name}
                            )
        results = self.cursor.fetchall()
        return results
    
    def get_alignment_id(self,align_name):
        """"
        Returns the publisher id for given publisher 
        """
        self.cursor.execute("""
                            SELECT align_id
                            FROM Alignment
                            WHERE name = :name
                            """,
                            {"name":align_name}
                            )
        results = self.cursor.fetchall()
        return results
    
    # ----- inserts ----- #
    
    def add_publisher(self,pub_name):
        """
        Adds provided publisher to the publisher table
        """
        insert_with_param = """INSERT INTO Publisher (name)
                            VALUES (?);"""
        data_tuple = (pub_name)
        
        self.cursor.execute(insert_with_param,[data_tuple])
        self.conn.commit()

        
    def add_alignment(self,align_name):
        """
        Adds provided publisher to the publisher table
        """
        insert_with_param = """INSERT INTO Alignment (name)
                            VALUES (?);"""
        data_tuple = (align_name)
        
        self.cursor.execute(insert_with_param,[data_tuple])
        self.conn.commit()
        
    def add_superhero(self,vals):
        """
        Adds provided publisher to the publisher table
        """
        insert_with_param = """INSERT INTO Superhero (
                                name,
                                intelligence,
                                strength,
                                speed,
                                durability,
                                power,
                                combat,
                                image,
                                publisher,
                                alignment,
                                )
                            VALUES (?,?,?,?,?,?,?,?,?,?);"""
        data_tuple = (vals)
        
        self.cursor.execute(insert_with_param,[data_tuple])
        self.conn.commit()
        