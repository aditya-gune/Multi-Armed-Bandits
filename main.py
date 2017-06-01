# -*- coding: utf-8 -*-
"""
ASSIGNMENT 5: MULTI-ARMED BANDITS
Aditya Gune
"""

import numpy as np
import random
from bandit import Bandit, SRBD
from multiarmedbandit import *
import csv


DEBUG = False

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
for i in range(0,20):
    arms2.append((i/20, 0.1))
bandit2 = SRBD(arms2)  
  
#bandit 3
arms3 = []
for i in range(10):
    arms3.append((0.1, 1))
for i in range(9):
    arms3.append((1, 0.5))
arms3.append((1, 0.01))
bandit3 = SRBD(arms3)

   
pulls = 100000
trials = 100
DEBUG = False
algodict = {}
def runtrials(bandit, pulls, trials, nidx):
    names = ['bandit1_', 'bandit2_', 'custombandit_']
    algodict = {}
    print('in runtrial')
    algodict['incremental'] = IncrementalUniform(bandit)
    algodict['ucb'] = UCB(bandit)
    algodict['epsilon'] = EpsilonGreedy(bandit)

    
    
    for key, a in algodict.items():
        
        file = names[nidx] + key + '.csv'
        opt_tuple = bandit.getOptimal()
        a_opt = opt_tuple[0]
        r_opt = opt_tuple[1][0] * opt_tuple[1][1]
        r = 0
        
        for t in range(trials):
#            print("\nTrial", t)
          
            best_arm = a.getOptimalArm()
            reward_current_best = 0
            reward_cumulative = 0
            cumulative_regret = 0
            simple_regret = 0
            n = 0
            f = open(file, 'w')
            writer = csv.writer(f, delimiter = ',')
            for p in range(pulls):
                
                pulled = a.calculateArmPull()
                n+=1
#                if DEBUG:
#                    print("\ncurrent best arm = ", best_arm)
#                    print("pulled", pulled)
                best_arm = a.getOptimalArm()
                reward_pulled = bandit.getArmReward(pulled[0])
                reward_current_best = bandit.getArmReward(best_arm)
                reward_cumulative += reward_pulled
                cumulative_regret = cumulativeRegret(r_opt, reward_current_best, reward_cumulative, n)
                simple_regret = simpleRegret(r_opt, reward_current_best)
                print("Cumulative Regret = ", cumulative_regret)
                print("Simple Regret = ", simple_regret)
#                if DEBUG:
#                    print("reward pulled", reward_pulled)
                writer.writerow([p, cumulative_regret, simple_regret])
            f.close()                
    nidx+=1
    return file

def cumulativeRegret(reward_opt, reward_current_best, reward_cumulative, n):
#    if DEBUG:
#        print(n, "*", reward_opt, "-", reward_cumulative)
    return n * reward_opt - reward_cumulative

def simpleRegret(reward_opt, reward_current_best):
    return reward_opt - reward_current_best

name = runtrials(bandit1, pulls, trials, 0)

name = runtrials(bandit2, pulls, trials, 1)

name = runtrials(bandit3, pulls, trials, 2)