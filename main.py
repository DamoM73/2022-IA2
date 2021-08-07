# main.py

from backend import Database
from frontend import UI
from game_elements import Card
import random

def create_db():
    hero_data.import_data("super_hero.csv")

def create_deck():
    heroes = hero_data.get_hero_details()
    deck = []
    for hero in heroes:
        deck.append(Card(hero))
    return deck

def deal(pack):
    player = []
    deck_size = len(pack)
    while len(pack) > deck_size/2:
        card = random.randint(0,len(pack)-1)
        player.append(pack.pop(card))
    return player, pack

hero_data = Database("hero_py.db")
main_window = UI()

#----- MAIN LOOP -----
running = True
deck = create_deck()
player_hand, AI_hand = deal(deck)

random.choice(player_hand).show_card()


"""
while running:
    response = main_window.main_menu()
    if response == 1:
        create_db()
    elif response == 2:
        running = False
"""