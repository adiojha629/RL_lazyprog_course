# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:15:28 2020
Epsilon Greedy with Optimistic Initial Values
@author: Aditya Ojha
"""

###Libraries Needed
from Bandit import Bandit
import random
import numpy as np
import matplotlib.pyplot as plt

#####Set this value:
upperlimit = 20
###########
winrates = [0.1,.4,.6,.7]
bandits = []
for winrate in winrates:
    bandits.append(Bandit(winrate))
epsilons = [0.01,0.05,0.1,0]
win_list = []
total_time_steps = int(1e5)
for eps in epsilons:
    band_n = [0,0,0,0] #number of times each bandit was choosen
    if(eps == 0):
        win_avg = [upperlimit]*4 #win rate for each bandit based on experiences
    else:
        win_avg = [0,0,0,0]
    wins = 0 #total number of wins
    best_bandit = 0 #guess that best bandit is zero
    data =[]
    cum_avg = 0
    for _ in range(total_time_steps):
        p = random.uniform(0,1)
        band_choosen = None
        if p<eps:
            band_choosen = random.randrange(0,len(bandits))
        else:
            band_choosen = np.argmax(win_avg)
        reward = bandits[band_choosen].pull_arm() #pull the slot mach. arm
        data.append(reward)
        wins+=reward #update total wins
        band_n[band_choosen]+=1 #increment counter for this bandit
        n = band_n[band_choosen] #var created to make below line of code more readable
        win_avg[band_choosen] = (1-(1.0/n))*win_avg[band_choosen] + (1.0/n)*reward #update the avg. win
    cum_avg = np.cumsum(data) / (np.arange(total_time_steps)+1)
    plt.plot(cum_avg,label = "Cum. Avg for epsilon = " + str(eps))
    print("Epsilon was " + str(eps))
    print("win_avg " + str(win_avg))
    print("band_n "+ str(band_n))
    print("Wins: "+ str(wins))
    win_list.append(wins)
print(epsilons)
print(win_list)
plt.xscale('log')
plt.title(label = "(Optim) Cum. Avg for epsilons 0.01,0.05,0.1,Optimistic Values")
plt.legend()
plt.show()