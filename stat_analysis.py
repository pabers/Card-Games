import matplotlib.pyplot as plt
import numpy as np
import Card_Decks as CD

num_of_points = 1000
num_of_rounds = 10000
statistical_data = []
player_winnings = []

for i in range(num_of_points):
	game = CD.Blackjack()
	game.play_round(num_of_rounds)
	statistical_data.append(game.round_scores)
	game.round_scores = [0,0]
	player_winnings.append(game.winnings)
	game.winnings = 0
	print str(float(i)/float(num_of_points)*100.0) + '% percent done'

print statistical_data

deal_win_rate = []
player_win_rate = []
players_wins = []

for i in range(num_of_points):
	dwr = float(statistical_data[i][0])/float(num_of_rounds)
	pwr = float(statistical_data[i][1])/float(num_of_rounds)
	deal_win_rate.append(dwr)
	player_win_rate.append(pwr)

	players_wins.append(statistical_data[i][1])


mean_dwr = np.mean(deal_win_rate)
std_dwr = np.std(deal_win_rate)
mean_pwr = np.mean(player_win_rate)
std_pwr = np.std(player_win_rate)

mean_winnings = np.mean(player_winnings)
std_winnings = np.std(player_winnings)

normal_dwr = np.random.normal(mean_dwr,std_dwr,10000)
normal_pwr = np.random.normal(mean_pwr,std_pwr,10000)

normal_winnings = np.random.normal(mean_winnings,std_winnings,10000)

FigWinRate = plt.figure(1)
plt.hist(normal_dwr,50,color = 'r',alpha =.5)
plt.hist(normal_pwr,50,color = 'b',alpha=.5)
plt.show()

FigWinnings = plt.figure(2)
plt.hist(normal_winnings,50)
plt.show()
