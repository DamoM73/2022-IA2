import random

class Card():

    def __init__(self, details):
        self.name = details[0]
        self.intelligence = details[1]
        self.strength = details[2]
        self.speed = details[3]
        self.durability = details[4]
        self.power = details[5]
        self.combat = details[6]
        self.publisher = details[7]
        self.image = details[8]

    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Durability: {self.durability}")
        print(f"Power: {self.power}")
        print(f"Combat: {self.combat}")
        print(f"Publisher: {self.publisher}")


class Pack():

    def __init__(self,db):
        self.pack = []
        self.cards = db.get_details()
        self.size = len(self.cards)

        self.create_pack()

    def create_pack(self):
        self.pack=[]
        index = 0
        while index < self.size:
            pick = random.randint(0,self.size-1)
            self.pack.append(Card(self.cards[pick]))
            index += 1

    def set_size(self,size):
        self.size = size
        self.create_pack()

    def display(self):
        for card in self.pack:
            card.display()
    
    def deal(self,player,ai):
        dealing = self.pack
        while len(player.deck) < len(dealing):
            pick = random.randint(0,len(dealing)-1)
            player.deck.append(dealing.pop(pick))
        ai.deck = dealing

class Deck():

    def __init__(self, name):
        self.name = name
        self.deck = []

    def display(self):
        for card in self.deck:
            card.display()
        self.count()

    def count(self):
        print(f"{self.name.capitalize()} deck: {len(self.deck)}")