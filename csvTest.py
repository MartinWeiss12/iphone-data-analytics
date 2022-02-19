#!/usr/bin/env python3

import pandas

import pandas as pd

import numpy as np

csvFile = pd.read_csv(r'/Users/martinweiss/Desktop/Python/iPhone_stock_data.csv')

eight_black = csvFile['8black'].tolist()

print (eight_black)

#eight_black = np.delete(eight_black, 0)

'''

model,dec11,dec18,dec25,jan01,jan08,jan15,jan22
8black,0,0,9,7,6,0,0
8gold,7,13,13,12,15,10,9
8pblack,0,6,1,0,14,6,6
xblack,0,9,0,0,17,8,5
xsmgold,3,5,0,0,31,16,16
xrblack,0,15,12,5,10,8,7
11pblack,2,35,32,30,30,22,22
11pmgreen,2,22,0,0,38,33,33

date,8black,8gold,8pblack,xblack,xsmgold,xrblack,11pblack,11pmgreen
dec11,0,7,0,0,3,0,2,2
dec18,0,13,6,9,5,15,35,22
dec25,9,13,1,0,0,12,32,0
jan01,7,12,0,0,0,5,30,0
jan08,6,15,14,17,31,10,30,38
kan15,0,10,6,8,16,8,22,33
jan2,0,9,6,5,16,7,22,33


'''