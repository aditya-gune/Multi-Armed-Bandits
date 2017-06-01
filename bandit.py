# -*- coding: utf-8 -*-
"""
Bandit base class
Scaled Binomial Reward Dist. class
Forms bandit API for solution algorithms
"""

import numpy as np
import random
DEBUG = False

class Bandit:
    def __init__(self, armrewards):
        self.numarms = len(armrewards)
        self.reward = []
    
    def NumArms(self):
        return self.numarms
    
class SRBD(Bandit):  
    def __init__(self, armrewards):
        self.numarms = len(armrewards)
        self.armrewards = armrewards
        t = self.getOptimal()
        self.a_star = t[0]
        self.reward = t[1][0]*t[1][1]
    
    def getOptimal(self):
        ta = []
        for (r,p) in self.armrewards:
            ta.append(r*p)
        a = np.argmax(ta)
        (r,p) = self.armrewards[a]
        return (a, (r,p))
    
    def Pull(self, a):
        if a > len(self.armrewards):
            return
        (r, p) = self.armrewards[a]
        rand = random.uniform(0,1)
        if p > rand:
            if DEBUG:
                print("p = ", p, "<=", rand)
                print("got reward", r)
            return r
        else:
            if DEBUG:
                print("p = ", p, ">", rand)
            return 0
        
    def getArmReward(self, a):
        (r, p) = self.armrewards[a]
        return r*p