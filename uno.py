import random

types = ["number", "skip", "reverse", "draw_Two",
         "wild", "wild_draw_four"]
colors = ["red", "yellow", "green", "blue"]
players = []

# CARD CLASS
class Card():

    def __init__(self):
        self.type = self.set_type()
        self.color = self.set_color()
        self.number = None

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

    def show_info(self):
        print(self.type, ", ", self.color, ", ", self.number)

    @classmethod
    def get_top_card(cls):
        top_card = Card()
        return top_card

# PLAYER CLASSES
class Player():

    def __init__(self):
        self.cards = []
        self.received_card = None

        players.append(self)

    def draw_card(self):
        drawn_card = Card()
        self.cards.append(drawn_card)

    def check_card(self, card):
        card.show_info()

    def is_first_player(self, index):
        if index == 0:
            return True
        else:
            return False

    def is_last_player(self, index):
        if index == len(players) - 1:
            return True
        else:
            return False

class Robot_Player(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name

class Real_Player(Player):

    def __init__(self):
        super().__init__()
        self.name = input("Your Name: ").upper()

# GAME STARTS HERE

# Create Players
player_one = Real_Player()
player_two = Robot_Player("RABBIT")
player_three = Robot_Player("DURANTULA")
player_four = Robot_Player("THE MAN")

# Set Up Game (order of turns, game over status, top card of discard pile)
game_rotation = "counterclockwise"
game_over = False
top_card = Card.get_top_card()

# Deal Cards
for player in players:
    for card in range(0, 7):
        player.draw_card()

# Start Game
players_index = 0

while game_over == False:

    # Start Current Player's Turn
    current_player = players[players_index]
    current_player.check_card(top_card)

    # Check If Current Player Is Winner
    if len(current_player.cards) == 0:
        print(current_player.name, " is the winner!")
        game_over = True

    # Next Turn
    if game_rotation == "clockwise":
        if current_player.is_last_player(players_index):
            players_index = 0
        else:
            players_index = players_index + 1
    else:
        if current_player.is_first_player(players_index):
            players_index = len(players) - 1
        else:
            players_index = players_index - 1

