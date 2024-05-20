import os, sys
syspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace(os.sep, '/')
if syspath not in sys.path:
    sys.path.append(syspath)

import matplotlib.pyplot as plt
from itertools import cycle
from log_utils import WARNING, INFO

def set_custom_rcparams(grid=True):
    """
    custom rcparams
    """
    plt.rcParams['axes.grid'] = grid
    #plt.rcParams['image.cmap'] = 'viridis_r'
    #plt.rc('font', size=12)
    ## Set the axes title font size
    #plt.rc('axes', titlesize=16)
    ## Set the axes labels font size
    #plt.rc('axes', labelsize=14)
    ## Set the font size for x tick labels
    #plt.rc('xtick', labelsize=12)
    ## Set the font size for y tick labels
    #plt.rc('ytick', labelsize=12)
    ## Set the legend font size
    #plt.rc('legend', fontsize=10)
    ## Set the font size of the figure title
    #plt.rc('figure', titlesize=16)

def make_iterator(prop_cycle:list):
    return cycle(prop_cycle)

def color_cycler():
    prop_cycle = plt.rcParams['axes.prop_cycle']
    return make_iterator(prop_cycle.by_key()['color'])

def linestyle_cycler():
    return make_iterator([
        ((0, (1,1))),
        ((0, (3,1))),
        ((0, (3,2, 1,2))),
        ((0, (3,1, 1,1, 1,1))),

        ((0, (1,3))),
        ((0, (3,3))),
        ((0, (6,2, 3,2))),
        ((0, (6,1, 2,1, 2,1))),
    ])

def fig2png(fig:plt.Figure, png_path:str, display:bool=True):
    _path = os.path.abspath(png_path).replace(os.sep, '/')
    _path = f"{os.path.splitext(_path)[0]:s}.png"
    if not os.path.isdir(os.path.dirname(_path)):
        WARNING(f"{os.path.dirname(_path):s} does not exist. PNG was not saved.")
        return _path
    fig.savefig(_path, format='png')
    if display:
        INFO(f"{_path:s}", TYPE="PNG", show_func=False)
    return _path



