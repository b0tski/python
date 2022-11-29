import random 

character_list = ["Jeff", "Claire", "Bob"]
random_number_of_charaters = random.randint(1,3)
print(random_number_of_charaters)

class Character:
    def __init__(self, name, weapon=None):

        self.name = name
        self.health = 100
        self.damage = 10
        self.weapon = weapon

    
    def dialogue(self):
        print(f"My name is {self.name}")

characters = {}

for x in range(random_number_of_charaters):
    random_character = random.choice(character_list)

    characters[random_character] = Character(random_character)
    character_list.remove(random_character)

for character in characters.values():
    character.dialogue()

print(characters["Jeff"].health)
