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
        return self.reward[a]