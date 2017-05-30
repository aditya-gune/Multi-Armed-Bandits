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
        self.rewards_avg = [0] * numarms
    
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
    def Pull(self):
        a = self.pulls_tot % self.bandit.NumArms()
        reward_a = self.bandit.Pull(a)
        self.updateRewards(a, reward_a)
        return (a, reward_a)
    
class UCB(MultiArmedBandit):
    def Pull(self):
        if self.pulls_tot < self.numarms:
            #pull unpulled arms
            a = self.pulls_tot % self.numarms
        else:
            #get exploration term
            avg = self.rewards_avg
            x = np.log(self.pulls_tot)
            y = np.divide(n, self.pulls)
            epsilon = np.sqrt(y)
            a = np.argmax(avg + epsilon)
        
        reward = self.bandit.Pull(a)
        self.updateRewards(a, reward)
        return (a, reward)
    
