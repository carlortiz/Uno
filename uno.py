import random

colors = ["red", "yellow", "green", "blue"]
players = []

# CARD CLASS
class Card:
    def __init__(self):
        self.type = "no type"
        self.color = "no color"
        self.number = "no number"

    def set_color(self):
        return colors[random.randint(0, 3)]

    def show_info(self):
        print(self.type, ",", self.color, ",", self.number)

    def is_effect_card(self):
        if isinstance(self, Skip_Card):
            return True
        elif isinstance(self, Draw_Two_Card):
            return True
        elif isinstance(self, WD4_Card):
            return True

        return False

    def is_eligible(self, card):
        if isinstance(card, Wild_Card) or isinstance(card, WD4_Card):
            return True

        if self.color == card.color and isinstance(self, Wild_Card):
            return True
        elif self.color == card.color and isinstance(self, WD4_Card):
            return True

        if isinstance(card, Number_Card) and isinstance(self, Number_Card):
            if self.color == card.color or self.number == card.number:
                return True
            else:
                return False

        if self.type == card.type:
            return True

        return False

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
class Player:

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

    def pick_card(self):
        card_choice = int(input("Okay, enter the number of the card: "))

        return self.cards[card_choice - 1]

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

class RobotPlayer(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name

class RealPlayer(Player):

    def __init__(self):
        super().__init__()
        self.name = input("Your Name: ").upper()

# Create Players
player_one = RealPlayer()
player_two = RobotPlayer("RABBIT")
player_three = RobotPlayer("DURANTULA")
player_four = RobotPlayer("THE MANN")

# Set Up Game (order of turns, game over status, top card of discard pile)
game_rotation = "clockwise"
game_over = False
top_card = Number_Card()

# Deal Cards
for player in players:
    for card in range(0, 7):
        player.draw_card()

# Start Game
players_index = 0

while not game_over:

    # Start Current Player's Turn
    current_player = players[players_index]
    print("* It is now", current_player.name, "'s turn.")

    print("* Now showing top card: ")
    current_player.check_card(top_card)

    print("\n* Now showing", current_player.name, "'s cards: ")
    cards_index = 1

    for card in current_player.cards:
        print("- card ", cards_index, "~", end = ' '),
        current_player.check_card(card)
        cards_index += 1

    # Check if current player receives a draw two, draw four, or skip card
    if current_player.received_card:
        if current_player.received_card.is_effect_card():
            current_player.received_card.take_effect()

    # Check if player wants to play a card if not skipped
    if current_player.is_skipped is False:
        will_choose_card = input("* Play a card? (y/n): ")
    else:
        will_choose_card = "n"

    if will_choose_card == "y":
        chosen_card = current_player.pick_card()
        if top_card.is_eligible(chosen_card):
            top_card = chosen_card
            current_player.cards.remove(chosen_card)
    elif will_choose_card == "n":
        current_player.draw_card()

    current_player.is_skipped = False

    # Check If Current Player Is Winner
    if len(current_player.cards) == 0:
        print(current_player.name, " is the winner!")
        game_over = True

    # Next Turn
    if isinstance(top_card, Reverse_Card):



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

    print("\n")