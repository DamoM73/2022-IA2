import csv

def new_alias(alias):
    new_cell = ""
    index = 0
    for char in alias:
        if alias[index].isupper() and alias[index-1] not in [" ",'"',"-","."]  and index != 0:
            new_cell += ";" + char
        else:
            new_cell += char
        index += 1
    return new_cell



with open("superhero.csv", "r") as data:
    reader = csv.reader(data)
    for row in reader:
        new_row = row
        new_row[9] = new_alias(row[9])
        
        with open("super_hero.csv", "a", newline='') as dest:
            writer = csv.writer(dest)
            writer.writerow(new_row)
        
