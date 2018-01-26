import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Start with implementing Rosenbergs models from 1971
# "Effect of Glottal Pulse Shape on the Quality of Natural Vowels"
# What is useful output?
# Could use as a command line application.
# Put in desired length of audio, waveform type, F0
# How is this used as a module? e.g. with a vocal tract model.

###############################################################################
# Global Variables

wav_length = 2.0 # Specify the length of the .Wav file in seconds

amplitude = 32767
sample_rate = 16000
fundamental_frequency = 115

period_samples = sample_rate // fundamental_frequency

Tp = int(0.4 * period_samples) # length of slope in 
Tn = int(0.16 * period_samples)
To = int(period_samples - Tp - Tn)

print(Tp, Tn, To)
print(Tp + Tn + To)
print(period_samples)

###############################################################################

# Rosenberg

def rosenberg_a():
    
    data = []
    
    for i in range(0, Tp): # 0 < t <= Tp
        #print(i)
        #print(amplitude * (i / Tp))
        data.append(amplitude * (i / Tp))

    for i in range(Tp, Tp + Tn): #Tp <= t <= Tp + Tn
        #print(i)
        #print(amplitude * (1 - ((i-Tp)/Tn)))
        data.append(amplitude * (1 - ((i-Tp)/Tn)))

    for i in range(Tp + Tn, period_samples):
        #print(i)
        #print(i*0)
        data.append(i*0)

    test = list(map(int, data))
    
    #print(len(test))
    #print(test)
    
    return test

def rosenberg_b():
    pass

def rosenberg_c():
    pass

def rosenberg_d():
    pass

def rosenberg_e():
    pass

def rosenberg_f():
    pass

# Pulse train

def pulse_train():
    pass

# LF model

def lf():
    pass

# Flanagan

def flanagan_landgraf():
    pass

def ishizaka_flanagan():
    pass


###############################################################################
# Helper functions

def make_wav():
    
    buffer = rosenberg_a()

    iterations = int((sample_rate * wav_length) / period_samples) # calculate nnumber of times need to use buffer
    #print(iterations)
    
    #print(np.asarray(buffer))

    a = np.array([])
    b = np.asarray(buffer)

    print(iterations)
    print(np.tile(b, 2))
    
    a = np.tile(b, iterations)
    print(a.size)

    print(sample_rate * wav_length)

    #for i in range(iterations):
    #    np.concatenate((a, b), axis=1)
    
    
    
make_wav()


def make_plot():
    fig, ax = plt.subplots()
    ax.plot(rosenberg_a())

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()

#make_plot()