# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:58:21 2020
Bayesian Sampling
Demonstrates how to update the a and b values of a beta distribution
so that you converge on the population mean. 

The example given it that of a coin toss
@author: Aditya Ojha
"""
import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np
import random
from Bandit import Bandit
#below function copied from https://emredjan.github.io/blog/2017/07/19/plotting-distributions/?source=post_page-----c5ebaafdeedd----------------------
def plot_beta(x_range, a, b, mu=0, sigma=1, cdf=False, **kwargs):
    '''
    Plots the f distribution function for a given x range, a and b
    If mu and sigma are not provided, standard beta is plotted
    If cdf=True cumulative distribution is plotted
    Passes any keyword arguments to matplotlib plot function
    '''
    x = x_range
    if cdf:
        y = ss.beta.cdf(x, a, b, mu, sigma)
    else:
        y = ss.beta.pdf(x, a, b, mu, sigma)
    plt.plot(x, y, **kwargs)
x = np.linspace(0, 1, 5000)
#plot_beta(x, 5, 2, 0, 1, color='red', lw=2, ls='-', alpha=0.5, label='pdf')
#plt.legend();

#Function 'coinToss'
#inputs: 'percentHeads' = probability of getting heads with this coin (between 0 and 1)
#outputs: return of the coin toss
def coinToss(percentHeads):
    p = random.uniform(0,1)
    return 1 if p<=percentHeads else 0
winRates = [.1,.3,.5,.7]
bandits = []
band_frq = [0,0,0,0]
for winrate in winRates:
    bandits.append(Bandit(winrate))
plot_dict = dict()
for trial in range(10):
    a_list = [1,1,1,1]
    b_list = [1,1,1,1]
    mean_list = [1.0/(1.0 + (b/a)) for a,b in zip(a_list,b_list)]
    total_reward = 0
    reward_over_time = []
    for step in range(15000):
        bandit_choose = np.argmax(mean_list)
        band_frq[bandit_choose] += 1
        reward = bandits[bandit_choose].pull_arm() #get reward
        reward_over_time.append(reward)
        total_reward += reward #update total reward
        if reward == 1:
            a_list[bandit_choose]+=1
        else:
            b_list[bandit_choose]+=1
        #recalculate means
        mean_list = [1.0/(1.0 + (b/a)) for a,b in zip(a_list,b_list)]
        if step in plot_dict.keys():
            plot_dict[step].append(bandit_choose)
        else:
            plot_dict[step] = [bandit_choose]
bandit_choosen_time = []
for step in plot_dict.keys():
    band_cho = plot_dict[step]
    bands = [0,0,0,0]
    for element in band_cho:
        bands[element]+=1
    bandit_choosen_time.append(np.argmax(bands))
plt.plot(bandit_choosen_time,label = "Bandits choosen")
plt.title("Bandit Choosen over time (10 trials)")
plt.legend()
plt.show()

mu = .3 #define mean of the coin (aka the probability that the coin will land on heads)
ones = 0 #counts number of ones
zeros =0 #counts number of zeros
a = 1# 'a' value for beta distribution
b = 1# 'b' value for beta distribution
for step in range(150):
    result = coinToss(mu) #get the result of the toss
    if(result == 0):#update number of ones and zeros
        zeros+=1
    else:
        ones+=1
    a += ones#update 'a' and 'b'
    b += zeros
    if step%10 == 0: #every ten trials, print out the distribution. User pressed enter to continue 'training'
        mean = 1.0/(1.0 + (b/a))
        #plot_beta(x, a, b, 0, 1, color='red', lw=2, ls='-', alpha=0.5, label='Sample Mean of '+str(mean))
        #plt.title("True Mean = "+str(mu) + " Sample mean = " +str(mean))
        #plt.legend()
        #plt.show()
        #y = input("continue?")