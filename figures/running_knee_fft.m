load('knee_moment_running.mat')

t_end = 1.3;

period = 0.001;
time = 0.001:period:1.3;

tau = spline(knee_moment_running(:,1)*1.3/100, knee_moment_running(:,2), ...
    time);

figure(1)
plot(time, tau)

%power spectral density

Fs = 1/period;
N = length(tau);
[Pxx,F] = periodogram(tau,[],N,Fs);
plot(F,10*log10(Pxx))

%{
xdft = fft(tau)

xdft = xdft(1:N/2+1);
psdx = (1/(Fs*N)) * abs(xdft).^2;
psdx(2:end-1) = 2*psdx(2:end-1);
freq = 0:Fs/N:Fs/2;

figure(2)
plot(freq,10*log10(psdx))
grid on
title('Periodogram Using FFT')
xlabel('Frequency (Hz)')
ylabel('Power/Frequency (dB/Hz)')

figure(3)
plot(freq,psdx)
grid on
title('Periodogram Using FFT')
xlabel('Frequency (Hz)')
ylabel('Power/Frequency (dB/Hz)')

power_int = cumtrapz(psdx);
power_int_percent = power_int/power_int(end);

index = find(power_int_percent > 0.9)
frq_cut = freq(index(1))
%}
