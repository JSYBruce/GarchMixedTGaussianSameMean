# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:22:41 2022

@author: BruceKing
"""

import numpy as np
import matplotlib.pyplot as plt
# Import required packages
import pickle

with open('BTC_data', 'rb') as f:
        coin_df = pickle.load(f)
        
with open('sigma1_data', 'rb') as f:
        sigma1 = pickle.load(f)
     
with open('sigma2_data', 'rb') as f:
        sigma2 = pickle.load(f)
    
with open('Normalsigma_data', 'rb') as f:
        sigma3 = pickle.load(f)
     
with open("Standardized Student's tsigma_data", 'rb') as f:
        sigma4 = pickle.load(f)
        
        
with plt.style.context('vibrant'):
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size':30})
    date = coin_df.index[1:]
    ax.plot(date, np.sqrt(sigma3[::-1]), label="Normal Distribution", linewidth='3')
    ax.plot(date, np.sqrt(sigma4[::-1]), label="StudentsT Distribution", linewidth='3')
    ax.plot(date, np.sqrt(sigma1[::-1]), label="StudentsT Component in TN Distribution", linewidth='3')
    ax.plot(date, np.sqrt(sigma2[::-1]), label="Normal Component in TN Distribution", linewidth='3')
    plt.xticks(rotation = 45, fontsize=25) # Rotates X-Axis Ticks by 45-degrees
    plt.yticks(fontsize=25)
    ax.autoscale(tight=True)
    plt.title('Volatility of Three Models (Bitcoin)')
    ax.set_ylabel(r'Volatility',  size = 30)
    ax.set_xlabel(r'Time',  size = 30)  
    #ax.set(xlim=(0, 13), xticks=np.arange(0, 13 ,2),
    #ylim=(0, 120), yticks=np.arange(0, 120, 20))
    ax.legend()
    ax.grid(True)  # 设置背景网格线为虚线
    plt.figure()
#     plt.plot(x, y)
    fig.set_size_inches(50, 20)
    ax.autoscale(tight=True)
    fig.autofmt_xdate()
    fig.savefig("VolatilityBitcoinThreeModel.png", dpi=400)
    plt.show()
    