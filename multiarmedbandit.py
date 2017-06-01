# -*- coding: utf-8 -*-
"""
Multi-Armed Bandit to hold algorithms
-Incremental Uniform
-UCB
-Epsilon-Greedy
"""

import numpy as np
import random
DEBUG = False

np.seterr(divide='ignore', invalid='ignore')
class MultiArmedBandit:
    def __init__(self, bandit):
        self.bandit = bandit
        self.numarms = bandit.NumArms()
        self.pulls_tot = 0
        self.pulls = [0] * self.numarms
        self.reward_accumulator = [0] * self.numarms
        self.optimal_arm = random.randint(0, self.numarms)
        self.rewards_avg = [0] * self.numarms
    
    def getOptimalArm(self):
        return self.optimal_arm
    
    def Pull(self, bandit, a):
        reward = bandit.Pull(a)
        if DEBUG:
            print("Pulled", a, "for reward", reward)
        self.updateRewards(a, reward)
        return (a, reward)
    
    def NumArms(self):
        return self.numarms
    
    def updateRewards(self, a, reward):
        self.reward_accumulator [a] += reward
        self.pulls[a] += 1
        self.pulls_tot += 1            
        self.rewards_avg = np.divide(self.reward_accumulator, self.pulls)
        self.optimal_arm = np.argmax(self.rewards_avg)
    
class IncrementalUniform(MultiArmedBandit):
    def __init__(self, bandit):
        MultiArmedBandit.__init__(self, bandit)
        self.bandit = bandit
        if DEBUG:
            print("armrewards:\n",self.bandit.armrewards)
        
    def calculateArmPull(self):
        a = self.pulls_tot % self.bandit.NumArms()
        return self.Pull(self.bandit, a)
    
class UCB(MultiArmedBandit):
    def __init__(self, bandit):
        MultiArmedBandit.__init__(self, bandit)

        
    def calculateArmPull(self):
        if self.pulls_tot < self.numarms:
            #pull unpulled arms
            a = self.pulls_tot % self.numarms
        else:
            #get exploration term
            avg = self.rewards_avg
            x = np.log(self.pulls_tot)
            y = np.divide(x, self.pulls)
            beta = np.sqrt(y)
            a = np.argmax(avg + beta)
        return self.Pull(self.bandit, a)
    
#0.5-greedy by default
class EpsilonGreedy(MultiArmedBandit):
    def __init__(self, bandit, epsilon = 0.5):
        self.epsilon = epsilon
        MultiArmedBandit.__init__(self, bandit)
        self.bandit = bandit
    def calculateArmPull(self):
        numarms = self.numarms
        a_opt = self.optimal_arm
        if self.epsilon <= random.uniform(0,1):
            a = a_opt
        else:
            a_avail = list(range(numarms))
            a_avail.remove(a_opt) 
            a = random.choice(a_avail)
            
        return self.Pull(self.bandit, a)