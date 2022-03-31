def get_alias_list(aliases):
        alias_list = []
        word = ""
        for index, letter in enumerate(aliases):
            if index != 0:
                if letter.isupper() and aliases[index - 1].islower():
                    alias_list.append(word)
                    word = letter
                else:
                    word += letter
            else:
                word += letter
                
        return alias_list
                    
                    
                    
                    
print(get_alias_list("Laura LoganLaura HowlettLaura XTalonWolverineX23"))