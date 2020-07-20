# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:53:23 2020
Epsilon Greedy Method for Multi-Arm Bandit
@author: Aditya Ojha
"""
from Bandit import Bandit
import random
import numpy as np
winrates = [0,.4,.6,.7]
bandits = []
bandit_history = [[0,0]]*len(winrates)
bandit_choose_frq = [0]*len(winrates)
for winrate in winrates:
    bandits.append(Bandit(winrate))
wins = 0
best_bandit = 3 #guess that best bandit is zero
#set to zero as an initial guess
epsilons = [0.05,0.06,0.08,0.1]
for _ in range(100):
    eps = 0.1
    p = random.uniform(0,1)
    if p<eps:
        band_choosen = random.randrange(0,len(bandits))
        bandit_choose_frq[band_choosen] +=1
        reward = bandits[band_choosen].pull_arm()
        wins+=reward
        bandit_history[band_choosen][0] += reward #increment total rewards
        bandit_history[band_choosen][1] += 1 #increment num of pulls
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
win_percents = []
for tup in bandit_history:
    try:
        win_percents.append(tup[0]/tup[1])
    except(ZeroDivisionError):
        win_percents.append(0)
print(win_percents)
print(bandit_choose_frq)
print(wins)
