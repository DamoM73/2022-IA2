# frontend.py

class UI():

    def __init__(self):
        pass

    def main_menu(self):
        print("1. Deal")
        print("2. Set pack size")
        print("9. Exit")
        return self.get_response("Please choose> ", [1, 2, 9])

    def pack_size_menu(self):
        print("Pack size: 10 - 726")
        options = list(range(10,726))
        return self.get_response("Enter size> ", options)

    def get_response(self,prompt, values):
        response = ""
        
        while response not in values:
            try:
                response = int(input(prompt))
            except:
                print("Please enter a number.")
        return response