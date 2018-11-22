import matplotlib.pyplot as plt
import numpy as np
import Card_Decks as CD

num_of_points = 100
num_of_rounds = 1000
statistical_data = []

for i in range(num_of_points):
	game = CD.Blackjack()
	game.play_round(num_of_rounds)
	statistical_data.append(game.round_scores)
	game.round_scores = [0,0]

print statistical_data

deal_win_rate = []
player_win_rate = []

for i in range(num_of_points):
	dwr = float(statistical_data[i][0])/float(num_of_rounds)
	pwr = float(statistical_data[i][1])/float(num_of_rounds)
	deal_win_rate.append(dwr)
	player_win_rate.append(pwr)

mean_dwr = np.mean(deal_win_rate)
std_dwr = np.std(deal_win_rate)
mean_pwr = np.mean(player_win_rate)
std_pwr = np.std(player_win_rate)

normal_dwr = np.random.normal(mean_dwr,std_dwr,10000)
normal_pwr = np.random.normal(mean_pwr,std_pwr,10000)

plt.hist(normal_dwr,50,color = 'r',alpha =.5)
plt.hist(normal_pwr,50,color = 'b',alpha=.5)

plt.show()