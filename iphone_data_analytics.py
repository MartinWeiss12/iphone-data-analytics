#!/usr/bin/env python3

#!/usr/bin/env python3

import pandas

import pandas as pd

import numpy as np

import matplotlib

import matplotlib.pyplot as plt

from matplotlib import pylab

from pylab import *

from matplotlib.colors import colorConverter

import math

from sklearn.linear_model import LinearRegression

# * * * * * Data Import * * * * *

csvFile = pd.read_csv(r'/Users/martinweiss/Desktop/Python/iPhone_stock_data.csv')

eight_black_list = csvFile['8black'].tolist()

eight_gold_list = csvFile['8gold'].tolist()

eight_plus_black_list = csvFile['8pblack'].tolist()

x_black_list = csvFile['xblack'].tolist()

xs_max_gold_list = csvFile['xsmgold'].tolist()

xr_black_list = csvFile['xrblack'].tolist()

eleven_pro_black_list = csvFile['11pblack'].tolist()

eleven_pro_max_green_list = csvFile['11pmgreen'].tolist()

# * * * * * Setting Lists to Arrays

eight_black = np.array(eight_black_list)

eight_gold = np.array(eight_gold_list)

eight_plus_black = np.array(eight_plus_black_list)

x_black = np.array(x_black_list)

xs_max_gold = np.array(xs_max_gold_list)

xr_black = np.array(xr_black_list)

eleven_pro_black = np.array(eleven_pro_black_list)

eleven_pro_max_green = np.array(eleven_pro_max_green_list)

weeks = [0, 1, 2, 3, 4, 5, 6]

# * * * * * Graphing * * * * *

plt.plot(weeks, eight_black, label = "8 Black")

plt.plot(weeks, eight_gold, label = "8 Gold")

plt.plot(weeks, eight_plus_black, label = "8 Plus Black")

plt.plot(weeks, x_black, label = "X Black")

plt.plot(weeks, xs_max_gold, label = "XS Max Gold")

plt.plot(weeks, xr_black, label = "XR Black")

plt.plot(weeks, eleven_pro_black, label = "11 Pro Black")

plt.plot(weeks, eleven_pro_max_green, label = "11 Pro Max Green")

plt.xlabel('Weeks From 12/11/20')

plt.ylabel('Glass Qty')

plt.legend(loc = 1)

fig = pylab.gcf()

fig.canvas.manager.set_window_title('iPhone Glass Stock Over Time')

eight_gold_list = ndarray.tolist(eight_gold)

# * * * * * * * * * * Math Analysis * * * * * * * * * *

# * * * * * Eight Black Math * * * * *

eight_black_empty = []

for i in range(len(eight_black)):	
	
	math = eight_black[i - 5] - eight_black[i]
	
	eight_black_empty.append(math)
	
eight_black_empty = np.delete(eight_black_empty, 5)

eight_black_diff = [element * -1 for element in eight_black_empty]

# * * * * * Eight Gold Math * * * * *

eight_gold_empty = []

for i in range(len(eight_gold)):	
	
	math = eight_gold[i - 5] - eight_gold[i]
	
	eight_gold_empty.append(math)
	
eight_gold_empty = np.delete(eight_gold_empty, 5)

eight_gold_diff = [element * -1 for element in eight_gold_empty]

# * * * * * Eight Plus Black Math * * * * *

eight_plus_black_empty = []

for i in range(len(eight_plus_black)):
	
	math = eight_plus_black[i - 5] - eight_plus_black[i]
	
	eight_plus_black_empty.append(math)
	
eight_plus_black_empty = np.delete(eight_plus_black_empty, 5)

eight_plus_black_diff = [element * -1 for element in eight_plus_black_empty]

# * * * * * X Black * * * * *

x_black_empty = []

for i in range(len(x_black)):
	
	math = x_black[i - 5] - x_black[i]
	
	x_black_empty.append(math)
	
x_black_empty = np.delete(x_black_empty, 5)

x_black_diff = [element * -1 for element in x_black_empty]

# * * * * * XS Max Gold * * * * *

xs_max_gold_empty = []

for i in range(len(xs_max_gold)):
	
	math = xs_max_gold[i - 5] - xs_max_gold[i]
	
	xs_max_gold_empty.append(math)
	
xs_max_gold_empty = np.delete(xs_max_gold_empty, 5)

xs_max_gold_diff = [element * -1 for element in xs_max_gold_empty]

# * * * * * XR Black * * * * *

xr_black_empty = []

for i in range(len(xr_black)):
	
	math = xr_black[i - 5] - xr_black[i]
	
	xr_black_empty.append(math)
	
xr_black_empty = np.delete(xr_black_empty, 5)

xr_black_diff = [element * -1 for element in xr_black_empty]

# * * * * * 11 Pro Black * * * * *

eleven_pro_black_empty = []

for i in range(len(eleven_pro_black)):
	
	math = eleven_pro_black[i - 5] - eleven_pro_black[i]
	
	eleven_pro_black_empty.append(math)
	
eleven_pro_black_empty = np.delete(eleven_pro_black_empty, 5)

eleven_pro_black_diff = [element * -1 for element in eleven_pro_black_empty]

# * * * * * 11 Pro Max Green * * * * *

eleven_pro_max_green_empty = []

for i in range(len(eleven_pro_max_green)):
	
	math = eleven_pro_max_green[i - 5] - eleven_pro_max_green[i]
	
	eleven_pro_max_green_empty.append(math)
	
eleven_pro_max_green_empty = np.delete(eleven_pro_max_green_empty, 5)

eleven_pro_max_green_diff = [element * -1 for element in eleven_pro_max_green_empty]

# * * * * * Finding the Max and Min of the Math Analysis * * * * *

# * * * * * Eight Black Max/Min * * * * *

eight_black_max = max(eight_black_diff)

eight_black_min = min(eight_black_diff)

# * * * * * Eight Gold Max/Min * * * * *

eight_gold_max = max(eight_gold_diff)

eight_gold_min = min(eight_gold_diff)

# * * * * * Eight Plus Black Max/Min * * * * *

eight_plus_black_max = max(eight_plus_black_diff)

eight_plus_black_min = min(eight_plus_black_diff)

# * * * * * X Black Max/Min * * * * *

x_black_max = max(x_black_diff)

x_black_min = min(x_black_diff)

# * * * * * XS Max Gold Max/Min * * * * *

xs_max_gold_max = max(xs_max_gold_diff)

xs_max_gold_min = min(xs_max_gold_diff)

# * * * * * XS Max Gold Max/Min * * * * *

xs_max_gold_max = max(xs_max_gold_diff)

xs_max_gold_min = min(xs_max_gold_diff)

# * * * * * XR Black Max/Min * * * * *

xr_black_max = max(xr_black_diff)

xr_black_min = min(xr_black_diff)

# * * * * * 11 Pro Black Max/Min * * * * *

eleven_pro_black_max = max(eleven_pro_black_diff)

eleven_pro_black_min = min(eleven_pro_black_diff)

# * * * * * 11 Pro Max Green Max/Min * * * * *

eleven_pro_max_green_max = max(eleven_pro_max_green_diff)

eleven_pro_max_green_min = min(eleven_pro_max_green_diff)

# * * * * * Graphing Math Analysis * * * * *

# * * * * * 8 Black * * * * *

eight_black_index_array = np.array(eight_black)

eight_black_max_index = np.where(eight_black_index_array == eight_black_max)

plot(eight_black_max_index, eight_black_max, 'bo') 

# * * * * * 8 Gold * * * * *

eight_gold_index_array = np.array(eight_gold)

eight_gold_max_index = np.where(eight_gold_index_array == eight_gold_max)

plot(eight_gold_max_index, eight_gold_max, 'bo') 

# * * * * * 8 Plus Black * * * * *

eight_plus_black_index_array = np.array(eight_plus_black)

eight_plus_black_max_index = np.where(eight_plus_black_index_array == eight_plus_black_max)

plot(eight_plus_black_max_index, eight_plus_black_max, 'bo') 

# * * * * * X Black * * * * *

x_black_index_array = np.array(x_black)

x_black_max_index = np.where(x_black_index_array == x_black_max)

plot(x_black_max_index, x_black_max, 'bo')

# * * * * * XR Black * * * * *

xr_black_index_array = np.array(xr_black)

xr_black_max_index = np.where(xr_black_index_array == xr_black_max)

plot(xr_black_max_index, xr_black_max, 'bo') 

plt.show()