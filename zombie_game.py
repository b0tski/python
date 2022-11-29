import random 
import json


with open("Resources/characters.json", "r") as f:
    char_info = json.load(f)



class Character:
    def __init__(self, name, weapon=None):

        self.name = name
        self.health = 100
        self.weapon: Weapon = weapon
        self.damage = self.weapon.damage
        self.level = 1

    
    def dialogue(self):
        """Introduces the charater(s)"""
        print(f"My name is {self.name}")

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


class Weapon:
    def __init__(self, name, damage, weapon_range):
        self.name = name
        self.damage = damage




army_knife = Weapon("Army Knife", 10)
brass_knuckles = Weapon("Brass Knuckles", 25)
crossbow = Weapon("Crossbow", 25)
slingshot = Weapon("Slingshot", 15)
sword = Weapon("Sword", 35)
