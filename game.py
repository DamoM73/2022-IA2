import random

class Game():

    def __init__(self,player,ai):
        self.player_deck = player
        self.ai_deck = ai
        self.turn = random.choice(["player","ai"])

        
    