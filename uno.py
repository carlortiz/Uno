import random

types = ["number", "skip", "reverse", "draw_two",
         "wild", "wild_draw_four"]
colors = ["red", "yellow", "green", "blue"]
players = []

# CARD CLASS
class Card():

    def __init__(self):
        self.type = None
        self.color = colors[self.set_color()]
        self.number = None

    def set_type(self):
        type = random.randint(1, 28)

        if type <= 20:
            return

    def set_color(self):
        return random.randint(0,3)


# PLAYER CLASSES
class Robot_Player():

    def __init__(self, name):
        self.name = name

        players.append(self)

class Real_Player():

    def __init__(self):
        self.name = input("Your Name: ").upper()

        players.append(self)

# GAME STARTS HERE

# Create Players
player_one = Real_Player()
player_two = Robot_Player("JACK")
player_three = Robot_Player("RABBIT")

# Set Up Game (order of turns, game over status, top card of discard pile)
game_rotation = "clockwise"
game_over = False
top_card = None

# Deal Cards

# Start Game

    # Start Current Player's Turn

    # Check If Current Player Is Winner

    # Switch Turns
