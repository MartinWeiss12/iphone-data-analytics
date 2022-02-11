#!/usr/bin/env python3

#!/usr/bin/env python3

import pandas

import pandas as pd

import xlrd

import numpy as np

import numpy as geek

import matplotlib.pyplot as plt

import matplotlib

from matplotlib import pylab

from pylab import *

from matplotlib.colors import colorConverter

import operator

from operator import itemgetter

import math

from sklearn.linear_model import LinearRegression

# * * * * * DEC 11 * * * * *

dec11Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_12_11_T.xlsx')

dec11Sheet = pd.read_excel(dec11Path)

d11_8BLK = pd.DataFrame(dec11Sheet, columns = ['8 BLACK'])

d11_8GLD = pd.DataFrame(dec11Sheet, columns = ['8 GOLD'])

d11_8PBLK = pd.DataFrame(dec11Sheet, columns = ['8+ BLACK'])

d11_XBLK = pd.DataFrame(dec11Sheet, columns = ['X BLACK'])

d11_XSMGLD = pd.DataFrame(dec11Sheet, columns = ['XS MAX GOLD'])

d11_XRBLK = pd.DataFrame(dec11Sheet, columns = ['XR BLACK'])

d11_11PBLK = pd.DataFrame(dec11Sheet, columns = ['11 PRO BLACK'])

d11_11PMGRN = pd.DataFrame(dec11Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * DEC 18 * * * * *

dec18Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_12_18_T.xlsx')

dec18Sheet = pd.read_excel(dec18Path)

d18_8BLK = pd.DataFrame(dec18Sheet, columns = ['8 BLACK'])

d18_8GLD = pd.DataFrame(dec18Sheet, columns = ['8 GOLD'])

d18_8PBLK = pd.DataFrame(dec18Sheet, columns = ['8+ BLACK'])

d18_XBLK = pd.DataFrame(dec18Sheet, columns = ['X BLACK'])

d18_XSMGLD = pd.DataFrame(dec18Sheet, columns = ['XS MAX GOLD'])

d18_XRBLK = pd.DataFrame(dec18Sheet, columns = ['XR BLACK'])

d18_11PBLK = pd.DataFrame(dec18Sheet, columns = ['11 PRO BLACK'])

d18_11PMGRN = pd.DataFrame(dec18Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * DEC 25 * * * * *

dec25Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_12_25_T.xlsx')

dec25Sheet = pd.read_excel(dec25Path)

d25_8BLK = pd.DataFrame(dec25Sheet, columns = ['8 BLACK'])

d25_8GLD = pd.DataFrame(dec25Sheet, columns = ['8 GOLD'])

d25_8PBLK = pd.DataFrame(dec25Sheet, columns = ['8+ BLACK'])

d25_XBLK = pd.DataFrame(dec25Sheet, columns = ['X BLACK'])

d25_XSMGLD = pd.DataFrame(dec25Sheet, columns = ['XS MAX GOLD'])

d25_XRBLK = pd.DataFrame(dec25Sheet, columns = ['XR BLACK'])

d25_11PBLK = pd.DataFrame(dec25Sheet, columns = ['11 PRO BLACK'])

d25_11PMGRN = pd.DataFrame(dec25Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * JAN 01 * * * * *

jan01Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_01_01_T.xlsx')

jan01Sheet = pd.read_excel(jan01Path)

j01_8BLK = pd.DataFrame(jan01Sheet, columns = ['8 BLACK'])

j01_8GLD = pd.DataFrame(jan01Sheet, columns = ['8 GOLD'])

j01_8PBLK = pd.DataFrame(jan01Sheet, columns = ['8+ BLACK'])

j01_XBLK = pd.DataFrame(jan01Sheet, columns = ['X BLACK'])

j01_XSMGLD = pd.DataFrame(jan01Sheet, columns = ['XS MAX GOLD'])

j01_XRBLK = pd.DataFrame(jan01Sheet, columns = ['XR BLACK'])

j01_11PBLK = pd.DataFrame(jan01Sheet, columns = ['11 PRO BLACK'])

j01_11PMGRN = pd.DataFrame(jan01Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * JAN 08 * * * * *

jan08Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_01_08_T.xlsx')

jan08Sheet = pd.read_excel(jan08Path)

j08_8BLK = pd.DataFrame(jan08Sheet, columns = ['8 BLACK'])

j08_8GLD = pd.DataFrame(jan08Sheet, columns = ['8 GOLD'])

j08_8PBLK = pd.DataFrame(jan08Sheet, columns = ['8+ BLACK'])

j08_XBLK = pd.DataFrame(jan08Sheet, columns = ['X BLACK'])

j08_XSMGLD = pd.DataFrame(jan08Sheet, columns = ['XS MAX GOLD'])

j08_XRBLK = pd.DataFrame(jan08Sheet, columns = ['XR BLACK'])

j08_11PBLK = pd.DataFrame(jan08Sheet, columns = ['11 PRO BLACK'])

j08_11PMGRN = pd.DataFrame(jan08Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * JAN 15 * * * * *

jan15Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_01_15_T.xlsx')

jan15Sheet = pd.read_excel(jan15Path)

j15_8BLK = pd.DataFrame(jan15Sheet, columns = ['8 BLACK'])

j15_8GLD = pd.DataFrame(jan15Sheet, columns = ['8 GOLD'])

j15_8PBLK = pd.DataFrame(jan15Sheet, columns = ['8+ BLACK'])

j15_XBLK = pd.DataFrame(jan15Sheet, columns = ['X BLACK'])

j15_XSMGLD = pd.DataFrame(jan15Sheet, columns = ['XS MAX GOLD'])

j15_XRBLK = pd.DataFrame(jan15Sheet, columns = ['XR BLACK'])

j15_11PBLK = pd.DataFrame(jan15Sheet, columns = ['11 PRO BLACK'])

j15_11PMGRN = pd.DataFrame(jan15Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * JAN 22 * * * * *

jan22Path = ('/Users/martinweiss/Downloads/iPhone Glass Files/iphone_glass_stock_01_22_T.xlsx')

jan22Sheet = pd.read_excel(jan22Path)

j22_8BLK = pd.DataFrame(jan22Sheet, columns = ['8 BLACK'])

j22_8GLD = pd.DataFrame(jan22Sheet, columns = ['8 GOLD'])

j22_8PBLK = pd.DataFrame(jan22Sheet, columns = ['8+ BLACK'])

j22_XBLK = pd.DataFrame(jan22Sheet, columns = ['X BLACK'])

j22_XSMGLD = pd.DataFrame(jan22Sheet, columns = ['XS MAX GOLD'])

j22_XRBLK = pd.DataFrame(jan22Sheet, columns = ['XR BLACK'])

j22_11PBLK = pd.DataFrame(jan22Sheet, columns = ['11 PRO BLACK'])

j22_11PMGRN = pd.DataFrame(jan22Sheet, columns = ['11 PRO MAX GREEN'])

# * * * * * Setting Data to Arrays * * * * *

eight_black = [d11_8BLK, d18_8BLK, d25_8BLK, j01_8BLK, j08_8BLK, j15_8BLK, j22_8BLK]

eight_gold = [d11_8GLD, d18_8GLD, d25_8GLD, j01_8GLD, j08_8GLD, j15_8GLD, j22_8GLD]

eight_plus_black = [d11_8PBLK, d18_8PBLK, d25_8PBLK, j01_8PBLK, j08_8PBLK, j15_8PBLK, j22_8PBLK]

x_black = [d11_XBLK, d18_XBLK, d25_XBLK, j01_XBLK, j08_XBLK, j15_XBLK, j22_XBLK]

xs_max_gold = [d11_XSMGLD, d18_XSMGLD, d25_XSMGLD, j01_XSMGLD, j08_XSMGLD, j15_XSMGLD, j22_XSMGLD]

xr_black = [d11_XRBLK, d18_XRBLK, d25_XRBLK, j01_XRBLK, j08_XRBLK, j15_XRBLK, j22_XRBLK]

eleven_pro_black = [d11_11PBLK, d18_11PBLK, d25_11PBLK, j01_11PBLK, j08_11PBLK, j15_11PBLK, j22_11PBLK]

eleven_pro_max_green = [d11_11PMGRN, d18_11PMGRN, d25_11PMGRN, j01_11PMGRN, j08_11PMGRN, j15_11PMGRN, j22_11PMGRN]

weeks = [0, 1, 2, 3, 4, 5]

# * * * * * Striping Useless Data from Arrays * * * * *

eight_black = np.delete(eight_black, 0)

eight_gold = np.delete(eight_gold, 0)

eight_plus_black = np.delete(eight_plus_black, 0)

x_black = np.delete(x_black, 0)

xs_max_gold = np.delete(xs_max_gold, 0)

xr_black = np.delete(xr_black, 0)

eleven_pro_black = np.delete(eleven_pro_black, 0)

eleven_pro_max_green = np.delete(eleven_pro_max_green, 0)

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

print("Eight Black:")

print(eight_black)

print("Eight Black  Diff:")

print(eight_black_diff)

# * * * * * Eight Gold Math * * * * *

#print([1, 2, 1, 6, 0])

#print("mine^ below is computer")

eight_gold_empty = []

for i in range(len(eight_gold)):	
	
	math = eight_gold[i - 5] - eight_gold[i]
	
	eight_gold_empty.append(math)
	
eight_gold_empty = np.delete(eight_gold_empty, 5)

eight_gold_diff = [element * -1 for element in eight_gold_empty]

print("Eight Gold:")

print(eight_gold)

print("Eight Gold  Diff:")

print(eight_gold_diff)

# * * * * * Eight Plus Black Math * * * * *

eight_plus_black_empty = []

for i in range(len(eight_plus_black)):
	
	math = eight_plus_black[i - 5] - eight_plus_black[i]
	
	eight_plus_black_empty.append(math)
	
eight_plus_black_empty = np.delete(eight_plus_black_empty, 5)

eight_plus_black_diff = [element * -1 for element in eight_plus_black_empty]

print("Eight Plus Black:")

print(eight_plus_black)

print("Eight Plus Black  Diff:")

print(eight_plus_black_diff)


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

print("XS Max Gold:")

print(xs_max_gold)

print("XS Max Gold Diff:")

print(xs_max_gold_diff)

# * * * * * XR Black * * * * *

xr_black_empty = []

for i in range(len(xr_black)):
	
	math = xr_black[i - 5] - xr_black[i]
	
	xr_black_empty.append(math)
	
xr_black_empty = np.delete(xr_black_empty, 5)

xr_black_diff = [element * -1 for element in xr_black_empty]

print("XR Black:")

print(xr_black)

print("XR Black Diff:")

print(xr_black_diff)

# * * * * * 11 Pro Black * * * * *

eleven_pro_black_empty = []

for i in range(len(eleven_pro_black)):
	
	math = eleven_pro_black[i - 5] - eleven_pro_black[i]
	
	eleven_pro_black_empty.append(math)
	
eleven_pro_black_empty = np.delete(eleven_pro_black_empty, 5)

eleven_pro_black_diff = [element * -1 for element in eleven_pro_black_empty]

print("11 Pro Black:")

print(eleven_pro_black)

print("11 Pro Black Diff:")

print(eleven_pro_black_diff)

# * * * * * 11 Pro Max Green * * * * *

eleven_pro_max_green_empty = []

for i in range(len(eleven_pro_max_green)):
	
	math = eleven_pro_max_green[i - 5] - eleven_pro_max_green[i]
	
	eleven_pro_max_green_empty.append(math)
	
eleven_pro_max_green_empty = np.delete(eleven_pro_max_green_empty, 5)

eleven_pro_max_green_diff = [element * -1 for element in eleven_pro_max_green_empty]

print("11 Pro Max Green:")

print(eleven_pro_max_green)

print("11 Pro Max Green Diff:")

print(eleven_pro_max_green_diff)

# * * * * * Finding the Max and Min of the Math Analysis * * * * *

# * * * * * Eight Black Max/Min * * * * *

eight_black_max = max(eight_black_diff)

eight_black_min = min(eight_black_diff)

print("Eight Black Max:")

print(eight_black_max)

print("Eight Black Min:")

print(eight_black_min)

# * * * * * Eight Gold Max/Min * * * * *

eight_gold_max = max(eight_gold_diff)

eight_gold_min = min(eight_gold_diff)

print("Eight Gold Max:")

print(eight_gold_max)

print("Eight Gold Min:")

print(eight_gold_min)

# * * * * * Eight Plus Black Max/Min * * * * *

eight_plus_black_max = max(eight_plus_black_diff)

eight_plus_black_min = min(eight_plus_black_diff)

print("Eight Plus Black Max:")

print(eight_plus_black_max)

print("Eight Plus Black Min:")

print(eight_plus_black_min)

# * * * * * X Black Max/Min * * * * *

x_black_max = max(x_black_diff)

x_black_min = min(x_black_diff)

print("X Black Max:")

print(x_black_max)

print("X Black Min:")

print(x_black_min)

# * * * * * XS Max Gold Max/Min * * * * *

xs_max_gold_max = max(xs_max_gold_diff)

xs_max_gold_min = min(xs_max_gold_diff)

print("XS Max Gold Max:")

print(xs_max_gold_max)

print("XS Max Gold Min:")

print(xs_max_gold_min)

# * * * * * XS Max Gold Max/Min * * * * *

xs_max_gold_max = max(xs_max_gold_diff)

xs_max_gold_min = min(xs_max_gold_diff)

print("XS Max Gold Max:")

print(xs_max_gold_max)

print("XS Max Gold Min:")

print(xs_max_gold_min)

# * * * * * XR Black Max/Min * * * * *

xr_black_max = max(xr_black_diff)

xr_black_min = min(xr_black_diff)

print("XR Black Max:")

print(xr_black_max)

print("XR Black Min:")

print(xr_black_min)

# * * * * * 11 Pro Black Max/Min * * * * *

eleven_pro_black_max = max(eleven_pro_black_diff)

eleven_pro_black_min = min(eleven_pro_black_diff)

print("11 Pro Black Max:")

print(eleven_pro_black_max)

print("11 Pro Black Min:")

print(eleven_pro_black_min)

# * * * * * 11 Pro Max Green Max/Min * * * * *

eleven_pro_max_green_max = max(eleven_pro_max_green_diff)

eleven_pro_max_green_min = min(eleven_pro_max_green_diff)

print("11 Pro Max Green Max:")

print(eleven_pro_max_green_max)

print("11 Pro Max Green Min:")

print(eleven_pro_max_green_min)

# * * * * * Graphing Math Analysis * * * * *

# * * * * * 8 Black * * * * *

eight_black_index_array = np.array(eight_black)

eight_black_max_index = np.where(eight_black_index_array == eight_black_max)

print(eight_black_max_index)

plot(eight_black_max_index, eight_black_max, 'bo') 

# * * * * * 8 Gold * * * * *

eight_gold_index_array = np.array(eight_gold)

eight_gold_max_index = np.where(eight_gold_index_array == eight_gold_max)

print(eight_gold_max_index)

#plot(eight_gold_max_index, eight_gold_max, 'bo') 

# * * * * * 8 Plus Black * * * * *

eight_plus_black_index_array = np.array(eight_plus_black)

eight_plus_black_max_index = np.where(eight_plus_black_index_array == eight_plus_black_max)

print(eight_plus_black_max_index)

#plot(eight_plus_black_max_index, eight_plus_black_max, 'bo') 

# * * * * * X Black * * * * *

x_black_index_array = np.array(x_black)

x_black_max_index = np.where(x_black_index_array == x_black_max)

print(x_black_max_index)

plot(x_black_max_index, x_black_max, 'bo')

# * * * * * XR Black * * * * *

xr_black_index_array = np.array(xr_black)

xr_black_max_index = np.where(xr_black_index_array == xr_black_max)

print(xr_black_max_index)

plot(xr_black_max_index, xr_black_max, 'bo') 

plt.show()


