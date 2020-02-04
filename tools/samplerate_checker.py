import os, subprocess
import scipy.io.wavfile as wav

# Script for listing the sample rate of files

path = 'Sounds'
vowels = os.listdir(path)

for vowel in vowels:
    (rate, signal) = wav.read("Sounds/{!s}".format(vowel))
    print(rate, vowel.replace('.wav', ''))

print()
RESAMPLE = input("Would you like to resample? (Y/N)  ")

if RESAMPLE == 'y' or 'Y':
    NEW_SAMPLE_RATE = int(input("Enter new sample rate in Hz. (Int)  "))

    for sound in vowels:
        with open('resample.praat', 'a') as f:
            f.write('Read from file: "{}/{}"\n'.format(path, sound))
            f.write('Resample: {!s}, 50\n'.format(NEW_SAMPLE_RATE))
            f.write('selectObject: "Sound {}_{!s}"\n'.format(sound.replace('.wav', ''), NEW_SAMPLE_RATE))
            f.write('Save as WAV file: "{}/{}_{!s}.wav"\n'.format(path, sound.replace('.wav', ''), NEW_SAMPLE_RATE))

subprocess.run(['./Praat/praat', '--run', './resample.praat'])



