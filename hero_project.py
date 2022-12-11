# Luke Bobrowski
# 8 December 2022
# Game Character Class

import random
import time


class Chacater:
  """Describes a hero"""

  def __init__(self, name, nickname, superpower, arch_type):
    self.arch_type = arch_type
    self.name = name
    self.power = superpower
    self.nickname = nickname
    self.health = 100
    self.damage = random.randint(15, 25)

  def describe_hero(self, ):
    print(
      f"You might of not heard of this hero... \nbut he goes by the name {self.nickname} or {self.name} if you know him personally."
    )
    print(
      f"He has the ability to '{self.power}' which helps him take \ndown his evil neighbor {villin.name}!"
    )

  def describe_villin(self):
    print(
      f"{villin.name} has been in this neighborhood since the beginning of 2000. \nHe figths with {hero.name} to defend his name as best neighbor! "
    )

  def battle_diolouge(self):
    print(
      f"One day, {villin.name} was mowing his lawn and sprayed all the fresh cut grass \nonto {hero.name} driveway! {hero.name} had enough of this nonsense!! He challenged \n{villin.name} to a..."
    )

  def attack(self):
    print(f"{hero.name} ATTACKED!")
    villin.health -= hero.damage
    print(f"{hero.name} did ({hero.damage}) DAMAGE")
    print(f"{villin.name} HEALTH: {villin.health}")
    print("-------------------")
    return villin.health

  def evil_attack(self):
    print(f"{villin.name} ATTACKED!")
    hero.health -= villin.damage
    print(f"{villin.name} did ({villin.damage}) DAMAGE")
    print(f"{hero.name} HEALTH: {hero.health}")
    print()
    print("-------------------")
    return hero.health

  def battle(self, hero_health, villin_health):

    while hero_health > 0 or villin_health > 0:
      #rand_damage = 0
      attack_turn = 0
      attack_turn = random.randint(1, 2)
      time.sleep(2)
      if attack_turn == 1:
        hero.attack()
        #
      elif attack_turn == 2:
        villin.evil_attack()
        #return rand_damage


hero = Chacater("Jerry", "Jerrinator", "Make the perfect patties",
                "The innocent")
villin = Chacater("Tony", "Tonestone", "Mow the lawn perfectly", "The Jester")

hero.describe_hero()
# time.sleep(8)
print()
villin.describe_villin()
# time.sleep(6)
print()
hero.battle_diolouge()
# time.sleep(6)
print("\nDAD")
# time.sleep(1)
print("OFF")
# time.sleep(2)
print("\nTHE BATTLE BEGINS!!")
print()
# returned_damage =
character1_health = hero.attack()
character2_health = villin.evil_attack()
hero.battle(character1_health, character2_health)
