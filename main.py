# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:12:34 2017

@author: adivt
"""

import numpy as np
import random
from bandit import Bandit, SRBD
from multiarmedbandit import *

DEBUG = True

#arms[i] = (r, p)
#r = reward
#p = probability of reward

#bandit 1
arms1 = [(0.05, 1)]*9
arms1.append((1, 0.1))
bandit1 = SRBD(arms1)
print(bandit1.numarms)


#bandit 2
arms2 = []
for i in range(1,20):
    arms2.append((i/20, 0.1))
    

   
pulls = 11
trials = 5
DEBUG = True
algodict = {}
def runtrials(bandit, pulls, trials):
    algodict = {}
    print('in runtrial')
    algodict['incremental'] = IncrementalUniform(bandit)
#    algodict['ucb'] = UCB(bandit)
#    algodict['epsilon'] = EpsilonGreedy(bandit)
    
    for a in algodict:
        print("\nRunning", a)
        a_opt = np.zeros(trials)
        r = 0
        for t in range(trials):
          print("Running trial", t)
          
          for p in range(pulls):
              arm = algodict[a].calculateArmPull()
              if DEBUG:
                  print(arm)
                  
    return algodict

#def getCumulativeReward():
    

algodict = runtrials(bandit1, pulls, trials)