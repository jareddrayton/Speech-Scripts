import numpy as np
import scipy.io.wavfile as wav

# Start with implementing Rosenbergs models from 1971
# "Effect of Glottal Pulse Shape on the Quality of Natural Vowels"
# What is useful output?
# Could use as a command line application.
# Put in desired length of audio, waveform type, F0
# How is this used as a module? e.g. with a vocal tract model.

# Pulse train

def pulse_train():
    pass


# Rosenberg

amplitude = 32767
sample_rate = 16000
fundamental_frequency = 117

period_samples = sample_rate // fundamental_frequency

Tp = int(0.4 * period_samples) # length of slope in 
Tn = int(0.16 * period_samples)
To = int(period_samples - Tp - Tn)

print(Tp, Tn, To)
print(Tp + Tn + To)
print(period_samples)

#0 < t <= Tp
#Tp <= t <= Tp + Tn

data = []

def rosenberg_a():
    
    for i in range(1, Tp):
        print(i)
        print(amplitude * (i / Tp))
    for i in range(Tp, Tp + Tn):
        print(i)
        print(amplitude(1- (i-)))

rosenberg_a()

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


# LF model

def lf():
    pass


# Flanagan

def flanagan_landgraf():
    pass

def ishizaka_flanagan():
    pass