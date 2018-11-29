import matplotlib.pyplot as plt
import numpy as np
import Card_Decks_Sp as CD


num_of_points = 1000
num_of_rounds = 1000

case = [False,True]

stats = [[],[]]
for k in range(len(case)):
	statistical_data = []
	player_winnings = []
	blackjack_count = []
	deal_bust_count = []
	
	for i in range(num_of_points):
		game = CD.Blackjack(1,6,case[k],case[k],case[k],True)
		game.play_round(num_of_rounds)
		statistical_data.append(game.round_scores)
		game.round_scores = [0,0]
		player_winnings.append(game.winnings)
		game.winnings = 0.0
		blackjack_count.append(game.blackjack_count)
		game.blackjack_count = 0
		deal_bust_count.append(game.dealer_bust_count)
		game.dealer_bust_count = 0

		percent_done = float(i)/float(num_of_points)*100.0/float(len(case))+50.0*float(k)
		if percent_done%10 == 0:
			print str(percent_done)  + '% percent done'

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

	plt.figure(3)
	plt.hist(player_winnings,25)

	stats[k].append(mean_dwr)
	stats[k].append(std_dwr)
	stats[k].append(mean_pwr)
	stats[k].append(std_pwr)
	stats[k].append(mean_winnings)
	stats[k].append(std_winnings)

	mean_bjc = np.mean(blackjack_count)
	bj_rate = mean_bjc/num_of_rounds

	mean_dbc = np.mean(deal_bust_count)
	db_rate = mean_dbc/num_of_rounds
	print bj_rate*100
	print np.std(blackjack_count)/num_of_rounds
	print db_rate*100
	print np.std(deal_bust_count)/num_of_rounds


print stats[0]
print stats[1]