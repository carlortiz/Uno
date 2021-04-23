import random

types = ["Number", "Skip", "Reverse", "Draw_Two",
         "Wild", "Wild_Draw_Four"]
colors = ["red", "yellow", "green", "blue"]
players = []

# CARD CLASS
class Card():

    def __init__(self):
        self.type = self.set_type()
        self.color = self.set_color()

    def set_type(self):
        random_type = random.randint(1, 28)
        types_index = 0

        if random_type == 21 or random_type == 22:
            types_index = 1
        elif random_type == 23 or random_type == 24:
            types_index = 2
        elif random_type == 25 or random_type == 26:
            types_index = 3
        elif random_type == 27:
            types_index = 4
        elif random_type == 28:
            types_index = 5

        return types[types_index]

    def set_color(self):
        return colors[random.randint(0,3)]


# PLAYER CLASSES
class Players():

    def __init__(self):
        self.cards = []

        players.append(self)

    def draw_card(self):
        drawn_card = Card()
        self.cards.append(drawn_card)
        print(drawn_card.type)

    def receive_skip(self):
        pass

    def receive_draw_two(self):
        pass
        # self.receive_skip()

    def receive_wild_draw_four(self):
        pass
        # self.receive_skip()

class Robot_Player(Players):

    def __init__(self, name):
        super().__init__()
        self.name = name

        players.append(self)

class Real_Player(Players):

    def __init__(self):
        super().__init__()
        self.name = input("Your Name: ").upper()

# GAME STARTS HERE

# Create Players
player_one = Real_Player()
player_two = Robot_Player("JACK")
player_three = Robot_Player("RABBIT")

# Set Up Game (order of turns, game over status, top card of discard pile)
game_rotation = "clockwise"
game_over = False
top_card = player_one.draw_card()

# Deal Cards
for player in players:
    for card in range(0, 7):
        player.draw_card()

# Start Game

    # Start Current Player's Turn

    # Check If Current Player Is Winner

    # Next Turn
