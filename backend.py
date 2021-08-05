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
            CREATE TABLE "Publishers" (
        	"pub_id"	INTEGER NOT NULL,
	        "publisher"	TEXT NOT NULL UNIQUE,
	        PRIMARY KEY("pub_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Alignments" (
	        "align_id"	INTEGER NOT NULL UNIQUE,
	        "alignment"	TEXT NOT NULL UNIQUE,
	        PRIMARY KEY("align_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Groups" (
	        "group_id"	INTEGER NOT NULL UNIQUE,
	        "group_name"	TEXT NOT NULL,
	        PRIMARY KEY("group_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Aliases" (
	        "alias_id"	INTEGER NOT NULL UNIQUE,
	        "alias"	TEXT NOT NULL,
	        PRIMARY KEY("alias_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Alter_egos" (
	        "alt_id"	INTEGER NOT NULL UNIQUE,
	        "alter_ego"	TEXT NOT NULL,
	        PRIMARY KEY("alt_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Heroes" (
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
	        "pub_id"	INTEGER,
	        "image"	TEXT  NOT NULL,
	        FOREIGN KEY("pub_id") REFERENCES "publisher"("pub_id"),
	        FOREIGN KEY("align_id") REFERENCES "alignment"("align_id"),
	        PRIMARY KEY("hero_id" AUTOINCREMENT)
            );
            """
            )

        self.cur.execute(
            """
            CREATE TABLE "Hero_alias" (
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
            CREATE TABLE "Hero_alt" (
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
            CREATE TABLE "Hero_group" (
	        "hero_id"	INTEGER NOT NULL,
	        "group_id"	INTEGER NOT NULL,
	        PRIMARY KEY("hero_id","group_id"),
            FOREIGN KEY("hero_id") REFERENCES "hero"("hero_id"),
	        FOREIGN KEY("group_id") REFERENCES "group"("group_id")
            );
            """
            )


    def insert_alias(self,values):
        for value in values:
            clean_val = value.strip()
            if self.check_alias(clean_val) == []:
                try:
                    self.cur.execute(
                        """
                        INSERT INTO Aliases
                        VALUES (NULL, :alias)
                        """,
                        {
                            'alias' : clean_val
                        }
                        )
                    self.conn.commit()
                except:
                    print(f"Cannot insert {clean_val} into alias")


    def insert_alignment(self,value):
        if self.check_alignment(value) == []:
            try:
                self.cur.execute(
                    """
                    INSERT INTO Alignments
                    VALUES (NULL, :alignment)
                    """,
                    {
                        'alignment' : value
                    }
                    )
                self.conn.commit()
            except:
                print(f"Cannot insert {value} into alignment")


    def insert_alter_ego(self,values):
        for value in values:
            clean_val = value.strip()
            if self.check_alts(clean_val) == []:
                try:
                    self.cur.execute(
                        """
                        INSERT INTO Alter_egos
                        VALUES (NULL, :alter_ego)
                        """,
                        {
                            'alter_ego' : clean_val
                        }
                        )
                    self.conn.commit()
                except:
                    print(f"Cannot insert {clean_val} into alter_ego")


    def insert_group(self,values):
        for value in values:
            clean_val = value.strip()
            if self.check_group(clean_val) == []:
                try:
                    self.cur.execute(
                        """
                        INSERT INTO Groups
                        VALUES (NULL, :group)
                        """,
                        {
                            'group' : clean_val
                        }
                        )
                    self.conn.commit()
                except:
                    print(f"Cannot insert {clean_val} into group")


    def insert_hero(self,name,full_name,intel,strg,speed,durability,power,combat,align,pub,image):
        align_id = self.check_alignment(align)[0][0]
        if pub == "":
            pub_id = None
        else:
            pub_id = self.check_publisher(pub)[0][0]

        try:
            self.cur.execute(
                """
                INSERT INTO Heroes
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
        except Exception as e:
            print("insert hero:",e)

    
    def insert_hero_alias(self,hero_id, alias_id):
        try:
            self.cur.execute(
                """
                INSERT INTO Hero_alias
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
                INSERT INTO Hero_alt
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
                INSERT INTO Hero_group
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

    
    def insert_publisher(self,value):
        if self.check_publisher(value) == [] and value !="":
            try:
                self.cur.execute(
                    """
                    INSERT INTO Publishers
                    VALUES (NULL, :publisher)
                    """,
                    {
                        'publisher' : value
                    }
                    )
                self.conn.commit()
            except:
                print(f"Cannot insert {value} into publisher")

    def check_alias(self,value):
        try:
            self.cur.execute(
                """
                SELECT alias_id
                FROM Aliases
                WHERE alias = :ali
                """,
            {
                'ali' : value
            }
            )
            return self.cur.fetchall()
        except:
            print("Error checking alignments")
            return False


    def check_alignment(self,value):
        try:
            self.cur.execute(
                """
                SELECT align_id
                FROM Alignments
                WHERE alignment = :align
                """,
            {
                'align' : value
            }
            )
            return self.cur.fetchall()
        except:
            print("Error checking alignment")
            return False


    def check_alts(self,value):
        try:
            self.cur.execute(
                """
                SELECT alt_id
                FROM Alter_egos
                WHERE alter_ego = :alt
                """,
            {
                'alt' : value
            }
            )
            return self.cur.fetchall()
        except:
            print("Error checking alter_egos")
            return False


    def check_group(self,value):
        #print(value)
        try:
            self.cur.execute(
                """
                SELECT group_id
                FROM Groups
                WHERE group_name = :grp
                """,
            {
                'grp' : value
            }
            )
            return self.cur.fetchall()
        except Exception as e:
            print("Error checking group")
            print(e)
            return False


    def check_publisher(self,value):
        try:
            self.cur.execute(
                """
                SELECT pub_id
                FROM Publishers
                WHERE publisher = :pub
                """,
            {
                'pub' : value
            }
            )
            return self.cur.fetchall()
        except:
            print("Error checking publisher")
            return False


    def import_data(self,csv_file):
        with open(csv_file,'r') as data:
            reader = csv.reader(data)
            records = 0
            for row in reader:
                if records != 0:
                    # extract data from CSV row
                    name = row[0]
                    intelligence = row[1]
                    strength = row[2]
                    speed = row[3]
                    durability = row[4]
                    power = row[5]
                    combat = row[6]
                    full_name = row[7]
                    alter_egos = row[8]
                    aliases = row[9]
                    publisher = row[12]
                    alignment = row[13]
                    groups = row[24]
                    image = row[26]
                    
                    # insert data into database
                    self.insert_alignment(alignment)
                    self.insert_publisher(publisher)
                    self.insert_alter_ego(alter_egos.split(";"))
                    self.insert_alias(aliases.split(";"))
                    self.insert_group(groups.split(";"))
                    self.insert_hero(name,full_name,intelligence,strength,speed,durability,power,combat,alignment,publisher,image)


                records += 1
                print(f"{records} heroes processed.")        