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
winter_data = np.loadtxt(open("winter_data_angle_torque.csv","rb"),delimiter=",",skiprows=1)
winter_data = winter_data[36:,:]

scale_factor = 85/56.7

max_torque_idx = np.argmax(winter_data[:,1])

#fit to 
p_dorsi = np.polyfit(winter_data[0:max_torque_idx, 0], 
    scale_factor*winter_data[0:max_torque_idx, 1], 1)
tau_fit_dorsi = np.polyval(p_dorsi, winter_data[0:max_torque_idx, 0])
#p_dorsi, _, _, _ = np.linalg.lstsq(np.array([winter_data[0:max_torque_idx,0]]).T, 
#    np.array([scale_factor*winter_data[0:max_torque_idx, 1]]).T)
#tau_fit_dorsi = p_dorsi[0][0]*winter_data[0:max_torque_idx,0]

p_plantar = np.polyfit(winter_data[max_torque_idx-1:, 0], 
    scale_factor*winter_data[max_torque_idx-1:, 1], 1)
tau_fit_plantar = np.polyval(p_plantar, winter_data[max_torque_idx-1:, 0])

#create figure
fig = plt.figure(figsize = (3,1.5))
ax = plt.axes()

#add lines connecting medians
markersize = 4
p0, = ax.plot(winter_data[:,0]*180/np.pi, winter_data[:,1]*scale_factor,
    linewidth=2, color=color0)
p1, = ax.plot(winter_data[0:max_torque_idx, 0]*180/np.pi, tau_fit_dorsi, '--',
    linewidth=2, color=color1)
p2, = ax.plot(winter_data[max_torque_idx-1:, 0]*180/np.pi, tau_fit_plantar, '--',
    linewidth=2, color=color2)

#pdb.set_trace()
ax.legend((p0, p1, p2), ('stance torque', 'early stance stiffness', 
    'late stance stiffness'), frameon = False, loc = (-0.2, 0.8), fontsize=8,
    handlelength=3)

ax.xaxis.set_label_text('Angle (deg)')
ax.yaxis.set_label_text('Torque (N-m)')

#set axis properties
ax.xaxis.set_tick_params(direction = 'out', width = 1)
ax.yaxis.set_tick_params(direction = 'out', width = 1)
ax.yaxis.set_tick_params(which='minor', direction = 'out', width = 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#ax.axis([-5, 10, -25, 160])

ax.spines['left'].set_bounds(0, 50)
ax.set_yticks(np.arange(0, 100, 50))
#ax.set_yticklabels([0, 0.001, 0.01, 0.1, 1, 10])

ax.spines['bottom'].set_bounds(-15, 0)
ax.set_xticks(np.arange(-15,15,15))
#ax.set_xticklabels(xtickloc+1)

#adjust label pos
inv_data = ax.transData.inverted()
inv_axes = ax.transAxes.inverted()

ylabelpos_axes = ax.yaxis.get_label().get_position()
ylabelpos_display = ax.transAxes.transform(ylabelpos_axes)
ylabelpos_data = inv_data.transform(ylabelpos_display)
ylabelpos_data[1] = np.array(ax.spines['left'].get_bounds()).mean()
ylabelpos_display = ax.transData.transform(ylabelpos_data)
ylabelpos_axes = inv_axes.transform(ylabelpos_display)
ax.yaxis.get_label().set_position(ylabelpos_axes)

xlabelpos_axes = ax.xaxis.get_label().get_position()
xlabelpos_display = ax.transAxes.transform(xlabelpos_axes)
xlabelpos_data = inv_data.transform(xlabelpos_display)
xlabelpos_data[0] = np.array(ax.spines['bottom'].get_bounds()).mean()
xlabelpos_display = ax.transData.transform(xlabelpos_data)
xlabelpos_axes = inv_axes.transform(xlabelpos_display)
ax.xaxis.get_label().set_position(xlabelpos_axes)


filename = 'ankle_impedance_fits.pdf'
fig.savefig(filename, bbox_inches='tight')
