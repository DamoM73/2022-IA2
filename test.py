from backend import Database

db = Database("hero_py.db")

print(db.get_hero_details())