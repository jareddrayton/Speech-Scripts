# This script generates n random artwords of a given duration for synthesisng with praat.
# It is intended to give a rough estimate as to the single vs parallel performance.
# Outputs a the total time, plus a rough how much faster than realtime simulation is.

import subprocess
import random
import time
import os
import shutil

# set number of artwords to be generated. should be equal to at least the number of threads available
n = 20

# set the duration of each artword sound
duration = '1.0'

# praat folder location
praat_fp = 'Praat'

# set the name of the temporary directory
temp_fp = 'temp'

def artword_generator(index):
    """This function generates a random artword/praat script"""

    # a list containing all of the articulator parameters barring lungs
    parameters = ['Interarytenoid',
                  'Cricothyroid',
                  'Vocalis',
                  'Thyroarytenoid',
                  'PosteriorCricoarytenoid',
                  'LateralCricoarytenoid',
                  'Stylohyoid',
                  'Sternohyoid',
                  'Thyropharyngeus',
                  'LowerConstrictor',
                  'MiddleConstrictor',
                  'UpperConstrictor',
                  'Sphincter',
                  'Hyoglossus',
                  'Styloglossus',
                  'Genioglossus',
                  'UpperTongue',
                  'LowerTongue',
                  'TransverseTongue',
                  'VerticalTongue',
                  'Risorius',
                  'OrbicularisOris',
                  'TensorPalatini',
                  'Masseter',
                  'Mylohyoid',
                  'LateralPterygoid',
                  'Buccinator']

    # Generate a list of n random values in the range [-1,1] with a list comprehension
    values = [round(random.uniform(-1, 1), 1) for x in range(len(parameters))]

    # creates a text file with the .praat extension by calling open and assigns to variable f
    f = open('./{}/test{}.praat'.format(temp_fp, index), 'w')

    f.write('Create Speaker... Robovox Male 2\r\n')
    f.write('Create Artword... Individual{!s} {}\r\n'.format(index, duration))
    f.write('Set target... 0.0  0.07  Lungs\r\n')
    f.write('Set target... 0.04  0.0  Lungs\r\n')
    f.write('Set target... {}   0.0  Lungs\r\n'.format(duration))
    f.write('Set target... 0.00 1 LevatorPalatini\r\n')
    f.write('Set target... {} 1 LevatorPalatini\r\n'.format(duration))

    # a loop that
    for i in range(len(parameters)):
        f.seek(0, 2)
        f.write('Set target... 0.0 {!s} {!s}\r\n'.format(values[i], parameters[i]))
        f.write('Set target... {} {!s} {!s}\r\n'.format(duration, values[i], parameters[i]))

    f.write('select Artword Individual{!s}\r\n'.format(index))
    f.write('plus Speaker Robovox\r\n')
    f.write('To Sound... 22500 25    0 0 0    0 0 0   0 0 0\r\n')
    f.write('''nowarn do ("Save as WAV file...", "Individual{!s}.wav")\r\n'''.format(index))


os.mkdir(temp_fp)

for i in range(n):
    artword_generator(i)

def praat_serial():

    start = time.time()

    for i in range(n):
        subprocess.run(['./{}/praat'.format(praat_fp), '--run', './{}/test{!s}.praat'.format(temp_fp,i)])

    end = round(time.time() - start, 2)

    print('Total time to synthesise {!s} sounds of duration {} in seconds = {!s}'.format(n, duration, end))
    print('This is equivalent to ', round(n * float(duration) / end, 2), 'x real time')

praat_serial()

shutil.rmtree(temp_fp)


os.mkdir(temp_fp)

for i in range(n):
    artword_generator(i)

def praat_parallel():

    start = time.time()

    for i in range(n):
        p = subprocess.Popen(['./{}/praat'.format(praat_fp), '--run', './{}/test{!s}.praat'.format(temp_fp,i)])

    p.communicate()

    end = round(time.time() - start, 2)

    print('Total time to synthesise {!s} sounds of duration {} in seconds = {!s}'.format(n, duration, end))
    print('This is equivalent to ', round(n * float(duration) / end, 2), 'x real time')

    time.sleep(4)

praat_parallel()

shutil.rmtree(temp_fp)