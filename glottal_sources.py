import numpy as np

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
fundamental_frequency = 120

period_samples = sample_rate // fundamental_frequency

Tp = 0.4 * period_samples # length of slope in 
Tn = 0.16
To = 1 - Tp - Tn

def rosenberg_a():
    0 < t <= Tp
    a = t/Tp
    a * t / Tp


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