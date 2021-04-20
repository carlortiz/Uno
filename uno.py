import random

# CARD CLASSES
class Card():
    colors = ["Red", "Yellow", "Green", "Blue"]
    top_card = None

    def __init__(self):
        self.color = self.set_color()

    def set_color(self):
        return Card.colors[random.randint(0, 3)]

    def show_info(self):
        print(type(self), ", ", self.color)

class Number_Card(Card):

    def __init__(self):
        super().__init__()
        self.number = random.randint(0, 9)

    def show_info(self):
        print("Number Card, ", self.color, ", ", self.number)

class Skip_Card(Card):

    def __init__(self):
        super().__init__()

class Reverse_Card(Card):

    def __init__(self):
        super().__init__()

class Draw_Two_Card(Card):
    draw_amount = 2

    def __init__(self):
        super().__init__()

class Wild_Card(Card):

    def __init__(self):
        super().__init__()

    def check_elibility(self):
        return True

class Draw_Four_Card(Card):
    draw_amount = 4

    def __init__(self):
        super().__init__()

# PLAYER CLASSES
class Player():

    def __init__(self):
        self.cards = []
        self.win_status = False
        self.name = None

    def draw_card(self):
        random_num = random.randint(1, 28)
        self.card = Number_Card()

        if random_num is 21 or random_num is 22:
            self.card = Skip_Card()
        elif random_num is 23 or random_num is 24:
            self.card = Reverse_Card()
        elif random_num is 25 or random_num is 26:
            self.card = Draw_Two_Card()
        elif random_num is 27:
            self.card = Wild_Card()
        else:
            self.card = Draw_Four_Card()

        self.cards.append(self.card)
        print("A card has been drawn for ", self.name)

    def play_card(self, card):
        Card.top_card = card
        print(self.name, " has played this card: ", card.show_info())

    def match_cards(self, card_one, card_two):
        if type(top_card) is type(chosen_card):
            return True
        elif top_card.color is chosen_card.color:
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
        self.name = input("Your Name: ")

    def check_cards(self):
        card_number = 0
        for card in self.cards:
            print("Card ", card_number, ": ", card.show_info())

    def choose_card(self):
        print("Which card would you like to choose? ")
        chosen_card = input("Card #: ")
        return self.cards[chosen_card]


# GAME STARTS HERE

# Create Players
player_one = Player()
player_two = Robot_Player("Dog")
player_three = Robot_Player("Ship")
player_four = Robot_Player("Top Hat")

players = [player_one, player_two, player_three, player_four]
current_turn = 0
current_player = players[current_turn]

# Set Up Game (order of turns, game over status, top card of discard pile)
game_rotation = "clockwise"
game_over = False
Card.top_card = current_player.draw_card()

# Deal Cards
for player in players:
    for card in range (0, 7):
        player.draw_card()

# Start Game
while game_over is False:

    # Start Current Player's Turn (REAL PLAYER)
    Card.top_card.show_info()
    if type(current_player) is Real_Player():
        current_player.check_cards()
        will_play = input("Would you like to place a card on top of the pile? (y/n): ")

        if will_play:
            chosen_card = current_player.choose_card()
            card_eligible = current_player.match_cards(Card.top_card, chosen_card)
            if card_eligible:
                current_player.play_card(chosen_card)
            else:
                current_player.draw_card()
        else:
            current_player.draw_card()

    # Start Current Player's Turn (ROBOT PLAYER)

    # Check If Current Player Is Winner
    if current_player.cards.len() is 0:
        current_player.win_status = True
        game_over = True

    # Switch Turns
    if game_rotation is "clockwise":
        if current_turn is 4:
            current_turn = 0
        else:
            current_turn = current_turn + 1
        current_player = players[current_turn]
    else:
        if current_turn is 0:
            current_turn = 4
        else:
            current_turn = current_turn - 1
        current_turn = players[current_turn]