# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:14:40 2022

@author: BruceKing
"""

import numpy as np
import matplotlib.pyplot as plt
# Import required packages
import pickle
plt.style.use(['ieee'])

with open('sigma1_data', 'rb') as f:
        sigma1 = pickle.load(f)
     
with open('sigma2_data', 'rb') as f:
        sigma2 = pickle.load(f)
        
        
with open('BTC_data', 'rb') as f:
        coin_df = pickle.load(f)
        
with plt.style.context('vibrant'):
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size':30})
    date = coin_df.index[1:]
    ax.plot(date, np.sqrt(sigma1[::-1]), label="StudentsT Component", linewidth='4')
    ax.plot(date, np.sqrt(sigma2[::-1]), label="Guassian Component", linewidth='4')
    plt.xticks(rotation = 45, fontsize=25) # Rotates X-Axis Ticks by 45-degrees
    plt.yticks(fontsize=25)
    ax.autoscale(tight=True)
    plt.title('StudentsT + Guassian Model (Bitcoin)')
    ax.set_ylabel(r'Volatility',  size = 30)
    ax.set_xlabel(r'Time',  size = 30)  
    #ax.set(xlim=(0, 13), xticks=np.arange(0, 13 ,2),
    #ylim=(0, 120), yticks=np.arange(0, 120, 20))
    ax.legend()
    ax.grid(True)  # 设置背景网格线为虚线
    plt.figure()
#     plt.plot(x, y)
    fig.set_size_inches(40, 20)
    ax.autoscale(tight=True)
    fig.autofmt_xdate()
    fig.savefig("StudentsT + Guassian Model_sigma.png", dpi=400)
    plt.show()

