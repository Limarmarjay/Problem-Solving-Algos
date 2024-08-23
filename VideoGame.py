# A video game program created using classes, instance variables, methods (class functions) and objects

class GamePlayer:
    def __init__(self, gender, name, outfit, health=100, weapon="sword"):
        # Instance variables/characteristics of game players
        self.gender = gender
        self.name = name
        self.outfit = outfit
        self.health = health
        self.weapon = weapon
    # Methods & Behaviors of players/Player activities 
    def attackPlayer(self, target, damage):
        # Reduce target's health by damage, pass in player object as target
        target.health -= damage


# Game World class
class CustomWorld:
    def __init__(self, world_name):
        self.world_name = world_name

    def selectWorld(self):
        print("{} selected.".format(self.world_name))


# Player instance creation
player1 = GamePlayer("male", "Naruto", "armor")
player2 = GamePlayer("female", "Sakura", "armor")

# World instance Creation
world = CustomWorld("Eldoria Fantasy World")

# Use created world object to customize the battle location
world.selectWorld()

# Use created player objects to perform actions in the game
player1.attackPlayer(player2, 15)
player2.attackPlayer(player1, 25)


# Keep playing game until one player's health is zero

while True:
    if player1.health <= 0:
        print("Game over!!!")
        print("{} wins!!!".format(player2.name))
        break
    elif player2.health <= 0:
        print("Game over!!!")
        print("{} wins!!!".format(player1.name))
        break

    # Execute players actions
    player1.attackPlayer(player2, 15)
    player2.attackPlayer(player1, 25)
    player1.attackPlayer(player2, 15)
    player2.attackPlayer(player1, 25)
    player1.attackPlayer(player2, 20)
    player2.attackPlayer(player1, 50)

    # End of while loop
