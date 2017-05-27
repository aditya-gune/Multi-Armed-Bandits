# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:16:07 2017

@author: adivt
"""

import numpy as np

class Bandit:
    def __init__(self, numarms, name = 'bandit'):
        self.numarms = numarms
        self.name = name
        self.reward = []
    
    def NumArms(self):
        return self.numarms
    
    def Pull(self, a):
        
        #TODO: Construct R matrix
        return 1

def SRBD(Bandit):
    def __init__(self, numarms, armrewards, name = 'bandit'):
        Bandit.__init__(self, numarms, name)
        self.armrewards = armrewards
        t = get_optimal_arm(armrewards)
        self.a_star = t[0]
        self.reward = t[1][0]*t[1][1]
        
        
    def get_optimal_arm(self, armrewards):
        a = np.argmax([r*p for (r,p) in armrewards])
        (r,p) = armrewards[a]
        return (a, (r,p))
    