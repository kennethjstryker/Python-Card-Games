import random as rand

# Creates the initial Wild object which is what will be called to assign the wild card to a certain color to continue game
class Wild(object):  
    def setWildBlue(self):
        if self.color == 'Wild':
            self.color = 'Blue'
        else:
            pass

    def setWildGreen(self):
        if self.color == 'Wild':
            self.color = 'Green'
        else:
            pass

    def setWildYellow(self):
        if self.color == 'Wild':
            self.color = 'Yellow'
        else:
            pass

    def setWildRed(self):
        if self.color == 'Wild':
            self.color = 'Red'
        else:
            pass                

# Very boring and basic Deck class that has a "Shuffle" feature
# As well as a "Deal" feature or method depending on who asked
class Deck(object):
    def shuffle(self):
        rand.shuffle(self.cards)
        print("Deck shuffled!")
    
    def deal(self):
        return self.cards.pop(0)

# Creates the rules needed for an Uno Card to exist
class Uno_Card(Wild):
    def __init__(self, name, value, color):
        self.value   = value
        self.name    = name
        self.showing = False
        self.color   = color

    
    def __repr__(self):
        if self.showing is True:
            return "{1} {0}".format(self.name, self.color)
        else:
            return "Uno Card"

# Creates the actual deck of Uno Cards
class Uno_Deck(Deck):
    def __init__(self):
        self.cards   = []
        values = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six': 6, 'Seven':7, 'Eight': 8, 'Nine': 9, 'Draw Two':10, 'Skip':11, 'Reverse':12}
        wild   = {'Wild':13,'Draw 4 Wild':14}
        zero   = {'Zero': 15}
        colors = ['Red', 'Blue', 'Green', 'Yellow']


        for name in zero:
            for color in colors:
                self.cards.append(Uno_Card(name, zero[name], color))    

        # Deck creation loop 
        for name in values:
            for color in colors:
                for i in range(2):
                    self.cards.append(Uno_Card(name, values[name], color))
        
        for name in wild:
            for i in range(4):
                self.cards.append(Uno_Card(name, wild[name], 'Wild'))         

    def __repr__(self):
        return 'This deck of Uno cards still has {0} cards'.format(len(self.cards))

# The Player class this is the actual person who'll be playing
# Or robot mwahahaha
class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
    
    def __repr__(self):
        return "{0} has {1} cards".format(self.name, len(self.hand))

# The start of
class Uno_Game(object):
    def __init__(self):
        self.gameDeck = Uno_Deck()
        self.gameDeck.shuffle()

kenny = Player("boi")
game = Uno_Game()

for i in range(7):
    kenny.hand.append(game.gameDeck.deal())

print(kenny.hand)


        
