import random
import matplotlib.pyplot as plt
import numpy as np

class Card(object):
    """Create a playing card object
    """
    suit_names = ["Joker","Diamonds","Clubs","Hearts","Spades"]
    rank_names = ['Joker','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    
    def __init__(self,suit=0,rank=0):
        "create a new card"
        self.suit = suit
        self.rank = rank
        self.rankname = Card.rank_names[self.rank]

    def __str__(self):
        "returns a string represenatation of the card created"
        return '%s of %s' %(Card.rank_names[self.rank],Card.suit_names[self.suit])

    def __repr__(self):
        "returns a string represenatation of the card created"
        return '%s of %s' %(Card.rank_names[self.rank],Card.suit_names[self.suit])


class Deck(object):
    "Create a Full Deck of Cards"

    def __init__(self,inc_jok = False):
        self.inc_jok = inc_jok
        self.deck_of_cards = []
        if self.inc_jok == True:
            for i in range(1,5):    
                for j in range(1,14):
                    card = Card(i,j)
                    self.deck_of_cards.append(card)
            self.deck_of_cards.append(Card(0,0))
            self.deck_of_cards.append(Card(0,0))
        elif self.inc_jok == False:
            for i in range(1,5):
                for j in range(1,14):
                    card = Card(i,j)
                    self.deck_of_cards.append(card)

    def __str__(self):
        string_cards = []
        for i in self.deck_of_cards:
            string_cards.append(str(i))
        return '\n'.join(string_cards)

    def __repr__(self):
        string_cards = []
        for i in self.deck_of_cards:
            string_cards.append(str(i))
        return '\n'.join(string_cards)        

    def shuffle(self):
        random.shuffle(self.deck_of_cards)

    def add_card(self,card):
        self.deck_of_cards.append(card)

    def remove_card(self,card):
        self.deck_of_cards.remove(card)

    def pop_card(self,i=-1):
        return self.deck_of_cards.pop(i)

    def deal_card(self,hand,num):
        "Deals number of cards to a given hand"
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Creates a hand of playing cards."""
    
    def __init__(self, label=''):
        self.deck_of_cards = []
        self.label = label

    def __str__(self):
        return self.label + ' currently has hand \n' + str(self.deck_of_cards) 

    def update_label(self,newlabel):
        self.label = newlabel



class Blackjack():
    """Sets up a game of Blackjack"""

    def __init__(self): #,num_of_players=1,num_of_decks=1):        
        self.num_of_players = 1 # num_of_players
        self.num_of_decks = 1 #num_of_decks
        self.hand_scores = [ [] for i in range(self.num_of_players+1)]
        self.round_scores = [0,0]
        self.discardpile = Hand('Discard Pile')
        self.players = []
        self.decks = []
        for i in range(1,self.num_of_decks+1):
            self.deck = Deck(False)
            self.deck.shuffle()

        dealer = Hand('Dealer')
        self.players.append(dealer)
        for i in range(self.num_of_players):
            j = i + 1
            label = 'Player %s' %(str(j))
            self.player = Hand(label)
            self.players.append(self.player)

    def deal(self):
        for i in range(2):
            j = 1
            while j <= self.num_of_players:
                self.deck.deal_card(self.players[j],1)
                j = j+1
            self.deck.deal_card(self.players[0],1)

    def __str__(self):
        return 'Current hands won: \n Dealer: %s \n Player 1: %s' %(str(self.scores[0]),str(self.scores[1]))
    
    def ace_check(self,s = 0,h = []):
        if s > 21:
            for i,val in enumerate(h):
                if val == 11:
                    val = 1
                    h[i] = val
        return h

    def blackjack_check(self,score,playernumber):
        if score == 21 and len(self.players[playernumber].deck_of_cards) == 2:
            score = 'Blackjack'
        return score

    def total_hand(self,playernumber):
        score = 0

        temp_hand_scores = []
        for card in self.players[playernumber].deck_of_cards:
            
            rank = card.rank
            rankname = card.rankname
            # print rank
            # print rankname

            if rankname == 'Jack' or rankname == 'Queen' or rankname == 'King' :
                rank = 10
            if rankname == 'Ace':
                rank = 11

            temp_hand_scores.append(rank)

        self.hand_scores[playernumber] = temp_hand_scores

        score = sum(self.hand_scores[playernumber])
        while score > 21 and 11 in self.hand_scores[playernumber]:
            newhand = self.ace_check(score,self.hand_scores[playernumber])
            self.hand_scores[playernumber] = newhand
            score = sum(self.hand_scores[playernumber])

        if playernumber == 0 and score >21:
            score = 0

        elif playernumber > 0 and score > 21:
            score = -1

        return score

    def play_round(self,num_of_rounds = 1):
        for k in range(num_of_rounds):
            if len(self.deck.deck_of_cards) < 26:
                self.discardpile.deal_card(self.deck,len(self.discardpile.deck_of_cards))

            self.deal()

            score1 = self.total_hand(1)
            while score1<17 and score1>0:
                self.deck.deal_card(self.players[1],1)
                score1 = self.total_hand(1)

            scoreDealer = self.total_hand(0)

            while scoreDealer<17 and scoreDealer>0:
                self.deck.deal_card(self.players[0],1)
                scoreDealer = self.total_hand(0)
        
            scoreDealer = self.blackjack_check(scoreDealer,0)
            score1 = self.blackjack_check(score1,1)

            if score1 == 'Blackjack' and scoreDealer != 'Blackjack':
                self.round_scores[1] = self.round_scores[1]+1.2

            elif score1 != 'Blackjack' and scoreDealer == 'Blackjack':
                self.round_scores[0] = self.round_scores[0]+1

            elif score1 == 'Blackjack' and scoreDealer == 'Blackjack':
                #tie
                ignore = 0

            elif scoreDealer>score1:
                self.round_scores[0] = self.round_scores[0]+1
                # print 'Dealer: %s \n Player1: %s \n Dealer Wins' %(str(scoreDealer),str(score1))
           
            elif scoreDealer<score1:
                self.round_scores[1] = self.round_scores[1]+1
                # print 'Dealer: %s \n Player1: %s \n Player1 Wins' %(str(scoreDealer),str(score1))
            
            #else:
                # print 'Dealer: %s \n Player1: %s \n Tie' %(str(scoreDealer),str(score1))

            # for i in range(len(self.players)):
            #     print i
            #     print self.players[i].deck_of_cards
            #     print self.hand_scores[i]
            #     if i == 0:
            #         print scoreDealer
            #     else:
            #         print score1

            for i in range(len(self.players)):
                # print self.players[i]
                cards_to_discard = len(self.players[i].deck_of_cards)
                self.players[i].deal_card(self.discardpile,cards_to_discard)

        # print self.round_scores