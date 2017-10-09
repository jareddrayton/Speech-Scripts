from python_speech_features import mfcc
from python_speech_features import fbank
from python_speech_features import logfbank

import scipy.io.wavfile as wav
import numpy as np
import pydistance
import os

# Specify the target file
(rate, signal) = wav.read("Target[a].wav")

# Prints the sample rate of target sound.
print(rate)

# Specify the location containing sounds to be compared with target
path = 'Sounds'
vowels = os.listdir(path)


mfcc_features_target = mfcc(signal, rate, winlen=0.025, winstep=0.025)
print(np.shape(mfcc_features_target))
mfcc_averages_target = np.average(mfcc_features_target, axis=0)

fbank_features_target, fbank_energy_target = fbank(signal, rate, winlen=0.025, winstep=0.025)
print(np.shape(fbank_features_target))
fbank_averages_target = np.average(fbank_features_target, axis=0)

logfbank_features_target = logfbank(signal, rate, winlen=0.025, winstep=0.025)
print(np.shape(logfbank_features_target ))
logfbank_averages_target = np.average(logfbank_features_target, axis=0)

def compare_mfcc(vowels):

    for vowel in vowels:
        (rate, signal) = wav.read("Sounds/{!s}".format(vowel))

        mfcc_features = mfcc(signal, rate, winlen=0.025, winstep=0.025)

        mfcc_averages = np.average(mfcc_features, axis=0)

        distance = pydistance.SSD(mfcc_averages_target, mfcc_averages)

        print(vowel, distance)


compare_mfcc(vowels)

def compare_fbank(vowels):
    for vowel in vowels:
        (rate, signal) = wav.read("Sounds/{!s}".format(vowel))

        fbank_features, fbank_energy = fbank(signal, rate, winlen=0.025, winstep=0.025)
        fbank_averages = np.average(fbank_features, axis=0, )

        distance = pydistance.SSD(fbank_averages_target, fbank_averages)

        print(vowel, distance)


compare_fbank(vowels)

def compare_logfbank(vowels):
    for vowel in vowels:
        (rate, signal) = wav.read("Sounds/{!s}".format(vowel))

        logfbank_features = logfbank(signal, rate, winlen=0.025, winstep=0.025)
        logfbank_averages = np.average(logfbank_features, axis=0, )

        distance = pydistance.SSD(fbank_averages_target, logfbank_averages)

        print(vowel, distance)


compare_logfbank(vowels)