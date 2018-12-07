# Card-Games
December 2, 2018
Code that allows a user to run simulations of blackjack gambling 

Personal project first began on November 15th.

Card_Decks_Sp contains four classes. A Card object, deck object, hand object (a child of deck) and Blackjack. The user can choose the number of decks, players, to use late surrender, to use count, to vary betting based on count, the random seed for shuffling, the penetration point (point at which deck is reshuffled) and if the dealer hits on soft 17. Multiplayer functionality is not currently set up and neither is the variations on basic strategy for deck size under 3. 

stat_analysis simulates many hands of blackjack to discover the statistical probabilities of various events in blackjack. The three main variables that a user can change are num_of_points, num_of_rounds, num_of_random_seeds and penetration point. Num_of_rounds sets the number of rounds to run for each point to find the final winnings the player has obtained. Note that in the latest version, only one set through the decks is allowed. Once a reshuffle happens, the rounds stops. This limits the rounds to a max of about 55 for a six deck shoe (the average amount of rounds until 6 decks were cleared). The number of points is how many times the set is played best on the original seed, and then all these points are averaged. Finally, the number of random seeds sets how many different original seeds are used. The total number of hands played equals the number of rounds*the number of points*the number of random seeds. The average winnings with and without a count and the standard deviations are stored in the variables wmc,wmnc,wsc,wsnc (winnings mean count, winnings mean no count etc). The length of the list of wmc and the rest is dependent on the length of the variable penetration point. The user can change this variable to see how penetration point effects the outcome of the counter's winnings. 

A word document file has been added to this repository as a basic and rough project report to explain and show the results of the code. The main takeawy is that counting cards (if the penetration point is deep enough) on a 6 deck hand results in an expected outcome of winning money. However, the margin is slim and the variance is large. It is not recommended to count cards to become a billionaire. A better method is possibly coding?
