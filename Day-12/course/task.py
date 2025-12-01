enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
# def drink_potion():
#     potion_strength = 2
#     print({potion_strength})
#
# drink_potion()
# print(potion_strength)

#global scope
player_health = 100

def drink_potion():
      potion_strength = 2
      print(player_health)

drink_potion()

#Block scope
game_level = 3
enemies = ["skeleton", "zombies", "alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()

#accessing global vars
hero = 1
def increase_hero():
    global hero
    hero = 2
    print(f"hero inside function: {hero}")

increase_hero()
print(f"hero outside function: {hero}")

#global constants
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

