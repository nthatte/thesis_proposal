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

def center_ylabel(axbnds, ytickbnds, axis):
    axrange = (axbnds[-1] - axbnds[0])/2
    newmdpt = (ytickbnds[-1] + ytickbnds[0])/2 - axbnds[0]
    ylabelpos = (-0.175, 0.5*newmdpt/axrange)
    axis.yaxis.set_label_coords(ylabelpos[0], ylabelpos[1])

def shift_axes(axis, shift):
    axpos_old = axis.get_position()
    axpos_new = [axpos_old.x0, axpos_old.y0 + shift, axpos_old.width, axpos_old.height]
    axis.set_position(axpos_new)

#plot boxplots
refImpulseData = sio.loadmat('reflexTrip.mat')
impImpulseData = sio.loadmat('impedanceTrip.mat')

refDisturbedBallPos = refImpulseData['RBallPosDisturbed']['signals'][0][0][0][0]['values']
refDisturbedTime    = refImpulseData['RBallPosDisturbed']['time'][0][0]

refUndisturbedBallPos = refImpulseData['RBallPosUndisturbed']['signals'][0][0][0][0]['values']
refUndisturbedTime    = refImpulseData['RBallPosUndisturbed']['time'][0][0]

impDisturbedBallPos = impImpulseData['RBallPosDisturbed']['signals'][0][0][0][0]['values']
impDisturbedTime    = impImpulseData['RBallPosDisturbed']['time'][0][0]

impUndisturbedBallPos = impImpulseData['RBallPosUndisturbed']['signals'][0][0][0][0]['values']
impUndisturbedTime    = impImpulseData['RBallPosUndisturbed']['time'][0][0]

#set times
tbuffer = 0.2

ref_start = 10.026
ref_end = 10.593
refT0 = ref_start - tbuffer
refT1 = ref_end + tbuffer
refImpulseT1 = ref_start + 0.05*(ref_end - ref_start)

imp_start = 9.401
imp_end = 10.062
impT0 = imp_start - tbuffer;
impT1 = imp_end + tbuffer;
impImpulseT1 = imp_start + 0.05*(imp_end - imp_start)

#Size of impulse Box 
refImpulsePos = refDisturbedBallPos[np.logical_and(refDisturbedTime > refImpulseT1,
    refDisturbedTime < (refImpulseT1 + 0.01))[:,0], :]
refDisturbedBallPos = refDisturbedBallPos[np.logical_and(refDisturbedTime > refT0, 
    refDisturbedTime < refT1)[:,0],:] 
refUndisturbedBallPos = refUndisturbedBallPos[np.logical_and(refUndisturbedTime > refT0, 
    refUndisturbedTime < refT1)[:,0], :]

impImpulsePos = impDisturbedBallPos[np.logical_and(impDisturbedTime > impImpulseT1,
    impDisturbedTime < (impImpulseT1 + 0.01))[:,0], :]
impDisturbedBallPos   = impDisturbedBallPos[np.logical_and(impDisturbedTime > impT0, 
    impDisturbedTime < impT1)[:,0],:] 
impUndisturbedBallPos = impUndisturbedBallPos[np.logical_and(impUndisturbedTime > impT0, 
    impUndisturbedTime < impT1)[:,0], :]

#make x values relative to begining
refX1 = refUndisturbedBallPos[0,0]
refDisturbedBallPos[:,0]   = refDisturbedBallPos[:,0]   - refX1
refUndisturbedBallPos[:,0] = refUndisturbedBallPos[:,0] - refX1
refImpulsePos[:,0] = refImpulsePos[:,0] - refX1

impX1 = impUndisturbedBallPos[0,0]
impDisturbedBallPos[:,0]   = impDisturbedBallPos[:,0]   - impX1
impUndisturbedBallPos[:,0] = impUndisturbedBallPos[:,0] - impX1
impImpulsePos[:,0] = impImpulsePos[:,0] - impX1

''' plot reflex controller'''
fig, (ax1, ax2) = plt.subplots(2,1, sharex = True)
fig.set_size_inches(3,2)
p11, = ax1.plot(refUndisturbedBallPos[:,0],refUndisturbedBallPos[:,2],'k--',linewidth=2)
p12, = ax1.plot(refDisturbedBallPos[:,0],refDisturbedBallPos[:,2],'k',linewidth=2)
ax1.legend((p11, p12), ('Undisturbed', 'Disturbed'), frameon = False, loc = (0.4,0.9), fontsize = 10)

#set axis properties
ax1.xaxis.set_tick_params(direction = 'out', width = 1)
ax1.yaxis.set_tick_params(direction = 'out', width = 1)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.xaxis.set_ticks_position('none')
ax1.yaxis.set_ticks_position('left')

axis_lims = [-0.25, 2.5, -0.05, 0.3]
ax1.axis(axis_lims)
ax1.spines['bottom'].set_bounds(0, 2.5)
ax1.spines['left'].set_bounds(0, 0.3)
ax1.yaxis.set_label_text('Y Position [m]')
#ax1.set_aspect(2)

#adjust y label pos
axbnds = ax1.get_ylim()
#center_ylabel(axbnds, [0, 0.3], ax1)

ax1.set_yticks(np.arange(0, 0.60, 0.3))

#adjust label pos
inv_data = ax1.transData.inverted()
inv_axes = ax1.transAxes.inverted()

ylabelpos_axes = ax1.yaxis.get_label().get_position()
ylabelpos_display = ax1.transAxes.transform(ylabelpos_axes)
ylabelpos_data = inv_data.transform(ylabelpos_display)
ylabelpos_data[1] = np.array(ax1.spines['left'].get_bounds()).mean()
ylabelpos_display = ax1.transData.transform(ylabelpos_data)
ylabelpos_axes = inv_axes.transform(ylabelpos_display)
ax1.yaxis.get_label().set_position(ylabelpos_axes)

xlabelpos_axes = ax1.xaxis.get_label().get_position()
xlabelpos_display = ax1.transAxes.transform(xlabelpos_axes)
xlabelpos_data = inv_data.transform(xlabelpos_display)
xlabelpos_data[0] = np.array(ax1.spines['bottom'].get_bounds()).mean()
xlabelpos_display = ax1.transData.transform(xlabelpos_data)
xlabelpos_axes = inv_axes.transform(xlabelpos_display)
ax1.xaxis.get_label().set_position(xlabelpos_axes)

'''plot impedance controller'''
p21, = plt.plot(impUndisturbedBallPos[:,0],impUndisturbedBallPos[:,2],'k--',linewidth=2)
p22, = plt.plot(impDisturbedBallPos[:,0],impDisturbedBallPos[:,2],'k',linewidth=2)

#set axis properties
ax2.xaxis.set_tick_params(direction = 'out', width = 1)
ax2.yaxis.set_tick_params(direction = 'out', width = 1)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

ax2.axis(axis_lims)
ax2.spines['bottom'].set_bounds(0, 2)
ax2.spines['left'].set_bounds(0, 0.3)
ax2.xaxis.set_label_text('X Position [m]')
ax2.yaxis.set_label_text('Y Position [m]')

#adjust x label pos
xlabelpos = ax2.xaxis.get_label().get_position()
xlabelpos = (xlabelpos[0] + 0.04, xlabelpos[1])
ax2.xaxis.get_label().set_position(xlabelpos)
ax2.set_xticks(np.arange(0, 2.5, 0.5))
#ax2.set_aspect(2)

#adjust y label pos
axbnds = ax2.get_ylim()
#center_ylabel(axbnds, [0, 0.25], ax2)

ax2.set_xticks(np.arange(0, 2.5, 0.5))
ax2.set_yticks(np.arange(0, 0.60, 0.3))

#adjust label pos
inv_data = ax2.transData.inverted()
inv_axes = ax2.transAxes.inverted()

ylabelpos_axes = ax2.yaxis.get_label().get_position()
ylabelpos_display = ax2.transAxes.transform(ylabelpos_axes)
ylabelpos_data = inv_data.transform(ylabelpos_display)
ylabelpos_data[1] = np.array(ax2.spines['left'].get_bounds()).mean()
ylabelpos_display = ax2.transData.transform(ylabelpos_data)
ylabelpos_axes = inv_axes.transform(ylabelpos_display)
ax2.yaxis.get_label().set_position(ylabelpos_axes)

xlabelpos_axes = ax2.xaxis.get_label().get_position()
xlabelpos_display = ax2.transAxes.transform(xlabelpos_axes)
xlabelpos_data = inv_data.transform(xlabelpos_display)
xlabelpos_data[0] = np.array(ax2.spines['bottom'].get_bounds()).mean()
xlabelpos_display = ax2.transData.transform(xlabelpos_data)
xlabelpos_axes = inv_axes.transform(xlabelpos_display)
ax2.xaxis.get_label().set_position(xlabelpos_axes)

shift_axes(ax2, -0.2)
#fig.tight_layout()
plt.savefig('impulseResponse.pdf', bbox_inches='tight', transparent=True)
