import random
import json


with open("Resources/characters.json", "r") as f:
    characters_json = json.load(f)

with open("Resources/weapons.json", "r") as w:
    weapons_json = json.load(w)


class Character:
    def __init__(self, name: str, weapon_key: str = None):

        self.name: str = name
        self.health: int = 100
        self.active_weapon_key: str = weapon_key
        self.weapon_info: dict = weapons_json[self.active_weapon_key]
        self.weapon_name: str = self.weapon_info["name"]
        self.weapon_damage: int = self.weapon_info["damage"]
        self.level: int = 1

    def change_weapon(self, new_weapon_key: str):

        self.active_weapon_key: str = new_weapon_key
        self.weapon_info: dict = weapons_json[self.active_weapon_key]
        self.weapon_name: str = self.weapon_info["name"]
        self.weapon_damage: int = self.weapon_info["damage"]


    def dialogue(self):
        """Introduces the charater(s)"""
        print(f"My name is {self.name}")
        print(f"My weapon is {self.weapon_name}")
        print(f"It does {self.weapon_damage} DAMAGE!")


characters = {}
random_number_of_charaters = random.randint(1, 3)

for x in range(random_number_of_charaters):
    random_character = random.choice(list(characters_json.keys()))
    # While selectd character has already been chosen/ pick a new character
    while random_character in characters.keys():
        random_character = random.choice(list(characters_json.keys()))
    characters[random_character] = Character(
        random_character, characters_json[random_character]["default_weapons"])


# for character in characters.values():
#     character.dialogue()

# HOW TO TAKE DAMAGE AWAY FROM CHARACTERS
current_character: Character = characters[random_character]

current_character.change_weapon("GUN_vandal")
print(current_character.name)
print(current_character.weapon_info)
current_character.dialogue()
