import matplotlib.pyplot as plt
import numpy as np
import Card_Decks_Sp as CD
reload(CD)
import random
import time

num_of_points = 1000
num_of_rounds = 100
num_of_random_seeds = 100
penetration_point = [.1,.25,.5,.75]
case = [False,True]

stats = [[],[]]
winnings_stats_mean =[[],[]]
winnings_stats_std = [[],[]]
random_seeds = []
random.seed(1)
for i in range(num_of_random_seeds):
	random_seeds.append(random.randint(1,1000))

total_stats = [[[] for i in range(num_of_random_seeds)] for j in range(len(penetration_point))]
for a in range(len(penetration_point)):
	for n in range(len(random_seeds)):
		initialtime = time.clock()
		for k in range(len(case)):
			reload(CD)
			statistical_data = []
			player_winnings = []
			blackjack_count = []
			deal_bust_count = []
			rounds_played = []
			game = CD.Blackjack(1,6,case[k],case[k],case[k],False,penetration_point[a],random_seeds[n])	
			for i in range(num_of_points):
				game.play_round(num_of_rounds)
				statistical_data.append(game.round_scores)
				player_winnings.append(game.winnings)
				blackjack_count.append(game.blackjack_count)
				deal_bust_count.append(game.dealer_bust_count)
				rounds_played.append(game.round_count[-1])
				game.reset()

				

				percent_done = (float(i)/float(num_of_points)*100.0/float(len(case))+50.0*float(k))/(float(num_of_random_seeds)-float(n))
				h = 1
				if percent_done%5 == 0:
					if h == 1 and percent_done!= 0.0:
						rate = (time.clock()-initialtime)/percent_done
						h = h+1
					if h>1:
						time_remaining = (100.0-percent_done)*rate*(num_of_random_seeds - n)
						print 'Time Remaining : ' + str(time_remaining)

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

			mean_rounds_played = np.mean(rounds_played)

			# normal_dwr = np.random.normal(mean_dwr,std_dwr,10000)
			# normal_pwr = np.random.normal(mean_pwr,std_pwr,10000)

			# normal_winnings = np.random.normal(mean_winnings,std_winnings,10000)

			# FigWinRate = plt.figure()
			# plt.hist(normal_dwr,50,color = 'r',alpha =.5)
			# plt.hist(normal_pwr,50,color = 'b',alpha=.5)
			# plt.show(block = False)

			# FigWinnings = plt.figure()
			# plt.hist(normal_winnings,50)
			# plt.show(block = False)

			# plt.figure()
			# plt.hist(player_winnings,25)

			mean_bjc = np.mean(blackjack_count)
			bj_rate = mean_bjc/num_of_rounds

			mean_dbc = np.mean(deal_bust_count)
			db_rate = mean_dbc/num_of_rounds

			mean_rounds = np.mean(rounds_played)

			stats[k].append(mean_dwr)
			stats[k].append(std_dwr)
			stats[k].append(mean_pwr)
			stats[k].append(std_pwr)
			stats[k].append(mean_winnings)
			stats[k].append(std_winnings)
			stats[k].append(mean_rounds)

		total_stats[a][n] = stats
		stats = [[],[]]

wmc = []
wmnc = []
wsc = []
wsnc = []

mean_count = []
mean_no_count = []

rpc = []
rpnc = []

for a in range(len(penetration_point)):
	tempn = []
	tempc = []
	for b in range(num_of_random_seeds):
		tempn.append(total_stats[a][b][0])
		tempc.append(total_stats[a][b][1])
	mean_count.append(np.mean(tempc,axis=0))
	mean_no_count.append(np.mean(tempn,axis=0))

	wmc.append(mean_count[a][4])
	wmnc.append(mean_no_count[a][4])
	wsc.append(mean_count[a][5])
	wsnc.append(mean_no_count[a][5])

	rpnc.append(mean_no_count[a][6])
	rpc.append(mean_count[a][6])

winnings_per_hand_count = [float(wmc[a])/float(rpc[a]) for a in range(len(penetration_point))]
std_per_hand_count = [float(wsc[a])/float(rpc[a]) for a in range(len(penetration_point))]

winnings_per_hand_no_count = [float(wmnc[a])/float(rpnc[a]) for a in range(len(penetration_point))]
std_per_hand_no_count = [float(wsnc[a])/float(rpnc[a]) for a in range(len(penetration_point))]

print winnings_per_hand_no_count
print std_per_hand_no_count

print winnings_per_hand_count
print std_per_hand_count