import os, sys
syspath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace(os.sep, '/')
if syspath not in sys.path:
    sys.path.append(syspath)

import matplotlib.pyplot as plt
from itertools import cycle
from log_utils import WARNING, INFO
from fileio_utils import absolute_path, unix_path

def set_custom_rcparams(reverse_cmap:bool=False) -> None:
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['image.cmap'] = 'viridis'
    if reverse_cmap: plt.rcParams['image.cmap'] = 'viridis_r'
    plt.rc('font', size=12)
    plt.rc('figure', titlesize=16)
    plt.rc('figure', labelsize=14)
    plt.rc('axes', titlesize=14)
    plt.rc('axes', labelsize=14)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.rc('legend', fontsize=12)


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

def fig2png(fig:plt.Figure, png_path:str, display:bool=True) -> str:
    _path = absolute_path(png_path)
    _path = f"{os.path.splitext(_path)[0]:s}.png"
    if not os.path.isdir(os.path.dirname(_path)):
        WARNING(f"{os.path.dirname(_path):s} does not exist. PNG was not saved.")
        return _path
    fig.savefig(_path, format='png')
    if display:
        INFO(f"{unix_path(_path):s}", hdr="PNG", show_func=False)
    return _path


def match_2d_axis_limits(ax: plt.Axes, xVy=1.0, loops=20):
    # todo: correct this!
    (x_min,x_max) = ax.get_xlim()
    (y_min,y_max) = ax.get_ylim()

    x_bot, x_top = x_min, x_max
    yx_bot, yx_top = y_min*xVy, y_max*xVy

    x_range = abs(x_top - x_bot)
    yx_range = abs(yx_top - yx_bot)

    counter=0
    while (x_range != yx_range) and counter < loops:
        diff = abs(x_range - yx_range)
        if x_range > (yx_range):
            yx_bot = yx_bot - (diff/2.0)
            yx_top = yx_top + (diff/2.0)
        if x_range < (yx_range*xVy):
            x_bot = x_min - (diff/2.0)
            x_top = x_max + (diff/2.0)

        x_range = (x_top - x_bot)
        yx_range = (yx_top - yx_bot)
        counter +=1

    if counter == loops:
        print(f"WARN [match_horizontal_limits()]:  plot limits miss-match ({x_range}) != ({yx_range})")

    y_top = yx_top/xVy
    y_bot = yx_bot/xVy

    ax.set_xlim(left = x_bot)
    ax.set_xlim(right = x_top)
    ax.set_ylim(bottom = y_bot)
    ax.set_ylim(top = y_top)


def align_yaxis(ax1:plt.Axes, ax2:plt.Axes, v1:float=0.0, v2:float=0.0):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)



def set_fig_title(fig: plt.Figure, title:str, tight_layout:bool=True):
    fig.suptitle(title)
    fig.canvas.manager.set_window_title(title)
    if tight_layout:
        fig.tight_layout()
