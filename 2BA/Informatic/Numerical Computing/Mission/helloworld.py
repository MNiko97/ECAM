# Author: Mitrovic Nikola
# Version: May 27, 2020

import numpy as np
import matplotlib.pyplot as plt

sampling = 10
interval = 1/sampling
frequency = 1
ncol=sampling**2
nrow=20

time = np.arange(0, sampling, interval)
signal = np.sin(2*np.pi*frequency*time)

noise = np.random.normal(0,1,ncol*nrow).reshape(nrow, ncol)
signal_noisy = signal + noise.mean(axis=0)

fftSignal = np.fft.fft(signal/len(signal))
fftSignal = fftSignal[range(int(len(signal)/2))]

timePeriod  = len(signal)/sampling
frequencies = np.arange(int(len(signal)/2))/timePeriod

figure, axs = plt.subplots(3)
plt.subplots_adjust(hspace=1)

axs[0].set_title('Sine Wave')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')
axs[0].plot(time, signal)

axs[1].set_title('Noisy Sine Wave')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Amplitude')
axs[1].plot(time, signal_noisy)

axs[2].set_title('FFT Transform Sine Wave')
axs[2].set_xlabel('Frequency')
axs[2].set_ylabel('Amplitude')
axs[2].plot(frequencies, abs(fftSignal))

plt.show()