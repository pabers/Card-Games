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
        if num == 1:
            card = self.pop_card()
            hand.add_card(card)
            cards_dealt = card

        else:
            cards_dealt = []
            for i in range(num):
                card = self.pop_card()
                hand.add_card(card)
                cards_dealt.append(card)

        return cards_dealt

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
    bet_tables_no_ace = []
    for row in range(22):
        if row >= 0 and row <=4:
            temp = ['Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit']
            bet_tables_no_ace.append(temp)
        elif row >= 5 and row <= 8:
            temp = ['Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit','Hit']
            bet_tables_no_ace.append(temp)
        elif row == 9:
            temp = ['Hit','Hit','Hit','Double','Double','Double','Double','Hit','Hit','Hit','Hit']
            bet_tables_no_ace.append(temp)
        elif row == 10:
            temp = ['Double','Hit','Double','Double','Double','Double','Double','Double','Double','Double','Hit']
            bet_tables_no_ace.append(temp)
        elif row == 11:
            temp = ['Double','Double','Double','Double','Double','Double','Double','Double','Double','Double','Double']
            bet_tables_no_ace.append(temp)
        elif row == 12:
            temp = ['Hit','Hit','Hit','Hit','Stand','Stand','Stand','Hit','Hit','Hit','Hit']
            bet_tables_no_ace.append(temp)
        elif row >= 13 and row <= 16:
            temp = ['Stand','Hit','Stand','Stand','Stand','Stand','Stand','Hit','Hit','Hit','Hit']
            bet_tables_no_ace.append(temp)
        elif row >= 17:
            temp = ['Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand']
            bet_tables_no_ace.append(temp)

    bet_tables_ace = []
    for row in range(14):
        if row >= 0 and row <=3:
            temp = ['Hit','Hit','Hit','Hit','Hit','Double','Double','Hit','Hit','Hit','Hit']
            bet_tables_ace.append(temp)
        elif row == 4 or row == 5:
            temp = ['Hit','Hit','Hit','Hit','Double','Double','Double','Hit','Hit','Hit','Hit']
            bet_tables_ace.append(temp)
        elif row == 6:
            temp = ['Hit','Hit','Hit','Double','Double','Double','Double','Hit','Hit','Hit','Hit']
            bet_tables_ace.append(temp)
        elif row == 7:
            temp = ['Hit','Hit','Double','Double','Double','Double','Double','Stand','Stand','Hit','Hit']
            bet_tables_ace.append(temp)
        elif row == 8:
            temp = ['Stand','Stand','Stand','Stand','Stand','Stand','Double','Stand','Stand','Stand','Stand']
            bet_tables_ace.append(temp)
        elif row >=9 and row <=13:
            temp = ['Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand']
            bet_tables_ace.append(temp)

    bet_tables_pairs = []
    for row in range(14):
        if row == 1 or row == 0:
            temp = ['Split','Split','Split','Split','Split','Split','Split','Split','Split','Split','Split']
            bet_tables_pairs.append(temp)
        elif row == 2 or row == 3:
            temp = ['Split','Hit','Split','Split','Split','Split','Split','Split','Hit','Hit','Hit']
            bet_tables_pairs.append(temp)
        elif row == 4:
            temp = ['Hit','Hit','Hit','Hit','Hit','Split','Split','Hit','Hit','Hit','Hit']
            bet_tables_pairs.append(temp)
        elif row == 5:
            temp = ['','','','','','','','','','','']
            bet_tables_pairs.append(temp)
        elif row == 6:
            temp = ['Split','Hit','Split','Split','Split','Split','Split','Hit','Hit','Hit','Hit']
            bet_tables_pairs.append(temp)
        elif row == 7:
            temp = ['Split','Hit','Split','Split','Split','Split','Split','Split','Hit','Hit','Hit']
            bet_tables_pairs.append(temp)
        elif row == 8:
            temp = ['Split','Split','Split','Split','Split','Split','Split','Split','Split','Split','Split']
            bet_tables_pairs.append(temp)
        elif row == 9:
            temp = ['Hit','Stand','Split','Split','Split','Split','Split','Stand','Split','Split','Stand']
            bet_tables_pairs.append(temp)
        elif row >= 10 and row <=13:
            temp = ['Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand','Stand']
            bet_tables_pairs.append(temp)

        surrender_table = []
        for row in range(22):
            empty = ['0','1','2','3','4','5','6','7','8','9','10']
            surrender_table.append(empty)
        #https://i0.wp.com/www.blackjackapprenticeship.com/wp-content/uploads/2018/08/BJA_Basic_Strategy.jpg

    def __init__(self,num_of_players = 1,num_of_decks = 6,use_surrender = True,use_count = True,use_count_multiplier = True,soft17hit = True): #,num_of_players=1,num_of_decks=1):        
        self.num_of_players = num_of_players
        self.num_of_decks = num_of_decks
        self.hand_scores = [ [[]] for i in range(self.num_of_players+1)]
        self.round_scores = [0,0]
        self.discardpile = Hand('Discard Pile')
        self.decks = []
        self.players = []
        self.did_double = [ [False] for i in range(self.num_of_players+1)]
        self.count = 0
        self.true_count = 0
        self.winnings = 0.0
        self.bet = 10.0
        self.count_multiplier = 1
        self.surrendered = [ [False] for i in range(self.num_of_players+1)]
        self.Insurance = False
        self.use_surrender_variable = use_surrender
        self.use_surrender(self.use_surrender_variable)
        self.blackjack_count = 0
        self.surrender_count = 0
        self.double_count = 0
        self.split_count = 0
        self.insurance_count = 0
        self.use_count = use_count
        self.use_count_multiplier = use_count_multiplier
        self.variations(self.true_count,self.use_count)
        self.dealer_bust_count = 0
        self.soft17hit = soft17hit
        self.soft17 = False
        self.prints = False

        self.deck = Deck(False)
        for i in range(self.num_of_decks-1):
            d = Deck(False)
            d.deal_card(self.deck,len(d.deck_of_cards))
            
        self.deck.shuffle()

        dealer = [Hand('Dealer')]
        self.players.append(dealer)
        for i in range(self.num_of_players):
            j = i + 1
            label = 'Player %s' %(str(j))
            self.player = [Hand(label)]
            self.players.append(self.player)

    def deal(self):

        for i in range(2):
            j = 1
            while j <= self.num_of_players:
                self.count_card(self.deck.deal_card(self.players[j][0],1))
                j = j+1

            self.deck.deal_card(self.players[0][0],1)



    def __str__(self):
        return 'Current hands won: \n Dealer: %s \n Player 1: %s' %(str(self.scores[0]),str(self.scores[1]))
    
    def ace_check(self,s = 0,h = []):
        if s > 21:
            for i,val in enumerate(h):
                if val == 11:
                    val = 1
                    h[i] = val
        return h

    def blackjack_check(self,score,playernumber,handnumber = 0):
        if len(self.players[playernumber]) == 1:
            if score == 21 and len(self.players[playernumber][handnumber].deck_of_cards) == 2:
                score = 'Blackjack'
            return score

    def total_hand(self,playernumber,handnumber = 0):
        score = 0

        temp_hand_scores = []
        for card in self.players[playernumber][handnumber].deck_of_cards:
            
            rankname = card.rankname
            # print rank
            # print rankname

            if rankname == 'Jack' or rankname == 'Queen' or rankname == 'King' :
                rank = 10
            elif rankname == 'Ace':
                rank = 11
            else:
                rank = card.rank

            temp_hand_scores.append(rank)

        self.hand_scores[playernumber][handnumber] = temp_hand_scores

        score = sum(self.hand_scores[playernumber][handnumber])
        while score > 21 and 11 in self.hand_scores[playernumber][handnumber]:
            newhand = self.ace_check(score,self.hand_scores[playernumber][handnumber])
            self.hand_scores[playernumber][handnumber] = newhand
            score = sum(self.hand_scores[playernumber][handnumber])
        
        if score == 17 and 11 in self.hand_scores[0][0] and playernumber == 0:
            self.soft17 = True
            # print score
            # print self.soft17
            # print self.players[0]
            # self.prints = True

        if playernumber == 0 and score >21:
            score = 0

        elif playernumber > 0 and score > 21:
            score = -1

        return score

    def play_round(self,num_of_rounds = 1):
        for k in range(num_of_rounds):

            if self.use_count_multiplier == True:
                if self.num_of_decks == 1:
                    if self.true_count <= 1:
                        self.count_multiplier = 1.0
                    elif self.true_count == 2:
                        self.count_multiplier = 2.0
                    elif self.true_count == 3:
                        self.count_multiplier = 3.0
                    elif self.true_count >= 4:
                        self.count_multiplier = 4.0

                elif self.num_of_decks == 2: 
                    if self.true_count <= 1:
                        self.count_multiplier = 1.0
                    elif self.true_count == 2:
                        self.count_multiplier = 2.0
                    elif self.true_count == 3:
                        self.count_multiplier = 3.0
                    elif self.true_count == 4:
                        self.count_multiplier = 4.0
                    elif self.true_count == 5:
                        self.count_multiplier = 5.0
                    elif self.true_count >= 6:
                        self.count_multiplier = 6.0 
                elif self.num_of_decks >=3: 
                    if self.true_count <= 1:
                        self.count_multiplier = 1.0
                    elif self.true_count == 2:
                        self.count_multiplier = 2.0
                    elif self.true_count == 3:
                        self.count_multiplier = 4.0
                    elif self.true_count == 4:
                        self.count_multiplier = 8.0
                    elif self.true_count >= 5:
                        self.count_multiplier = 12.0
                      
            else:
                self.count_multiplier = 1.0
            # print 'count is currrently : ' + str(self.count)
            # print 'count multiplier is : ' + str(self.count_multiplier)

            if len(self.deck.deck_of_cards) < 26:
                self.discardpile.deal_card(self.deck,len(self.discardpile.deck_of_cards))
                self.deck.shuffle()
                self.count = 0
                self.true_count = 0
                # print 'count reset : ' + str(self.count)
            self.deal()

            self.dealer_shows = self.players[0][0].deck_of_cards[1]
            self.count_card(self.dealer_shows)

            self.check_insurance(self.dealer_shows)

            scoreDealer = self.total_hand(0,0)
            score1 = self.total_hand(1,0)
            scoreDealer = self.blackjack_check(scoreDealer,0,0)
            score1 = self.blackjack_check(score1,1,0)
            
            splitblackpossible = False

            if self.players[1][0].deck_of_cards[1] == self.players[0][0].deck_of_cards[0] \
            and (
                self.players[1][0].deck_of_cards[1].rank == 10 \
                or self.players[1][0].deck_of_cards[1].rank == 1
                ):
                splitblackpossible = True
            

            skip = False
            if scoreDealer == 'Blackjack' and splitblackpossible == False:
                skip = True
            if score1 == 'Blackjack':
                skip = True

            if skip == False:
                self.variations(self.true_count,self.use_count)
                ace_split = self.check_split(1)
                for n in range(len(self.players[1])):
                    score1 = score1 = self.total_hand(1,n)
                    self.variations(self.true_count,self.use_count)
                    strat1 = self.strategy(1,n,score1)
                    if strat1 == 'Surrender' and ace_split == False:
                        self.action(strat1,1,n)
                        self.surrendered[1][n] = True

                    while strat1 != 'Stand' and self.surrendered[1][n] == False and ace_split == False:
                        if strat1 == 'Double':
                            self.action(strat1,1,n)
                            break
                        self.action(strat1,1,n)
                        score1 = self.total_hand(1,n)
                        self.variations(self.true_count,self.use_count)
                        strat1 = self.strategy(1,n,score1)

                if self.soft17hit == False:    
                    while scoreDealer<17 and scoreDealer>0 and score1 != -1:
                        self.count_card(self.deck.deal_card(self.players[0][0],1))
                        scoreDealer = self.total_hand(0,0)

                    if scoreDealer == 0:
                        self.dealer_bust_count = self.dealer_bust_count + 1
                elif self.soft17hit == True:
                    while ((scoreDealer<17 and scoreDealer>0) or self.soft17 == True)and score1 != -1 :
                        if self.soft17 == True:
                            self.soft17 = False
                        self.count_card(self.deck.deal_card(self.players[0][0],1))
                        scoreDealer = self.total_hand(0,0)

                    if scoreDealer == 0:
                        self.dealer_bust_count = self.dealer_bust_count + 1

            for n in range(len(self.players[1])):
                score1 = self.total_hand(1,n)
                score1 = self.blackjack_check(score1,1,0)

                if score1 == 'Blackjack' and scoreDealer != 'Blackjack':
                    self.round_scores[1] = self.round_scores[1]+1
                    self.winnings = self.winnings + 1.5*self.bet*self.count_multiplier
                    self.blackjack_count = self.blackjack_count+1

                elif score1 != 'Blackjack' and scoreDealer == 'Blackjack':
                    self.round_scores[0] = self.round_scores[0]+1
                    self.winnings = self.winnings - self.bet*self.count_multiplier*(1.0-self.Insurance)

                elif score1 == 'Blackjack' and scoreDealer == 'Blackjack':
                    #tie
                    self.blackjack_count = self.blackjack_count+1

                elif self.surrendered[1][n] == True:
                    self.round_scores[0] = self.round_scores[0]+1
                    self.winnings = self.winnings - self.bet*self.count_multiplier*0.5
                
                elif scoreDealer>score1:
                    self.round_scores[0] = self.round_scores[0]+1
                    self.winnings = self.winnings - self.bet*(self.did_double[1][n] * 1.0 + 1.0)*self.count_multiplier
                    # print 'Dealer: %s \n Player1: %s \n Dealer Wins' %(str(scoreDealer),str(score1))
               
                elif scoreDealer<score1:
                    self.round_scores[1] = self.round_scores[1]+1
                    self.winnings = self.winnings + self.bet*(self.did_double[1][n] * 1.0 + 1.0)*self.count_multiplier
                
                # print 'Dealer: %s \n Player1: %s \n Player1 Wins' %(str(scoreDealer),str(score1))

            #else:
                # print 'Dealer: %s \n Player1: %s \n Tie' %(str(scoreDealer),str(score1))
            # if self.prints == True:
            #     print self.players[0]
            #     self.prints = False
            #     print ' '
            #     print ' '
            # for i in range(len(self.players)):
            #     print i
            #     print self.players[i].deck_of_cards
            #     print self.hand_scores[i]
            #     if i == 0:
            #         print scoreDealer
            #     else:
            #         print score1
            # print ' '
            # print self.players[1].deck_of_cards
            # print 'score1 : ' + str(score1)
            # print self.players[0].deck_of_cards
            # print 'score Dealer : ' + str(scoreDealer)
            # print 'Dealer : ' + str(self.total_hand(0,0))
            # for n in range(len(self.players[1])):
            #     print 'Player 1, Hand ' + str(n) + ' ' + str(self.total_hand(1,n))
            # print self.winnings


            for i in range(len(self.players)):
                # print self.players[i]
                for n in range(len(self.players[i])):
                    cards_to_discard = len(self.players[i][n].deck_of_cards)
                    self.players[i][n].deal_card(self.discardpile,cards_to_discard)
                
                while len(self.players[i]) > 1:
                    self.players[i].pop()
                    self.hand_scores[i].pop()
                    self.did_double[i].pop()
                    self.surrendered[i].pop()

                self.did_double[i][0] = False
                self.surrendered[1][0] = False



        # print self.round_scores
        # print self.winnings

    def strategy(self,playernumber,handnumber = 0,score = -1):
        deal_shows_rank = self.dealer_shows.rank
        if deal_shows_rank >= 10:
            deal_shows = 10
        else:
            deal_shows = deal_shows_rank

        strat = ''

        if len(self.players[playernumber][handnumber].deck_of_cards) == 2 and self.use_surrender_variable == True:
            strat = Blackjack.surrender_table[score][deal_shows]

        if strat ==  'Surrender':
            stophere = True
            # print self.players
            self.surrender_count = self.surrender_count+1

        elif len(self.players[playernumber][handnumber].deck_of_cards) == 2 \
        and (self.players[playernumber][handnumber].deck_of_cards[0].rank == \
            self.players[playernumber][handnumber].deck_of_cards[1].rank ) \
        and (self.players[playernumber][handnumber].deck_of_cards[0].rank != 5):
                strat = Blackjack.bet_tables_pairs_var[self.players[playernumber][handnumber].deck_of_cards[0].rank][deal_shows] 
        
        elif 11 in self.hand_scores[playernumber][handnumber]:
            no_ace_score = score - 11
            # print 'no ace score ' + str(no_ace_score)
            strat = Blackjack.bet_tables_ace[no_ace_score][deal_shows]

        elif score <= 17:
            strat = Blackjack.bet_tables_no_ace_var[score][deal_shows]
            
        else:
            strat = 'Stand'

        if strat == 'Double':
            if len(self.players[playernumber][handnumber].deck_of_cards) == 2:
                strat = 'Double'
            else:
                strat = Blackjack.bet_tables_no_ace_var[score][deal_shows]
                if strat == 'Double':
                    strat = 'Hit'

        # print self.players[playernumber].deck_of_cards
        # print 'score of player' + str(playernumber) + ' ' + str(score)
        # print 'dealer shows ' + str(deal_shows)
        # print strat
        return strat

    def count_card(self, card):

        if card.rank <=6 and card.rank>= 2:
            self.count = self.count+1
        elif card.rank == 1 or card.rank>=10:
            self.count = self.count-1

        if self.num_of_decks > 2:
            cards_remaining = float(len(self.deck.deck_of_cards))
            decks_remaining = cards_remaining/52.0
            tr_count = float(self.count)/decks_remaining
            self.true_count = int(tr_count)

        elif self.num_of_decks > 0 and self.num_of_decks <= 2:
            self.true_count = self.count

        # print ' '
        # print cards_remaining
        # print decks_remaining
        # print self.count
        # print tr_count
        # print self.true_count



    def action(self,move,playernumber,handnumber = 0):
        # print move

        if move == 'Hit':
            # print 'hitting'
            self.count_card(self.deck.deal_card(self.players[playernumber][handnumber],1))
        
        elif move == 'Double':
            self.count_card(self.deck.deal_card(self.players[playernumber][handnumber],1))
            self.did_double[playernumber][handnumber] = True
            self.double_count = self.double_count+1
            # print 'Doubling'

        elif move == 'Split':
            newhand = Hand('splithand')
            self.players[playernumber].append(newhand)
            self.players[playernumber][handnumber].deal_card(self.players[playernumber][-1],1)
            self.deck.deal_card(self.players[playernumber][handnumber],1)
            self.deck.deal_card(self.players[playernumber][-1],1)
            self.hand_scores[playernumber].append([])
            self.did_double[playernumber].append(False)
            self.surrendered[playernumber].append(False)
            self.split_count = self.split_count+1



    def check_split(self,playernumber):
        hand_strategies = []
        did_split = False
        for handnumber in range(len(self.players[playernumber])):
            score = self.total_hand(playernumber,handnumber)
            strat = self.strategy(playernumber,handnumber,score)
            hand_strategies.append(strat)

        if 'Split' in hand_strategies:
            for handnumber in range(len(self.players[playernumber])):
                score = self.total_hand(playernumber,handnumber)
                strat = self.strategy(playernumber,handnumber,score)
                if strat == 'Split':
                    self.action('Split',playernumber,handnumber)

            self.check_split(playernumber)
            did_split =True
        if did_split == True and self.players[playernumber][0].deck_of_cards[0].rank == 1:
            ace_split = True
            return ace_split
        else:
            ace_split = False
            return ace_split

    def check_insurance(self,dealer_shows,playernumber = 1):
        deal_shows_rank = dealer_shows.rank

        if deal_shows_rank == 1 and self.true_count >= 3 and self.use_count == True:
            self.Insurance = True
            self.winnings = self.winnings - 0.3*self.bet
            self.insurance_count = self.insurance_count+1

            

    def use_surrender(self,use_surrender):
        if use_surrender == True:
            Blackjack.surrender_table[16][1] = 'Surrender'
            Blackjack.surrender_table[16][9] = 'Surrender'
            Blackjack.surrender_table[16][10] = 'Surrender'
            Blackjack.surrender_table[15][10] = 'Surrender'
            # Blackjack.bet_tables_pairs[8][1] = 'Surrender'
            # Blackjack.bet_tables_pairs[8][9] = 'Surrender'
            # Blackjack.bet_tables_pairs[8][10] = 'Surrender'

    def variations(self,count,use):
    
        Blackjack.bet_tables_no_ace_var = np.copy(Blackjack.bet_tables_no_ace)
        Blackjack.bet_tables_pairs_var = np.copy(Blackjack.bet_tables_pairs)
        if use == True:
            for i in range(count+1):
                if count == 8:
                    donothing = True
                elif count == 7:
                    donothing =True
                elif count == 6:
                    donothing = True
                elif count == 5:
                    Blackjack.bet_tables_pairs_var[10][5] = 'Split'
                    Blackjack.bet_tables_no_ace_var[16][9] = 'Stand'
                elif count == 4:
                    Blackjack.bet_tables_pairs_var[10][6] = 'Split'
                    Blackjack.bet_tables_no_ace_var[15][10] = 'Stand'
                    Blackjack.bet_tables_no_ace_var[10][10] = 'Double'
                    Blackjack.bet_tables_no_ace_var[10][1] = 'Double'
                elif count == 3:
                    Blackjack.bet_tables_no_ace_var[12][2] = 'Stand'
                    Blackjack.bet_tables_no_ace_var[9][7] = 'Double'
                elif count == 2:
                    Blackjack.bet_tables_no_ace_var[12][3] = 'Stand' 
                elif count == 1:
                    Blackjack.bet_tables_no_ace_var[11][1] = 'Double'
                    Blackjack.bet_tables_no_ace_var[9][2] = 'Double'
                elif count == 0:
                    Blackjack.bet_tables_no_ace_var[12][4] = 'Stand'
                    Blackjack.bet_tables_no_ace_var[16][10] = 'Stand'
                elif self.true_count == -1:
                    Blackjack.bet_tables_no_ace_var[13][2] = 'Stand'
                    Blackjack.bet_tables_no_ace_var[12][6] = 'Stand'
                elif self.true_count <= -2:
                    Blackjack.bet_tables_no_ace_var[12][5] = 'Stand'
                    Blackjack.bet_tables_no_ace_var[13][3] = 'Stand'
