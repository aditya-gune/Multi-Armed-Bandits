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
        self.optimal_arm = random.randint(0, self.numarms)
        self.rewards_avg = [0] * numarms
    
    def Pull(self, bandit, a):
        reward = bandit.Pull(a)
        self.updateRewards(a, reward)
        return (a, reward)
    
    def NumArms(self):
        return self.numarms
    
    def updateRewards(self, a, reward):
        self. reward_accumulator [a] += reward
        self.pulls[a] += 1
        self.pulls_tot += 1
        self.rewards_avg = np.divide(self.reward_accumulator, self.pulls)
        
    
class IncrementalUniform(MultiArmedBandit):
    def calculateArmPull(self):
        a = self.pulls_tot % self.bandit.NumArms()
        return super.Pull(self.bandit, a)
    
class UCB(MultiArmedBandit):
    def calculateArmPull(self):
        if self.pulls_tot < self.numarms:
            #pull unpulled arms
            a = self.pulls_tot % self.numarms
        else:
            #get exploration term
            avg = self.rewards_avg
            x = np.log(self.pulls_tot)
            y = np.divide(x, self.pulls)
            epsilon = np.sqrt(y)
            a = np.argmax(avg + epsilon)
        
        return super.Pull(self.bandit, a)
    
#0.5-greedy by default
class EpsilonGreedy(MultiArmedBandit):
    def __init(self, bandit, epsilon = 0.5):
        self.epislon = epsilon
        self.bandit = bandit
    def calculateArmPull(self, a):
        numarms = self.numarms
        a_opt = self.optimal_arm
        if self.epsilon <= random.uniform(0,1):
            a = a_opt
        else:
            a_avail = list(range(numarms)).remove(a_opt)
            a = random.choose(a_avail)
            
        return super.Pull(self.bandit, a)
        
    
            
            
    
    