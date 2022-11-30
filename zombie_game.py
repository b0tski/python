import random 
import json


with open("Resources/characters.json", "r") as f:
    char_info = json.load(f)

with open("Resources/weapons.json", "r") as w:
    weap_info = json.load(w)

class Character:
    def __init__(self, name, weapon=None):

        self.name = name
        self.health = 100
        self.weapon = weap_info[weapon]
        self.weapon_name = self.weapon["name"]
        self.damage = self.weapon["damage"]
        self.level = 1

    
    def dialogue(self):
        """Introduces the charater(s)"""
        print(f"My name is {self.name}")
        print(f"My weapon is {self.weapon_name}")

characters = {}
random_number_of_charaters = random.randint(1,3)

for x in range(random_number_of_charaters):
    random_character = random.choice(list(char_info.keys()))
    while random_character in characters.keys():
        random_character = random.choice(list(char_info.keys()))
    characters[random_character] = Character(random_character, char_info[random_character]["default_weapons"])


for character in characters.values():
    character.dialogue()

#HOW TO TAKE DAMAGE AWAY FROM CHARACTERS
# characters["Jeff"].health -=1
# print(characters["Jeff"].health)






