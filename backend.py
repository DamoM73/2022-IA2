import sqlite3

class Database():
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        # build the database
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
	        "align_id"	INTEGER,
	        "pub_id"	INTEGER,
	        PRIMARY KEY("hero_id" AUTOINCREMENT),
	        FOREIGN KEY("align_id") REFERENCES "alignment"("align_id"),
	        FOREIGN KEY("pub_id") REFERENCES "publisher"("pub_id")
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


    def __del__(self):
        self.cur.close()


