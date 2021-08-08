# main.py

from backend import Database
from frontend import UI
from game_elements import Card, Pack, Deck


hero_data = Database("hero_py.db","super_hero.csv")

main_window = UI()
pack = Pack(hero_data)
player_deck = Deck("player")
ai_deck = Deck("ai")



#----- MAIN LOOP -----
running = True
while running:
    response = main_window.main_menu()
    # Deal
    if response == 1:
        pack.deal(player_deck,ai_deck)
        player_deck.count()
        ai_deck.count()
    elif response == 2:
        size = main_window.pack_size_menu()
        pack.set_size(size)
    elif response == 9:
        running = False
