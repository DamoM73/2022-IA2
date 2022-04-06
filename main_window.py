import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtTest import QTest
from ui_smuc import Ui_MainWindow
from datastore import SuperheroDB
from game import Card
import random
import time


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
        self.pack_size = 20
        self.pack = self.get_game_pack()
            
        # deal hands
        self.player_hand = []
        self.ai_hand = []
        self.kitty = []
        self.deal_hands()
        
        # game state variables
        self.reveal = False
                
        # change display
        self.update_display()
        
        self.signals()
        
        
    def establish_poss_cards(self):
        """
        generates all cards with stats, then shuffles them
        """
        max_cards = self.shdb.get_last_superhero_id()
        all_cards = list(range(1, max_cards + 1))
        random.shuffle(all_cards)
        return all_cards
    
    
    def get_game_pack(self):
        """
        Draws required number of cards to form pack
        Establishes the ranking of card's stats
        """
        # generate pack
        temp_pack = []
        index = 0
        while len(temp_pack) < self.pack_size:
            card = Card(self.shdb.get_card_details(self.deck[index]))
            if not card.all_blank():
                temp_pack.append(card)
            index += 1
        # establish ranking
        for card in temp_pack:
            card.get_rankings(temp_pack)
        return temp_pack
    
    
    def deal_hands(self):
        """
        Deals the player and AI cards from the pack
        """
        self.player_hand = []
        self.ai_hand = []
        while len(self.pack) > 0:
            self.player_hand.append(self.pack.pop(0))
            self.ai_hand.append(self.pack.pop(0))
        
            
    
    def display_player_card(self,card):
        card.show_card_details()
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
        if self.reveal:
            self.ui.ai_name_lb.setText(card.name)
            self.ui.ai_intel_lb.setText(str(card.intel))
            self.ui.ai_str_lb.setText(str(card.strength))
            self.ui.ai_spd_lb.setText(str(card.speed))
            self.ui.ai_dura_lb.setText(str(card.durability))
            self.ui.ai_pwr_lb.setText(str(card.power))
            self.ui.ai_combat_lb.setText(str(card.combat))
            ai_img = QPixmap(card.image).scaledToHeight(320)
            self.ui.ai_img_lb.setPixmap(ai_img)
        else:
            self.ui.ai_name_lb.setText("???")
            self.ui.ai_intel_lb.setText("???")
            self.ui.ai_str_lb.setText("???")
            self.ui.ai_spd_lb.setText("???")
            self.ui.ai_dura_lb.setText("???")
            self.ui.ai_pwr_lb.setText("???")
            self.ui.ai_combat_lb.setText("???")
            ai_img = QPixmap("./images/back.png").scaledToHeight(320)
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
        self.ui.kitty_lb.setText(str(len(self.kitty)))
            
    
    def compare_stat(self, player, ai):
        print(player,ai)
        if player > ai:
            return "player"
        elif player < ai:
            return "ai"
        else:
            return "draw"
    
    
    def check_for_win(self):
        if len(self.ai_hand) == 0:
            self.ui.victory_lb.setText("Player")
            return True
        elif len(self.player_hand) == 0:
            self.ui.victory_lb.setText("Computer")
            return True
        else:
            return False
    
    def show(self):
        self.main_win.show()
        

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        self.ui.player_intel_btn.clicked.connect(lambda: self.compare("intel"))
        self.ui.player_str_btn.clicked.connect(lambda: self.compare("str"))
        self.ui.player_spd_btn.clicked.connect(lambda: self.compare("spd"))
        self.ui.player_dura_btn.clicked.connect(lambda: self.compare("dura"))
        self.ui.player_pwr_btn.clicked.connect(lambda: self.compare("pwr"))
        self.ui.player_combat_btn.clicked.connect(lambda: self.compare("combat"))
    
        
    # ----- slots ----- #
    def compare(self,stat):
        # show ai card
        self.reveal = True
        self.update_display()
        
        # calcualte winner
        player_card = self.player_hand.pop(0)
        ai_card = self.ai_hand.pop(0)
        player_card.show_card_details()
        
        match stat:
            case "intel":
                result = self.compare_stat(player_card.intel, ai_card.intel)
            case "str":
                result = self.compare_stat(player_card.strength, ai_card.strength)
            case "spd":
                result = self.compare_stat(player_card.speed, ai_card.speed)
            case "dura":
                result = self.compare_stat(player_card.durability, ai_card.durability)
            case "pwr":
                result = self.compare_stat(player_card.power, ai_card.power)
            case "combat":
                result = self.compare_stat(player_card.combat, ai_card.combat)            
        
        # exchange cards
        match result:
            case "player":
                self.ui.win_lb.setText("Player")
                self.player_hand.append(player_card)
                self.player_hand.append(ai_card)
                if len(self.kitty) > 0:
                    self.player_hand.extend(self.kitty)
                    self.kitty = []
            case "ai":
                self.ui.win_lb.setText("Computer")
                self.ai_hand.append(ai_card)
                self.ai_hand.append(player_card)
                if len(self.kitty) > 0:
                    self.ai_hand.extend(self.kitty)
                    self.kitty = []
            case "draw":
                self.ui.win_lb.setText("Draw")
                self.kitty.append(player_card)
                self.kitty.append(ai_card)
        
        
        QTest.qWait(2000)
        # allow for win condition
        if self.check_for_win():
            self.pack = self.get_game_pack()
            self.player_hand = []
            self.ai_hand = []
            self.kitty = []
            self.deal_hands()
        
        # next card
        self.ui.win_lb.setText("")
        self.reveal = False
        self.update_display()
               

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())