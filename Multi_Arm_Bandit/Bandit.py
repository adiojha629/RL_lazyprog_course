# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:43:55 2020
Multi-Arm Bandit
@author: Aditya Ojha
"""
import random
#MultiArm Bandit Class
class Bandit():
    def __init__(self,winrate):
        assert(winrate>=0 and winrate<=1)
        self.winrate = winrate
    def pull_arm(self) -> int:
        return 0 if random.uniform(0,1)>self.winrate else 1
    def __str__(self):
        return"I am a bandit with winrate " + str(self.winrate)
'''
x = Bandit(0)
counter = 0
for _ in range(100):
    counter += x.pull_arm()
print(counter/100)
'''