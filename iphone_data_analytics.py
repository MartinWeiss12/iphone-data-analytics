import pandas

import pandas as pd

import numpy as np

import matplotlib

import matplotlib.pyplot as plt

from matplotlib import pyplot

from matplotlib import pylab

from numpy import sin

from numpy import sqrt

from numpy import arange

from scipy.optimize import curve_fit

from pylab import *

from matplotlib.colors import colorConverter

import math

from sklearn.metrics import r2_score

from sklearn.cluster import KMeans

# * * * * * Data Import * * * * *

csvFile = pd.read_csv(r'/Users/martinweiss/Desktop/Python/iPhone_stock_data.csv') #CHANGE THIS TO YOUR PATH

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

weeks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,28,30,31,32,33,34,35,36,37]

# * * * * * Eight Black Regression * * * * *

eight_black_model = np.poly1d(np.polyfit(weeks, eight_black, 16))

eight_black_line = np.linspace(0, 38, 1000)

eight_black_r2 = str(r2_score(eight_black, eight_black_model(weeks)))

print("Eight Black R^2: " + eight_black_r2)

plt.plot(eight_black_line, eight_black_model(eight_black_line), label = "8 Black")

# * * * * * Eight Gold Regression * * * * *

eight_gold_model = np.poly1d(np.polyfit(weeks, eight_gold, 15))

eight_gold_line = np.linspace(0, 38, 1000)

eight_gold_r2 = str(r2_score(eight_gold, eight_gold_model(weeks)))

print("Eight Gold R^2: " + eight_gold_r2)

plt.plot(eight_gold_line, eight_gold_model(eight_gold_line), label = "8 Gold")

# * * * * * Eight Plus Black Regression * * * * *

eight_plus_black_model = np.poly1d(np.polyfit(weeks, eight_plus_black, 8))

eight_plus_black_r2 = str(r2_score(eight_plus_black, eight_plus_black_model(weeks)))

eight_plus_black_line = np.linspace(0, 38, 1000)

print("Eight Plus Black R^2: " + eight_plus_black_r2)

plt.plot(eight_plus_black_line, eight_plus_black_model(eight_plus_black_line), label = "8 Plus Black")

# * * * * * X Black Regression * * * * *

x_black_model = np.poly1d(np.polyfit(weeks, x_black, 8))

x_black_line = np.linspace(0, 38, 1000)

x_black_r2 = str(r2_score(x_black, x_black_model(weeks)))

print("X Black R^2: " + x_black_r2)

plt.plot(x_black_line, x_black_model(x_black_line), label = "X Black")

#* * * * * XS Max Gold Regression * * * * *

xs_max_gold_model = np.poly1d(np.polyfit(weeks, xs_max_gold, 11))

xs_max_gold_line = np.linspace(0, 38, 1000)

xs_max_gold_r2 = str(r2_score(xs_max_gold, xs_max_gold_model(weeks)))

print("XS Max Gold R^2: " + xs_max_gold_r2)

plt.plot(xs_max_gold_line, xs_max_gold_model(xs_max_gold_line), label = "XSM Gold")

# * * * * * XR Black Regression * * * * *

xr_black_model = np.poly1d(np.polyfit(weeks, xr_black, 8))

xr_black_line = np.linspace(0, 38, 1000)

xr_black_line_r2 = str(r2_score(xr_black, xr_black_model(weeks)))

print("XR Black R^2: " + xr_black_line_r2)

plt.plot(xr_black_line, xr_black_model(xr_black_line), label = "XR Black")

# * * * * * 11 Pro Black Regression * * * * *

eleven_pro_black_model = np.poly1d(np.polyfit(weeks, eleven_pro_black, 14))

eleven_pro_black_line = np.linspace(0, 38, 1000)

eleven_pro_black_r2 = str(r2_score(eleven_pro_black, eleven_pro_black_model(weeks)))

print("11 Pro Black R^2: " + eleven_pro_black_r2)

plt.plot(eleven_pro_black_line, eleven_pro_black_model(eleven_pro_black_line), label = "11 Pro Black")

# * * * * * 11 Pro Max Green Regression * * * * *

eleven_pro_max_green_model = np.poly1d(np.polyfit(weeks, eleven_pro_max_green, 13))

eleven_pro_max_green_line = np.linspace(0, 38, 1000)

eleven_pro_max_green_r2 = str(r2_score(eleven_pro_max_green, eleven_pro_max_green_model(weeks)))

print("11 Pro Max Green R^2: " + eleven_pro_max_green_r2)

plt.plot(eleven_pro_max_green_line, eleven_pro_max_green_model(eleven_pro_max_green_line), label = "11 Max Green")

# * * * * * Graph Window * * * * *

plt.xlabel('Weeks From 12/11/2020')

plt.ylabel('Glass Qty')

plt.legend(loc = 0)

fig = pylab.gcf()

fig.canvas.manager.set_window_title('iPhone Glass Stock Over Time')

plt.show()