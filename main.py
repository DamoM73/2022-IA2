from backend import Database

hero_data = Database("hero_py.db")

hero_data.import_data("super_hero.csv")