%sup2009preliminary, au2007, au2008,

scale_factor = 85/56.7;

hat_speed  = xlsread('Winter_Appendix_data.xlsx', 3, 'AL5:AL110'); %m/s

ankle_speed  = xlsread('Winter_Appendix_data.xlsx', 4, 'E5:E110'); %rad/s
ankle_torque = xlsread('Winter_Appendix_data.xlsx', 5, 'I6:I111')*scale_factor; %N-m
ankle_power  = ankle_speed.*ankle_torque; %W

knee_speed  = xlsread('Winter_Appendix_data.xlsx', 4, 'H5:H110'); %rev/s
knee_torque = xlsread('Winter_Appendix_data.xlsx', 5, 'P6:P111')*scale_factor; %N-m
knee_power  = knee_speed.*knee_torque; %W

mean_hat_speed = mean(hat_speed) %m/s

max_ankle_speed = max(abs(ankle_speed))/(2*pi)  %rev/s
max_ankle_torque = max(abs(ankle_torque)) %Nm
max_ankle_power = max(ankle_power) %W

max_knee_speed = max(abs(knee_speed))/(2*pi)  %rev/s
max_knee_torque = max(abs(knee_torque)) %Nm
max_knee_power = max(knee_power) %W
