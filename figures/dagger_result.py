import numpy as np
import matplotlib as mpl
from matplotlib import rc
import scipy.io as sio
import scipy.stats as stats
import pdb
mpl.use("pgf")
import matplotlib.pyplot as plt

pgf_with_custom_preamble = {
    "pgf.texsystem": "xelatex",
    "font.family": "sans-serif", # use san serif/main font for text elements
    "text.usetex": False,    # use inline math for ticks
    "pgf.rcfonts": False,   
    "font.size": 10,
    "pgf.preamble": [
        r"\usepackage{amsmath}",
        r"\usepackage{fontspec}",
        r"\setsansfont{Avenir Next}",
        r"\setmainfont{Times}",
    ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

#define colors http://colorschemedesigner.com/csd-3.5/#3B400hWs0dJMP
color0      = '#476A92'
color0light = '#9EC0E7'
color0dark  = '#2F537C'
color1      = '#BAD55E'
color1light = '#E3F6A2'
color1dark  = '#9BB53F'
color2      = '#A0468F'
color2light = '#EA9ADB'
color2dark  = '#882F77'
color3      = '#DFAE62'
color3light = '#F8D6A3'
color3dark  = '#BE8D42'

#load data
trip_detect_errors = [0.5, 20.7, 0.0236]
strat_class_errors = [0, 29.3, 12]

n_groups = 3

fig = plt.figure(figsize = (2,2))
ax  = plt.axes()

index = np.arange(n_groups)
bar_width = 0.35

rects1 = ax.bar(index, trip_detect_errors, bar_width, color=color0,
    label='Trip Detection', edgecolor='none', align='center')

rects2 = ax.bar(index + bar_width, strat_class_errors, bar_width, color=color1,
    label='Strategy Classification', edgecolor='none', align='center')

ax.yaxis.set_label_text('Error %')

fontsize = ax.xaxis.get_label().get_fontsize()
ax.legend(bbox_to_anchor=(-0.1, 1.00, 1., 0.2), loc=9, fontsize=fontsize-4,
    ncol=2, mode=None, frameon = False)

#set axis properties
ax.yaxis.set_tick_params(direction = 'out', width = 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('left')

for (i, err) in zip(index, trip_detect_errors):
    err_str = "{:3.2f}".format(err)
    ax.text(i, err+1, "{:.4}".format(err_str), fontsize=fontsize-4, ha='center',
    color=color0dark)

for (i, err) in zip(index, strat_class_errors):
    err_str = "{:3.2f}".format(err)
    ax.text(i + bar_width, err+1, "{:.4}".format(err_str), fontsize=fontsize-4, 
    ha='center', color=color1dark)

ax.axis([-bar_width, index[-1]+2*bar_width, 0, 30])
ax.spines['left'].set_bounds(0, 30)
ax.set_yticks(np.arange(0, 45, 15))

ax.set_xticks(index+1.5*bar_width)
ax.set_xticklabels(['Offline Error', 'Online Error', 
    'Online Error-Dagger'], rotation=45, ha='right')

filename = 'dagger_result.pdf'
fig.savefig(filename, bbox_inches='tight')
