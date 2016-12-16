import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import scipy.io as sio
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
         r"\usepackage{xunicode} %Unicode extras!",
         r"\usepackage{xltxtra}  %Fixes",
         r"\setmainfont[Ligatures={Common,TeX}]{Times}",
         r"\setsansfont[Ligatures={Common,TeX}]{Avenir Next Regular}",
         r"\usepackage{sfmath}"
         ],
    "legend.handlelength": 3
}
mpl.rcParams.update(pgf_with_custom_preamble)

#plot boxplots
gaitData = sio.loadmat('nm_data/gait_data_for_steady_state_fig.mat')
human_data = sio.loadmat('humanWalkEMG.mat')

normalized_time  = 100*gaitData['normalized_time']
hip_angle        = gaitData['hip_angle']
winter_hip       = gaitData['winter_hip']
hip_angle_mean   = gaitData['hip_angle_mean']
knee_angle       = gaitData['knee_angle']
winter_knee      = gaitData['winter_knee']
knee_angle_mean  = gaitData['knee_angle_mean']
vas_act          = gaitData['vas_act']
vas_act_mean     = gaitData['vas_act_mean']
ham_act          = gaitData['ham_act']
ham_act_mean     = gaitData['ham_act_mean']
gas_act          = gaitData['gas_act']
gas_act_mean     = gaitData['gas_act_mean']
knee_torque      = gaitData['knee_torque']
knee_torque_mean = gaitData['knee_torque_mean']
winter_torque    = gaitData['winter_torque']
winter_toe_off   = 100*(0.987 - 0.386)
toe_off_median   = 63.62
emg_time = 100*human_data['humanWalk']['phase'][0][0][0]
emg_vas  = 100*human_data['humanWalk']['EMG'][0][0][6,:]
emg_ham  = 100*human_data['humanWalk']['EMG'][0][0][4,:]
emg_gas  = 100*human_data['humanWalk']['EMG'][0][0][8,:]

def center_ylabel(axbnds, ytickbnds, axis):
    axrange = (axbnds[-1] - axbnds[0])/2
    newmdpt = (ytickbnds[-1] + ytickbnds[0])/2 - axbnds[0]
    ylabelpos = (-0.175, 0.5*newmdpt/axrange)
    axis.yaxis.set_label_coords(ylabelpos[0], ylabelpos[1])

fig, ax = plt.subplots(6,1, sharex = True)
fig.set_size_inches(3,6)

fig_space = 0.15

#plot hip data
p00  = ax[0].plot(normalized_time, hip_angle, color='0.5', linewidth=0.5)
p01, = ax[0].plot(normalized_time, hip_angle_mean, 'k', linewidth=2)
p02, = ax[0].plot(normalized_time, winter_hip, '--k', linewidth=2)
ytickbnds = (-20, 20)
ax[0].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[0].set_yticks(np.arange(-20, 40, 20))
ax[0].yaxis.set_label_text(r'$\mathsf{\theta_h}$ (deg)')
axbnds = ax[0].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[0])
axpos0 = ax[0].get_position()

#plot knee data
p10  = ax[1].plot(normalized_time, knee_angle, color='0.5', linewidth=0.5)
p11, = ax[1].plot(normalized_time, knee_angle_mean, 'k', linewidth=2)
p12, = ax[1].plot(normalized_time, winter_knee, '--k', linewidth=2)
ytickbnds = (0, 50)
ax[1].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[1].set_yticks(np.arange(0, 100, 50))
ax[1].yaxis.set_label_text(r'$\mathsf{\theta_k}$ (deg)')
axbnds = ax[1].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[1])
axpos1 = ax[1].get_position()
ax[1].set_position([axpos1.x0, axpos0.y0 - fig_space, axpos1.width, axpos1.height])
axpos1 = ax[1].get_position()

#plot knee torque
p20  = ax[2].plot(normalized_time, knee_torque, color='0.5', linewidth=0.5)
p21, = ax[2].plot(normalized_time, knee_torque_mean, 'k', linewidth=2)
p22, = ax[2].plot(normalized_time, winter_torque, '--k', linewidth=2)
ax[2].set_ylim(-40, 40)
ytickbnds = (-40, 40)
ax[2].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[2].set_yticks(np.arange(-40, 80, 40))
ax[2].yaxis.set_label_text(r'$\mathsf{\tau_k}$ (N-m)')
axbnds = ax[2].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[2])
axpos2 = ax[2].get_position()
ax[2].set_position([axpos2.x0, axpos1.y0 - fig_space, axpos2.width, axpos2.height])
axpos2 = ax[2].get_position()

#plot vastus activation 
p30  = ax[3].plot(normalized_time, vas_act, color='0.5', linewidth=0.5)
p31, = ax[3].plot(normalized_time, vas_act_mean, 'k', linewidth=2)
p32, = ax[3].plot(emg_time, emg_vas, '--k', linewidth=2)
ax[3].set_ylim(0, 50)
ytickbnds = (0, 20)
ax[3].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[3].set_yticks(np.arange(0, 40, 20))
ax[3].yaxis.set_label_text('VAS (%)')
axbnds = ax[3].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[3])
axpos3 = ax[3].get_position()
ax[3].set_position([axpos3.x0, axpos2.y0 - fig_space + 0.04, axpos3.width, axpos3.height])
axpos3 = ax[3].get_position()

#plot hamstring activation 
p40  = ax[4].plot(normalized_time, ham_act, color='0.5', linewidth=0.5)
p41, = ax[4].plot(normalized_time, ham_act_mean, 'k', linewidth=2)
p42, = ax[4].plot(emg_time, emg_ham, '--k', linewidth=2)
ax[4].set_ylim(0, 50)
ytickbnds = (0, 20)
ax[4].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[4].set_yticks(np.arange(0, 40, 20))
ax[4].yaxis.set_label_text('HAM (%)')
axbnds = ax[4].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[4])
axpos4 = ax[4].get_position()
ax[4].set_position([axpos4.x0, axpos3.y0 - fig_space + 0.02, axpos4.width, axpos4.height])
axpos4 = ax[4].get_position()

#plot gastrocnemius activation 
p50  = ax[5].plot(normalized_time, gas_act, color='0.5', linewidth=0.5)
p51, = ax[5].plot(normalized_time, gas_act_mean, 'k', linewidth=2)
p52, = ax[5].plot(emg_time, emg_gas, '--k', linewidth=2)
ax[5].set_ylim(0, 100)
ytickbnds = (0, 60)
ax[5].spines['left'].set_bounds(ytickbnds[0], ytickbnds[1])
ax[5].set_yticks(np.arange(0, 120, 60))
ax[5].yaxis.set_label_text('GAS (%)')
axbnds = ax[5].get_ylim()
center_ylabel(axbnds, ytickbnds, ax[5])
axpos5 = ax[5].get_position()
ax[5].set_position([axpos5.x0, axpos4.y0 - fig_space + 0.02, axpos5.width, axpos5.height])
axpos5 = ax[5].get_position()

#plot toeoff times
color0      = '#AA4839'
color1      = '#2A4F6E'
ax[-1].axvline(x=winter_toe_off,ymin=-0,ymax= 6.85,
    color=color0, linestyle='--', linewidth=1, zorder=0, clip_on=False)
ax[-1].axvline(x=toe_off_median,ymin=-0,ymax= 6.85,
    color=color1, linestyle='-', linewidth=1, zorder=0, clip_on=False)
    
#set axis properties
for axis in ax:
    axis.yaxis.set_tick_params(direction = 'out', width = 1)
    axis.spines['right'].set_visible(False)
    axis.spines['top'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    axis.xaxis.set_ticks_position('none')
    axis.yaxis.set_ticks_position('left')

ax[-1].spines['bottom'].set_visible(True)
ax[-1].set_xlim(-5, 100)
xtickbnds = (0, 100)
ax[-1].spines['bottom'].set_bounds(xtickbnds[0], xtickbnds[1])
ax[-1].xaxis.set_tick_params(direction = 'out', width = 1)
ax[-1].xaxis.set_ticks_position('bottom')
ax[-1].xaxis.set_label_text('% stride')

#ax1.set_position([box.x0, box.y0, box.width, 0.9*box.height])
ax[0].legend((p00[0], p01, p12), ('Individual Trial', 'Median', 'Unimpaired Data'),
    frameon = False, loc = 'upper center', prop={'size': 6}, ncol = 3,
    bbox_to_anchor =(0.4,1.4))

#fig.tight_layout()
plt.savefig('gaitData.pdf', bbox_inches='tight', transparent=True)
