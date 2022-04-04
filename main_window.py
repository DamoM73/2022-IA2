import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from ui_smuc import Ui_MainWindow
from datastore import SuperheroDB
from game import Card
import random


class MainWindow:
    def __init__(self):
        # creating main window
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # create databases
        self.shdb = SuperheroDB()
        
        # establish all possible cards
        self.deck = self.establish_poss_cards()
        
        # create game pack
        self.pack_size = 10
        self.pack = self.get_game_pack()
        
        # establish ranking
        for card in self.pack:
            card.get_rankings(self.pack)
            
        # deal hands
        self.player_hand = []
        self.ai_hand = []
        while len(self.pack) > 0:
            self.player_hand.append(self.pack.pop(0))
            self.ai_hand.append(self.pack.pop(0))
            
        self.update_display()
        
        
        
    def establish_poss_cards(self):
        max_cards = self.shdb.get_last_superhero_id()
        all_cards = list(range(1, max_cards + 1))
        random.shuffle(all_cards)
        return all_cards
    
    
    def get_game_pack(self):
        temp_pack = []
        index = 0
        while len(temp_pack) < self.pack_size:
            card = Card(self.shdb.get_card_details(self.deck[index]))
            if not card.all_blank():
                temp_pack.append(card)
            index += 1
        return temp_pack
        
    
    def display_player_card(self,card):
        self.ui.player_name_lb.setText(card.name)
        self.ui.player_intel_lb.setText(str(card.intel))
        self.ui.player_str_lb.setText(str(card.strength))
        self.ui.player_spd_lb.setText(str(card.speed))
        self.ui.player_dura_lb.setText(str(card.durability))
        self.ui.player_pwr_lb.setText(str(card.power))
        self.ui.player_combat_lb.setText(str(card.combat))
        player_img = QPixmap(card.image).scaledToHeight(320)
        self.ui.player_img_lb.setPixmap(player_img)
        
        
    def display_ai_card(self,card):
        self.ui.ai_name_lb.setText(card.name)
        self.ui.ai_intel_lb.setText(str(card.intel))
        self.ui.ai_str_lb.setText(str(card.strength))
        self.ui.ai_spd_lb.setText(str(card.speed))
        self.ui.ai_dura_lb.setText(str(card.durability))
        self.ui.ai_pwr_lb.setText(str(card.power))
        self.ui.ai_combat_lb.setText(str(card.combat))
        ai_img = QPixmap(card.image).scaledToHeight(320)
        self.ui.ai_img_lb.setPixmap(ai_img)


    def update_display(self):
        """
        Refreshes the display
        """
        # top cards
        self.display_player_card(self.player_hand[0])
        self.display_ai_card(self.ai_hand[0])
        
        # update deck numbers
        self.ui.player_hand_lb.setText(str(len(self.player_hand)))
        self.ui.ai_hand_lb.setText(str(len(self.ai_hand)))
        
    
    
    def show(self):
        self.main_win.show()

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        pass
    
    # ----- slots ----- #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())