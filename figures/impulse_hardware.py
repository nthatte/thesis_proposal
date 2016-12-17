import numpy as np
import matplotlib as mpl
from matplotlib import rc
import scipy.io as sio
import pdb
mpl.use("pgf")
import matplotlib.pyplot as plt

pgf_with_custom_preamble = {
    "pgf.texsystem": "xelatex",
    "font.family": "sans-serif", # use san serif/main font for text elements
    "text.usetex": False,    # use inline math for ticks
    "pgf.rcfonts": False,   
    "pgf.preamble": [
        r"\usepackage{amsmath}",
        r"\usepackage{fontspec}",
        r"\setsansfont{Avenir Next}",
        r"\setmainfont{Times}",
    ]
}
mpl.rcParams.update(pgf_with_custom_preamble)

#plot boxplots
no_impulse    = sio.loadmat('nm_data/no_impulse.mat')
early_impulse = sio.loadmat('nm_data/early_impulse.mat')
mid_impulse   = sio.loadmat('nm_data/mid_impulse.mat')
late_impulse  = sio.loadmat('nm_data/late_impulse.mat')

def shift_ylabel(axbnds, ytickbnds, axis):
    axrange = (axbnds[-1] - axbnds[0])/2
    newmdpt = (ytickbnds[-1] + ytickbnds[0])/2 - axbnds[0]
    ylabelpos = (-0.175, 0.5*newmdpt/axrange)
    axis.yaxis.set_label_coords(ylabelpos[0], ylabelpos[1])

def center_xlabel(axbnds, xtickbnds, axis):
    axrange = (axbnds[-1] - axbnds[0])/2
    newmdpt = (xtickbnds[-1] + xtickbnds[0])/2 - axbnds[0]
    xlabelpos = (0.5*newmdpt/axrange, -0.5)
    axis.xaxis.set_label_coords(xlabelpos[0], xlabelpos[1])

def shift_axes(axis, shift):
    axpos_old = axis.get_position()
    axpos_new = [axpos_old.x0, axpos_old.y0 + shift, axpos_old.width, axpos_old.height]
    axis.set_position(axpos_new)

fig, ax = plt.subplots(4,1, sharex = True)
fig.set_size_inches(2,5)
ylim = (-0.05, 0.3)
xlim = (-0.5, 0.35)
plot_letter_loc = -0.6
plot_letter_size = 10

color0      = '#AA4839'
color0light = '#D4796A'

#plot no impulse data
y_offset = -no_impulse['foot_tgt_pt'][0][1]
p00  = ax[0].plot(-1*no_impulse['foot_pos_x'], 
    no_impulse['foot_pos_y']+y_offset, 
    color='0.5', linewidth=0.5)
p01,  = ax[0].plot(-1*no_impulse['foot_pos_x_mean'], 
    no_impulse['foot_pos_y_mean']+y_offset, 'k', linewidth=2)
ytickbnds = (0, 0.1)
ax[0].set_ylim(ylim[0], ylim[1])
ax[0].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[0].set_yticks(np.arange(0, 0.2, 0.1))
#ax[0].yaxis.set_label_text('y position (m)')
#axbnds = ax[0].get_ylim()
#center_ylabel(axbnds, ytickbnds, ax[0])
ax[0].text(plot_letter_loc,0.15,'A', size = plot_letter_size)
ax[0].set_xlim(xlim[0], xlim[1])

#plot early impulse data
y_offset = -early_impulse['foot_tgt_pt'][0][1]
p10  = ax[1].plot(-1*early_impulse['foot_pos_x'], 
    early_impulse['foot_pos_y']+y_offset, 
    color='0.5', linewidth=0.5)
p11,  = ax[1].plot(-1*early_impulse['foot_pos_x_mean'], 
    early_impulse['foot_pos_y_mean']+y_offset, 'k', linewidth=2)
ytickbnds = (0, 0.1)
ax[1].set_ylim(ylim[0], ylim[1])
ax[1].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[1].set_yticks(np.arange(0, 0.2, 0.1))
ax[1].yaxis.set_label_text('y position (m)')
ax[1].text(plot_letter_loc,0.15,'B', size = plot_letter_size)
ylabelpos = ax[1].yaxis.get_label().get_position()
ax[1].yaxis.set_label_coords(-0.3, ylabelpos[1] - 0.65)
shift_axes(ax[1], 0.06)

#plot mid impulse data
y_offset = -mid_impulse['foot_tgt_pt'][0][1]
p20  = ax[2].plot(-1*mid_impulse['foot_pos_x'], 
    mid_impulse['foot_pos_y']+y_offset, 
    color='0.5', linewidth=0.5)
p21,  = ax[2].plot(-1*mid_impulse['foot_pos_x_mean'], 
    mid_impulse['foot_pos_y_mean']+y_offset, 'k', linewidth=2)
ytickbnds = (0, 0.1)
ax[2].set_ylim(ylim[0], ylim[1])
ax[2].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[2].set_yticks(np.arange(0, 0.2, 0.1))
#ax[2].yaxis.set_label_text('y position (m)')
#axbnds = ax[2].get_ylim()
#center_ylabel(axbnds, ytickbnds, ax[2])
shift_axes(ax[2], 0.125)
ax[2].text(plot_letter_loc,0.15,'C', size = plot_letter_size)

#plot mid impulse data
y_offset = -late_impulse['foot_tgt_pt'][0][1]
p30  = ax[3].plot(-1*late_impulse['foot_pos_x'], 
    late_impulse['foot_pos_y']+y_offset, 
    color='0.5', linewidth=0.5)
p31,  = ax[3].plot(-1*late_impulse['foot_pos_x_mean'], 
    late_impulse['foot_pos_y_mean']+y_offset, 'k', linewidth=2)
ytickbnds = (0, 0.1)
ax[3].set_ylim(ylim[0], ylim[1])
ax[3].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[3].set_yticks(np.arange(0, 0.2, 0.1))
#ax[3].yaxis.set_label_text('y position (m)')
#axbnds = ax[3].get_ylim()
#center_ylabel(axbnds, ytickbnds, ax[3])
shift_axes(ax[3], 0.19)
ax[3].text(plot_letter_loc,0.15,'D', size = plot_letter_size)
ax[3].set_xlim(xlim[0], xlim[1])

#plot target ft pt
ax[-1].axvline(x=-1*late_impulse['foot_tgt_pt'][0][0],ymin=-0,ymax= 3.0,
    c='k', linestyle='--', linewidth=1, zorder=0, clip_on=False)

#set axis properties
for axis in ax:
    axis.yaxis.set_tick_params(direction = 'out', width = 1)
    axis.spines['right'].set_visible(False)
    axis.spines['top'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    axis.xaxis.set_ticks_position('none')
    axis.yaxis.set_ticks_position('left')

ax[-1].spines['bottom'].set_visible(True)
xtickbnds = (-0.4, 0.2)
ax[-1].spines['bottom'].set_bounds(xtickbnds[0], xtickbnds[1])
ax[-1].set_xticks(np.arange(-0.4, 0.4, 0.2))
ax[-1].xaxis.set_tick_params(direction = 'out', width = 1)
ax[-1].xaxis.set_ticks_position('bottom')
ax[-1].xaxis.set_label_text('x position (m)')
axbnds = ax[-1].get_xlim()
center_xlabel(axbnds, xtickbnds, ax[-1])

ax[0].legend((p00[0], p01), ('Individual Trial', 'Median'),
    frameon = False, loc = 'upper center', prop={'size': 8}, ncol = 2,
    bbox_to_anchor =(0.3,1.05))

#fig.tight_layout()
plt.savefig('impulseHardware.pdf', bbox_inches='tight', transparent=True)
