import random

colors = ["red", "yellow", "green", "blue"]
players = []

# CARD CLASS
class Card():

    def __init__(self):
        self.type = "no type"
        self.color = "no color"
        self.number = "no number"

    def set_color(self):
        return colors[random.randint(0,3)]

    def show_info(self):
        print(self.type, ",", self.color, ",", self.number)

    @classmethod
    def generate_card(cls):
        card = Number_Card()
        random_type = random.randint(1, 28)

        if random_type == 21 or random_type == 22:
            card = Skip_Card()
        elif random_type == 23 or random_type == 24:
            card = Reverse_Card()
        elif random_type == 25 or random_type == 26:
            card = Draw_Two_Card()
        elif random_type == 27:
            card = Wild_Card()
        elif random_type == 28:
            card = WD4_Card()

        return card

class Number_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "number"
        self.color = self.set_color()
        self.number = self.set_number()

    def set_number(self):
        return random.randint(0, 9)

class Skip_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "skip"
        self.color = self.set_color()

    def take_effect(self, player):
        player.is_skipped = True

class Reverse_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "reverse"
        self.color = self.set_color()

class Draw_Two_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "draw two"
        self.color = self.set_color()

    def take_effect(self, player):
        player.draw_card()
        player.draw_card()

class Wild_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "wild"

    def set_color(self):
        print("The colors are red, yellow, green, and blue.")
        print("What color will your wild card be?")
        color = input("(r/y/g/b: ")

        return color

class WD4_Card(Card):

    def __init__(self):
        super().__init__()
        self.type = "wild draw four"

    def set_color(self):
        print("The colors are red, yellow, green, and blue.")
        print("What color will your wild card be?")
        color = input("(r/y/g/b: ")

        return color

    def take_effect(self, player):
        for num in range(1, 4):
            player.draw_card()

# PLAYER CLASSES
class Player():

    def __init__(self):
        self.cards = []
        self.received_card = None
        self.is_skipped = False

        players.append(self)

    def draw_card(self):
        card = Card.generate_card()
        self.cards.append(card)

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
top_card = Card.generate_card()

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

    for card in current_player.cards:
        current_player.check_card(card)

    if isinstance(current_player.received_card, Skip_Card):
        current_player.received_card.take_effect(current_player)
    elif isinstance(current_player.received_card, Draw_Two_Card):
        current_player.received_card.take_effect(current_player)
    elif isinstance(current_player.received_card, WD4_Card):
        current_player.received_card.take_effect(current_player)

    # if not current_player.is_skipped:
        # choose_card = input("Play a card? (y/n): ")

        # if choose_card is yes:
        #   chosen_card = current_player.pick_card()
        #   ^ make sure it checks for eligibility, if not draw card
        #   top_card = chosen_card
        # else if no:
        #   current_player.draw_card()
        #
        # current_player.is_skipped = False

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

