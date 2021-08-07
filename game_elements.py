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

    
    def show_card(self):
        print(f"Name: {self.name}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        print(f"Durability: {self.durability}")
        print(f"Power: {self.power}")
        print(f"Combat: {self.combat}")
        print(f"Publisher: {self.publisher}")
