# frontend.py

class UI():

    def __init__(self):
        pass

    def main_menu(self):
        print("1. Build database") 
        print("2. Exit")
        return self.get_response("Please choose> ", 1, 2)

    def get_response(self,prompt,*values):
        response = ""
        while response not in values:
            response = int(input(prompt))
        return response