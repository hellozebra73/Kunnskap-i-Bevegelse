import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys
from numpy import sin, cos, tan, arctan, arccos, arcsin, sqrt, exp
from numpy import log as ln
from numpy import log10 as log



def display_axis(x,y,tick_spacing_x = 0.5,tick_spacing_y=5):
    ax = fig.add_subplot(1,1,1)
    ax.plot(x, y)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_x))
    ax.yaxis.set_ticks_position('left')
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_y))


fig = plt.figure()

if len(sys.argv)==2:
    x = np.linspace(-7, 7, 150)
    y = eval(sys.argv[1])
    display_axis(x,y)

if len(sys.argv)==3:
    xrang = [float(sys.argv[2].split(',')[0]), float(sys.argv[2].split(',')[1])] 
    x = np.linspace(xrang[0], xrang[1], 150)
    y = eval(sys.argv[1])
    display_axis(x,y)

if len(sys.argv)==4:
    xrang = [float(sys.argv[3].split(',')[0]), float(sys.argv[3].split(',')[1])] 
    x = np.linspace(xrang[0], xrang[1], 150)
    y1 = eval(sys.argv[1])
    y2 = eval(sys.argv[2])
    display_axis(x,y1)
    plt.hold('on')
    plt.plot(x,y2)

if len(sys.argv)==5:
    xrang = [float(sys.argv[4].split(',')[0]), float(sys.argv[4].split(',')[1])] 
    x = np.linspace(xrang[0], xrang[1], 150)
    y1 = eval(sys.argv[1])
    y2 = eval(sys.argv[2])
    y3 = eval(sys.argv[3])
    display_axis(x,y1)
    plt.hold('on')
    plt.plot(x,y2)
    plt.plot(x,y3)

plt.grid(True)
plt.show()

"""
Default command plots a given user expression over the interval x = [-7,7] with x and y-axis.
>> python matplot.py 'sin(x)'

Following command plots three linear functions over the interval x = [-9,9] with x and y-axis.
>> python matplot.py 'x+3' '-x+9' 'x-3' '-9,9'

"""
