import random as rand

class Card(object):
    def __init__(self, name, value, suit):
        self.value   = value
        self.suit    = suit
        self.name    = name
        self.showing = False

    def __repr__(self):
        if self.showing:
            return str(self.name) + " of " + self.suit
        else:
            return "Card"

class Deck(object):
    def shuffle(self):
        rand.shuffle(self.cards)
        print("Deck shuffled!")
    
    def deal(self):
        return self.cards.pop(0)

class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,  'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13,  'Ace':14}
        suits  = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        for name in values:
             for suit in suits:
                 self.cards.append(Card(name, values[name], suit)) 

    def __repr__(self):
        return "Standard deck of cards: {0} cards remaining".format(len(self.cards))   

class Player(object):
    def __init__(self):
        self.cards = []

    def numOfCrds(self):
        pass


class PokerScorer(object):
    def __init__(self):
        self.deck = StandardDeck()
        self.royalFlush    = False
        self.straightFlush = False
        self.fullHouse     = False
        self.flush         = False
        self.straight      = False
        self.threeOfAKind  = False
        self.twoPair       = False
        self.pair          = False
        self.highCard      = False


    def suitCount(self):
        # suits = [for card.suit in self.cards]
        # return len( list( set(suits) ) )
        pass


