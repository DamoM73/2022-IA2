import sqlite3
import os
import csv

class Database():
    def __init__(self,db):
        
        if os.path.exists(db):
            self.conn = sqlite3.connect(db)
            self.cur = self.conn.cursor()
            print("DB present")
        else:
            self.conn = sqlite3.connect(db)
            self.cur = self.conn.cursor()
            self.build_db()
            print("DB built")


    def __del__(self):
        self.cur.close()


    def build_db(self):
        self.cur.execute(
            """
            CREATE TABLE "publisher" (
        	"pub_id"	INTEGER NOT NULL,
	        "publisher"	TEXT NOT NULL UNIQUE,
	        PRIMARY KEY("pub_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "alignment" (
	        "align_id"	INTEGER NOT NULL UNIQUE,
	        "alignment"	TEXT NOT NULL UNIQUE,
	        PRIMARY KEY("align_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "group" (
	        "group_id"	INTEGER NOT NULL UNIQUE,
	        "group_name"	TEXT NOT NULL,
	        PRIMARY KEY("group_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "alias" (
	        "alias_id"	INTEGER NOT NULL UNIQUE,
	        "alias"	TEXT NOT NULL,
	        PRIMARY KEY("alias_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "alter_ego" (
	        "alt_id"	INTEGER NOT NULL UNIQUE,
	        "alter-ego"	TEXT NOT NULL,
	        PRIMARY KEY("alt_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "hero" (
	        "hero_id"	INTEGER NOT NULL UNIQUE,
	        "name"	TEXT NOT NULL,
	        "full_name"	TEXT,
	        "intelligence"	INTEGER,
	        "strength"	INTEGER,
	        "speed"	INTEGER,
	        "durability"	INTEGER,
	        "power"	INTEGER,
	        "combat"	INTEGER,
	        "align_id"	INTEGER NOT NULL,
	        "pub_id"	INTEGER NOT NULL,
	        "image"	TEXT  NOT NULL,
	        FOREIGN KEY("pub_id") REFERENCES "publisher"("pub_id"),
	        FOREIGN KEY("align_id") REFERENCES "alignment"("align_id"),
	        PRIMARY KEY("hero_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "hero_alias" (
	        "hero_id"	INTEGER NOT NULL,
	        "alias_id"	INTEGER NOT NULL,
	        FOREIGN KEY("hero_id") REFERENCES "hero"("hero_id"),
	        FOREIGN KEY("alias_id") REFERENCES "alias"("alias_id"),
	        PRIMARY KEY("hero_id","alias_id")
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "hero_alt" (
	        "hero_id"	INTEGER NOT NULL,
	        "alt_id"	INTEGER NOT NULL,
	        PRIMARY KEY("hero_id","alt_id"),
	        FOREIGN KEY("hero_id") REFERENCES "hero"("hero_id"),
	        FOREIGN KEY("alt_id") REFERENCES "alter_ego"("alt_id")
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "hero_group" (
	        "hero_id"	INTEGER NOT NULL,
	        "group_id"	INTEGER NOT NULL,
	        PRIMARY KEY("hero_id","group_id"),
            FOREIGN KEY("hero_id") REFERENCES "hero"("hero_id"),
	        FOREIGN KEY("group_id") REFERENCES "group"("group_id")
            );
            """
            )


    def insert_alias(self,alias):
        try:
            self.cur.execute(
                """
                INSERT INTO alias
                VALUES (NULL, :alias)
                """,
                {
                    'alias' : alias
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {alias} into alias")


    def insert_alignment(self,alignment):
        try:
            self.cur.execute(
                """
                INSERT INTO alignment
                VALUES (NULL, :alignment)
                """,
                {
                    'alignment' : alignment
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {alignment} into alignment")


    def insert_alter_ego(self,alter_ego):
        try:
            self.cur.execute(
                """
                INSERT INTO alter_ego
                VALUES (NULL, :alter_ego)
                """,
                {
                    'alter_ego' : alter_ego
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {alter_ego} into alter_ego")


    def insert_group(self,group):
        try:
            self.cur.execute(
                """
                INSERT INTO group
                VALUES (NULL, :group)
                """,
                {
                    'group' : group
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {group} into group")


    def insert_alter_ego(self,alter_ego):
        try:
            self.cur.execute(
                """
                INSERT INTO alter_ego
                VALUES (NULL, :alter_ego)
                """,
                {
                    'alter_ego' : alter_ego
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {alter_ego} into alter_ego")


    def insert_hero(self,name,full_name,intel,strg,speed,durability,power,combat,align_id,pub_id,image):
        try:
            self.cur.execute(
                """
                INSERT INTO hero
                VALUES (NULL, :name, :full_name, :intel, :strg, :speed, :durability, :power, :combat, :align_id, :pub_id, :image)
                """,
                {
                    'name' : name,
                    'full_name' : full_name,
                    'intel' : intel,
                    'strg' : strg,
                    'speed' : speed,
                    'durability' : durability,
                    'power' : power,
                    'combat' : combat,
                    'align_id' : align_id,
                    'pub_id' : pub_id,
                    'image' : image
                }
                )
            self.conn.commit()
        except:
            print("Cannot insert data into hero")

    
    def insert_hero_alias(self,hero_id, alias_id):
        try:
            self.cur.execute(
                """
                INSERT INTO hero_alias
                VALUES (NULL, :hero_id, :alias_id)
                """,
                {
                    'hero_id' : hero_id,
                    'alias_id': alias_id
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {hero_id} or {alias_id} into hero_alias")


    def insert_hero_alt(self,hero_id, alt_id):
        try:
            self.cur.execute(
                """
                INSERT INTO hero_alt
                VALUES (NULL, :hero_id, :alt_id)
                """,
                {
                    'hero_id' : hero_id,
                    'alt_id': alt_id
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {hero_id} or {alt_id} into hero_alt")

    
    def insert_hero_group(self,hero_id, group_id):
        try:
            self.cur.execute(
                """
                INSERT INTO hero_group
                VALUES (NULL, :hero_id, :group_id)
                """,
                {
                    'hero_id' : hero_id,
                    'alt_id': group_id
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {hero_id} or {group_id} into hero_group")

    
    def insert_publisher(self,publisher):
        try:
            self.cur.execute(
                """
                INSERT INTO publisher
                VALUES (NULL, :publisher)
                """,
                {
                    'publisher' : publisher
                }
                )
            self.conn.commit()
        except:
            print(f"Cannot insert {publisher} into publisher")

    
    def import_data(self,csv_file):
        with open(csv_file,'r') as data:
            reader = csv.reader(data)
            records = 0
            for row in reader:
                if records != 0:
                    print(row[7])
                records += 1