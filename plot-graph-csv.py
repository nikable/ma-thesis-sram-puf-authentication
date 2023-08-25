import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

## Add name Devices to the first colum in the csv file
headers = ['Devices', 
           'Response-one',
           'Response-one-size (bytes)',
           'Response-two',
           'Response-two-size (bytes)',
           'Intra-Hamming Distance']

## load the csv in a data frame
df = pd.read_csv('/home/stark/thesis/sram/csv/test.csv', usecols=headers)
print (df)

## load the list of devices and their hamming distance with the initial response
response_set = df['Devices'].values
distance     = df['Intra-Hamming Distance'].values

## graph plotting
plt.plot(response_set, distance, color='black', linestyle='dashdot', linewidth = 1,
        marker='o', markerfacecolor='green', markersize=10)

## adjust the steps and graph appearance 
plt.xticks(np.arange(min(response_set), 51, 3))
plt.yticks(np.arange(0, max(distance)+0.13, 0.05))
plt.xlabel('Arduino Uno (ATmega328P microcontroller) SRAM responses in experiment', fontsize=10)
plt.ylabel('Fractional Hamming distance',fontsize=10)
plt.show()
