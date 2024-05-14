
import matplotlib.pyplot as plt
from itertools import cycle

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


