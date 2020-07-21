# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:53:23 2020
Epsilon Greedy Method for Multi-Arm Bandit
@author: Aditya Ojha
"""
###Libraries Needed
from Bandit import Bandit
import random
import numpy as np


winrates = [0,.4,.6,.7]
bandits = []
for winrate in winrates:
    bandits.append(Bandit(winrate))
epsilons = [0.05,0.06,0.08,0.1]
win_list = []
for eps in epsilons:
    bandit_history = [[0,0],[0,0],[0,0],[0,0]]
    bandit_choose_frq = [0]*len(winrates)
    wins = 0
    best_bandit = 0 #guess that best bandit is zero
    for _ in range(int(1e6)):
        p = random.uniform(0,1)
        #print("p is " + str(p))
        if p<eps:
            band_choosen = random.randrange(0,len(bandits))
            bandit_choose_frq[band_choosen] +=1
            reward = bandits[band_choosen].pull_arm()
            wins+=reward
            bandit_history[band_choosen][0] += reward #increment total rewards
            bandit_history[band_choosen][1] += 1 #increment num of pulls
            #print("Exploring Randomly")
            #print("band_choosen " + str(band_choosen))
            #print("bandit_choose_frq "+ str(bandit_choose_frq))
            #print("bandit history " + str(bandit_history))
        else:
            win_percents = []
            for tup in bandit_history:
                try:
                    win_percents.append(tup[0]/tup[1])
                except(ZeroDivisionError):
                    win_percents.append(0)
            best_bandit = np.argmax(win_percents)
            bandit_choose_frq[best_bandit] +=1
            wins+=bandits[best_bandit].pull_arm()
            #print("Choosing best winrate")
            #print("best_bandit is "+ str(best_bandit))
            #print("Win %s are "+ str(win_percents))
        #x = input("Continue?")
    
    win_percents = []
    for tup in bandit_history:
        try:
            win_percents.append(tup[0]/tup[1])
        except(ZeroDivisionError):
            win_percents.append(0)
    print("Epsilon was " + str(eps))
    print("Win %s are "+ str(win_percents))
    print("bandit_choose_frq "+ str(bandit_choose_frq))
    print("Wins: "+ str(wins))
    win_list.append(wins)
print(epsilons)
print(win_list)