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

#define colors http://colorschemedesigner.com/csd-3.5/#3B400hWs0dJMP
color0      = '#476A92'
color0light = '#9EC0E7'
color1      = '#BAD55E'
color1light = '#E3F6A2'
color2      = '#A0468F'
color2light = '#EA9ADB'
color3      = '#DFAE62'
color3light = '#F8D6A3'

#load data
ssm_grf_y = sio.loadmat('spring_mass_model_grf_y.mat')
ssm_grf_y = ssm_grf_y['spring_mass_model_grf_y']

ssm_grf_x = sio.loadmat('spring_mass_model_grf_x.mat')
ssm_grf_x = ssm_grf_x['spring_mass_model_grf_x']

ssm_height = sio.loadmat('spring_mass_model_y.mat')
ssm_height = ssm_height['spring_mass_model_y']

human_grf_y = sio.loadmat('human_grf_y.mat')
human_grf_y = human_grf_y['human_grf_y']

human_grf_x = sio.loadmat('human_grf_x.mat')
human_grf_x = human_grf_x['human_grf_x']

human_height = sio.loadmat('human_y.mat')
human_height = human_height['human_y']

#create figure
#fig, axes = plt.subplots(2, sharex = True, figsize = (2,5))
fig = plt.figure(figsize=(2, 4)) 
gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1], sharex = ax0)

#figure 
markersize = 4
p00, = ax0.plot(ssm_grf_y[:,0], ssm_grf_y[:,1], linewidth=2, color=color0)
p01, = ax0.plot(ssm_grf_x[:,0], ssm_grf_x[:,1], linewidth=2, color=color0)
p02, = ax0.plot(human_grf_y[:,0], human_grf_y[:,1], linewidth=2,
    color=color1) 
p03, = ax0.plot(human_grf_x[:,0], human_grf_x[:,1],
    linewidth=2, color=color1)

p10, = ax1.plot(ssm_height[:,0], ssm_height[:,1], linewidth=2, color=color0)
p11, = ax1.plot(human_height[:,0], human_height[:,1], linewidth=2,
    color=color1)

ax1.legend((p10, p11), ('spring-mass model', 'human data'), frameon = False,
    bbox_to_anchor=(-0.25, -0.5, 1., 0), loc=9, fontsize=10)

ax0.yaxis.set_label_text('GRF (m)')
ax1.yaxis.set_label_text(r'$\Delta$ COM height (cm)')
ax1.xaxis.set_label_text('Stance Time (%)')

#set axis properties
ax0.xaxis.set_tick_params(direction = 'out', width = 1)
ax0.yaxis.set_tick_params(direction = 'out', width = 1)
ax0.yaxis.set_tick_params(which='minor', direction = 'out', width = 1)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.yaxis.set_ticks_position('left')
ax0.xaxis.set_ticks_position('none')

ax1.xaxis.set_tick_params(direction = 'out', width = 1)
ax1.yaxis.set_tick_params(direction = 'out', width = 1)
ax1.yaxis.set_tick_params(which='minor', direction = 'out', width = 1)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

#ax0.axis([-5, 10, -25, 160])

ax0.spines['left'].set_bounds(0, 1)
ax0.set_yticks(np.arange(0, 1.5, 0.5))
#ax0.set_yticklabels([0, 0.001, 0.01, 0.1, 1, 10])

ax1.set_ylim([-3.5, ax1.get_ylim()[-1]])
ax1.spines['left'].set_bounds(-3, 3)
ax1.set_yticks(np.arange(-3, 6, 3))
ax1.spines['bottom'].set_bounds(0, 100)
ax1.set_xticks(np.arange(0,150,50))
#ax0.set_xticklabels(xtickloc+1)
plt.setp(ax0.get_xticklabels(), visible=False)

#adjust label pos
inv_data_0 = ax0.transData.inverted()
inv_axes_0 = ax0.transAxes.inverted()

inv_data_1 = ax1.transData.inverted()
inv_axes_1 = ax1.transAxes.inverted()

ylabelpos_axes = ax0.yaxis.get_label().get_position()
ylabelpos_display = ax0.transAxes.transform(ylabelpos_axes)
ylabelpos_data = inv_data_0.transform(ylabelpos_display)
ylabelpos_data[1] = np.array(ax0.spines['left'].get_bounds()).mean()
ylabelpos_display = ax0.transData.transform(ylabelpos_data)
ylabelpos_axes = inv_axes_0.transform(ylabelpos_display)
ax0.yaxis.get_label().set_position(ylabelpos_axes)

ylabelpos_axes = ax1.yaxis.get_label().get_position()
ylabelpos_display = ax1.transAxes.transform(ylabelpos_axes)
ylabelpos_data = inv_data_1.transform(ylabelpos_display)
ylabelpos_data[1] = np.array(ax1.spines['left'].get_bounds()).mean()
ylabelpos_display = ax1.transData.transform(ylabelpos_data)
ylabelpos_axes = inv_axes_1.transform(ylabelpos_display)
ax1.yaxis.get_label().set_position(ylabelpos_axes)

xlabelpos_axes = ax1.xaxis.get_label().get_position()
xlabelpos_display = ax1.transAxes.transform(xlabelpos_axes)
xlabelpos_data = inv_data_1.transform(xlabelpos_display)
xlabelpos_data[1] = np.array(ax1.spines['left'].get_bounds()).mean()
xlabelpos_display = ax1.transData.transform(xlabelpos_data)
xlabelpos_axes = inv_axes_1.transform(xlabelpos_display)
ax1.xaxis.get_label().set_position(xlabelpos_axes)

plt.subplots_adjust(hspace = .001)

filename = 'spring_mass_model_data.pdf'
fig.savefig(filename, bbox_inches='tight')
