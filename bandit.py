# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:16:07 2017

@author: adivt
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
        t = self.getOptimal(armrewards)
        self.a_star = t[0]
        self.reward = t[1][0]*t[1][1]
    
    def getOptimal(self, armrewards):
        ta = []
        for (r,p) in armrewards:
            ta.append(r*p)
        a = np.argmax(ta)
        #a = np.argmax([r*p for (r,p) in armrewards])
        (r,p) = armrewards[a]
        return (a, (r,p))
    
    def Pull(self, a):
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
        
    