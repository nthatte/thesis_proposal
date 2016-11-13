import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib as mpl
import pdb

mpl.use("pgf")
pgf_with_custom_preamble = {
    "pgf.texsystem": "xelatex",
    "font.family": "sans-serif", # use san serif/main font for text elements
    "text.usetex": False,    # use inline math for ticks
    "pgf.rcfonts": True,   
    "pgf.preamble": [
        r"\usepackage{amsmath}",
        r"\usepackage{fontspec}",
        r"\usepackage{newpxmath}"
        r"\usepackage{xunicode} %Unicode extras!",
        r"\usepackage{xltxtra}  %Fixes",
        r"\setmainfont[Ligatures={Common,TeX}]{Palatino}",
        r"\setsansfont[Ligatures={Common,TeX}]{Avenir Next}",
        ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

#define colors http://colorschemedesigner.com/csd-3.5/#3B400hWs0dJMP
color0      = '#476A92'
color0light = '#9EC0E7'
color1      = '#BAD55E'
color1light = '#E3F6A2'
color2      = '#A0468F'
color2light = '#EA9ADB'
color3      = '#DFAE62'
color3light = '#F8D6A3'

K = 5
N = 1.5
sigma_ce_neg = np.linspace(-1, 0) #normalized fiver length
sigma_ce_pos = np.linspace( 0, 1) #normalized fiver length
fv_neg = (1 + sigma_ce_neg)/(1 - K*sigma_ce_neg)
fv_pos = N + (N - 1)*(1 - sigma_ce_pos)/(-7.56*K*sigma_ce_pos - 1)

#create figure
fig = plt.figure(figsize = (2,2))
ax = plt.axes()

#add lines connecting medians
markersize = 4
p0, = ax.plot(sigma_ce_neg, fv_neg, linewidth=2, color=color1)
p1, = ax.plot(sigma_ce_pos, fv_pos, linewidth=2, color=color1)

ax.set_title('CE Force-Velocity', y=1.08)
ax.xaxis.set_label_text('Velocity')
ax.yaxis.set_label_text('Force')

#set axis properties
ax.xaxis.set_tick_params(direction = 'out', width = 1)
ax.yaxis.set_tick_params(direction = 'out', width = 1)
ax.yaxis.set_tick_params(which='minor', direction = 'out', width = 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis([-1.2, 1.1, -0.15, 1.6])
ax.spines['left'].set_bounds(0, 1.5)
ax.set_yticks([0, 1, N])
ax.set_yticklabels(['0', 1, 'N'])

ax.spines['bottom'].set_bounds(-1, 1)
ax.set_xticks(np.arange(-1,2,1))
ax.set_xticklabels(['$\mathsf{v_{max}}$', '0', '$\mathsf{|v_{max}|}$'])

#adjust label pos
ylabelpos = ax.yaxis.get_label().get_position()
ylabelpos = (ylabelpos[0], ylabelpos[1] + 0.05)
ax.yaxis.get_label().set_position(ylabelpos)

xlabelpos = ax.xaxis.get_label().get_position()
xlabelpos = (xlabelpos[0]+0.05, xlabelpos[1])
ax.xaxis.get_label().set_position(xlabelpos)

filename = 'force_velocity_plot.pdf'
fig.savefig(filename, bbox_inches='tight')
