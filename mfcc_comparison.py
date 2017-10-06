from python_speech_features import mfcc
from python_speech_features import logfbank

import scipy.io.wavfile as wav
import numpy as np
import pydistance
import os

# Specify the target file
(rate, signal) = wav.read("vowel-07.wav")

# Specify the location containing sounds to be compared with target
path = 'sounds'
vowels = os.listdir(path)

# Prints the sample rate of the sound.
print(rate)

mfcc_features_target = mfcc(signal, rate, winlen=0.025, winstep=0.025)
mfcc_averages_target = np.average(mfcc_features_target, axis=0)

fbank_features_target = logfbank(signal, rate, winlen=0.025, winstep=0.025)
fbank_averages_target = np.average(fbank_features_target, axis=0)


def compare_mfcc(vowels):
    for vowel in vowels:
        (rate, signal) = wav.read("sounds\\{!s}".format(vowel))

        mfcc_features = mfcc(signal, rate, winlen=0.025, winstep=0.025)

        mfcc_averages = np.average(mfcc_features, axis=0)

        print(rate)

        distance = pydistance.SSD(mfcc_averages_target, mfcc_averages)

        print(vowel, distance)


compare_mfcc(vowels)


def compare_fbank(vowels):
    for vowel in vowels:
        (rate, signal) = wav.read("sounds\\{!s}".format(vowel))

        fbank_features = logfbank(signal, rate, winlen=0.025, winstep=0.025)
        fbank_averages = np.average(fbank_features, axis=0, )

        print(rate)

        distance = pydistance.SSD(fbank_averages_target, fbank_averages)

        print(vowel, distance)


compare_fbank(vowels)