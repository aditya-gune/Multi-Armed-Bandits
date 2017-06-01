# -*- coding: utf-8 -*-
"""
Plots things. Run after main.py
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

f = []

def plotC(filename):
    data = np.loadtxt(filename, delimiter=',')
    print(data)
    cumulative = data[:,1]
    
    #pulls = data[:,0]
    
    plt.plot(cumulative)
    #plt.xticks(np.arange(0, len(cumulative), len(cumulative)/5))
    #plt.yticks(np.arange(0, np.ceil(max(cumulative)), 200))
    
    picname = filename[:-4] + '_cumulative.png'
    plt.savefig(picname)
    
def plotS(filename):
    data = np.loadtxt(filename, delimiter=',')
    simple = data[:,2]
    plt.plot(simple)
    plt.xticks(np.arange(0, len(simple), len(simple)/5))
    #plt.yticks(np.arange(0, np.ceil(max(simple))))
    picname = filename[:-4] + '_simple.png'
    plt.savefig(picname)
        
plotC('bandit2_epsilon.csv')
#plotS('bandit2_epsilon.csv')
