import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy import signal




## time domain

(rate, data) = wav.read("vowel-01.wav")

print(rate, data)
print(type(data))
print(len(data))

time = np.linspace(0, len(data) / rate, num=len(data))


"""
fig, ax = plt.subplots()
ax.plot(time, data)

ax.set( xlabel='time (s)', 
        ylabel='Amplitude',
        title='Time Domain',
        xlim=(0,time[len(time)-1])

        )

ax.grid()
"""
#fig.savefig("test.png")
#plt.show()


# frequency domain



f, t, Sxx = signal.spectrogram(data, fs=44100, scaling='spectrum')
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.ylim(0,4000)
plt.xlabel('Time [sec]')
plt.show()