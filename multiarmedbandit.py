# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:59:24 2017

@author: adivt
"""

import numpy as np
import random

class MultiArmedBandit:
    def __init__(self, bandit):
        self.bandit = bandit
        self.numarms = bandit.NumArms()
        self.pulls_tot = 0
        self.pulls = [0] * self.numarms
        self.reward_accumulator = [0] * self.numarms
        self.optimal_arm = random.randing(0, self.numarms)
    
    def Pull(self):
        return 1
    
    def NumArms(self):
        return self.numarms
    
    def updateRewards(self, a, reward):
        self. reward_accumulator [a] += reward
        self.pulls[a] += 1
        self.pulls_tot += 1
        self.rewards_avg = np.divide(self.reward_accumulator, self.pulls)
        
    
class IncrementalUniform(MultiArmedBandit):
    def __init__(self, bandit):
        self.bandit = bandit
        self.numarms = bandit.NumArms()
        self.pulls_tot = 0
        self.pulls = [0] * self.numarms
        self.reward_accumulator = [0] * self.numarms
        self.optimal_arm = random.randing(0, numarms)
    
    def Pull(self):
        a = self.pulls_tot % self.bandit.NumArms()
        reward_a = self.bandit.Pull(a)
        self.updateRewards(a, reward_a)
        return (a, reward_a)
    
class UCB(MultiArmedBandit):
    def __init__(self, bandit):
        
        
        