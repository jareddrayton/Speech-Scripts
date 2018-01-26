import math
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Start with implementing Rosenbergs models from 1971
# "Effect of Glottal Pulse Shape on the Quality of Natural Vowels"
# What is useful output?
# Could use as a command line application.
# How is this used as a module? e.g. with a vocal tract model.

###############################################################################
# Rosenberg Variables

wav_length = 10.0 # Specify the length of the .Wav file in seconds

amplitude = 32767 # Using 16 Bit PCM. This is 'a' in the original paper
sample_rate = 44100 # 
fundamental_frequency = 119 #

period_samples = sample_rate // fundamental_frequency # No. of samples used for one period

positive_slope = 0.40
negative_slope = 0.16

Tp = int(positive_slope * period_samples) # duration of slope in samples 
Tn = int(negative_slope * period_samples) # duration of slope in samples
To = int(period_samples - Tp - Tn)

print(Tp, Tn, To)
print(Tp + Tn + To)
print(period_samples)

###############################################################################
# Rosenberg pulse functions

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

    data = list(map(int, data))
    
    #print(len(test))
    #print(test)
    
    return data

def rosenberg_b():
    
    data = []
    
    for i in range(0, Tp): # While 0 < t <= Tp
        data.append(amplitude * ( 3 * (i/Tp) ** 2 - 2 * (i/Tp) ** 3))

    for i in range(Tp, Tp + Tn): # While Tp <= t <= Tp + Tn
        data.append(amplitude * (1 - ((i-Tp)/Tn)**2))

    for i in range(Tp + Tn, period_samples): # 
        data.append(i*0)

    data = list(map(int, data)) # Convert to integers
    
    return data

def rosenberg_c():
    
    data = []
    
    for i in range(0, Tp): # While 0 < t <= Tp
        data.append(    (amplitude/2.0) * (1 - math.cos((i/Tp) * math.pi)       ))

    for i in range(Tp, Tp + Tn): # While Tp <= t <= Tp + Tn
        data.append( amplitude * math.cos( ((i-Tp)/Tn) * (math.pi/2) ) )
        #print(amplitude, i, Tp, Tn,)
    
    for i in range(Tp + Tn, period_samples): # 
        data.append(i*0)

    data = list(map(int, data)) # Convert to integers
    
    return data

def rosenberg_d():
    
    data = []
    
    for i in range(0, Tp): # While 0 < t <= Tp
        data.append(    (amplitude/2.0) * (1 - math.cos((i/Tp) * math.pi)       ))

    for i in range(Tp, Tp + Tn): # While Tp <= t <= Tp + Tn
        data.append( amplitude/2.0 * ( 1 + math.cos( ((i-Tp)/Tn) * (math.pi/2) ) ) )
        #print(amplitude, i, Tp, Tn,)
        #print( amplitude/2.0 * ( 1 + math.cos( ((i-Tp)/Tn) * (math.pi/2) ) ) )
    for i in range(Tp + Tn, period_samples): # 
        data.append(i*0)

    data = list(map(int, data)) # Convert to integers
    
    return data

rosenberg_d()

def rosenberg_e():
    data = []
    
    for i in range(0, Tp): # While 0 < t <= Tp
        data.append(  amplitude * math.sin((i/Tp) * (math.pi/2))       )

    for i in range(Tp, Tp + Tn): # While Tp <= t <= Tp + Tn
        data.append( amplitude * math.cos( ((i-Tp)/Tn) * (math.pi/2) ) )
    
    for i in range(Tp + Tn, period_samples): # 
        data.append(i*0)

    data = list(map(int, data)) # Convert to integers
    
    return data

def rosenberg_f():
    pass

###############################################################################
# Pulse trains

def pulse_train():
    pass

###############################################################################
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

    iterations = int((sample_rate * wav_length) / period_samples) # calculate number of times need to use buffer

    b = np.asarray(buffer, dtype=np.int16) # Sets data type to int16 for 16 Bit PCM
    
    a = np.tile(b, iterations) # Use tile function to duplicate the buffer
    
    print(iterations)
    print(a.size)

    print('WARNING: File will be short by ', 
        int(sample_rate * wav_length) - a.size, 'samples')

    wav.write('test_a.wav', sample_rate, a) # Writes the numpy array to a .wav file

#make_wav()

###############################################################################
# Plotting functions

def make_plot():
    fig, ax = plt.subplots()
    #ax.plot(rosenberg_a())
    #ax.plot(rosenberg_b())
    ax.plot(rosenberg_c())
    #ax.plot(rosenberg_d())
    ax.plot(rosenberg_e())

    ax.set(xlabel='time (s)', ylabel='Amplitude',
       title='About as simple as it gets, folks')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()

make_plot()

def plot_all():
    pass