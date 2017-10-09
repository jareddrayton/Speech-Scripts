import os
import scipy.io.wavfile as wav

# Script for listing the sample rate of files

path = 'Sounds'
vowels = os.listdir(path)

for vowel in vowels:
    (rate, signal) = wav.read("Sounds/{!s}".format(vowel))
    print(rate, vowel)