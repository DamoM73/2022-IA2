# main.py

from backend import Database
from frontend import UI

def create_db():
    hero_data.import_data("super_hero.csv")

hero_data = Database("hero_py.db")
main_window = UI()

#----- MAIN LOOP -----
running = True

while running:
    response = main_window.main_menu()
    if response == 1:
        create_db()
    elif response == 2:
        running = False