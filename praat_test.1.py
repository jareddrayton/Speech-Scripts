# This script generates n random artwords of a given duration for synthesisng with praat.
# It is intended to give a rough estimate as to the single vs parallel performance.
# Outputs a the total time, plus a rough how much faster than realtime simulation is.

import subprocess
import random
import time
import os
import shutil
import multiprocessing

from time import sleep

from concurrent import futures

# set number of artwords to be generated. should be equal to at least the number of threads available
n = 10

# set the duration of each artword sound
duration = '1.0'

# praat folder location
praat_fp = 'Praat'

# set the name of the temporary directory
temp_fp = 'temp'
os.mkdir(temp_fp)
print('hey')

def artword_generator_limited(index):
    """This function generates a random artword/praat script"""

    # a list containing all of the articulator parameters barring lungs
    limited_parameters = ['Hyoglossus',
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
    values = [round(random.uniform(0, 1), 1) for x in range(len(limited_parameters))]

    # creates a text file with the .praat extension by calling open and assigns to variable f
    f = open('./{}/test{}.praat'.format(temp_fp, index), 'w')

    f.write('Create Speaker... Robovox Male 2\r\n')
    f.write('Create Artword... Individual{!s} {}\r\n'.format(index, duration))
    f.write('Set target... 0.0  0.18  Lungs\r\n')
    f.write('Set target... 0.1  0.0  Lungs\r\n')
    f.write('Set target... {}   0.0  Lungs\r\n'.format(duration))
    f.write('Set target... 0.0 1 LevatorPalatini\r\n')
    f.write('Set target... {} 1 LevatorPalatini\r\n'.format(duration))
    f.write('Set target... 0.0 0.5 Interarytenoid\r\n')
    f.write('Set target... {} 0.5 Interarytenoid\r\n'.format(duration))

    # a loop that
    for i in range(len(limited_parameters)):
        f.seek(0, 2)
        f.write('Set target... 0.0 {!s} {!s}\r\n'.format(values[i], limited_parameters[i]))
        f.write('Set target... {} {!s} {!s}\r\n'.format(duration, values[i], limited_parameters[i]))

    f.write('select Artword Individual{!s}\r\n'.format(index))
    f.write('plus Speaker Robovox\r\n')
    f.write('To Sound... 22500 25    0 0 0    0 0 0   0 0 0\r\n')
    f.write('''nowarn do ("Save as WAV file...", "Individual{!s}.wav")\r\n'''.format(index))

for i in range(n):
    artword_generator_limited(i)

sleep(1)

def running(i):    
    subprocess.call(['./{}/praat'.format(praat_fp), '--run', './{}/test{!s}.praat'.format(temp_fp,i)])

def pool_setup(n):
    ex = futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    ex.map(running, [i for i in range(n)])
    ex.shutdown()
    print('bye')
pool_setup(n)


"""
if __name__ == '__main__':
    def running(i):    
        subprocess.call(['Praat/Praat.exe', '--run', '/temp/test{!s}.praat'.format(i)])

    def pool_setup(n):
        p = Pool(multiprocessing.cpu_count())
        p.map(running, [i for i in range(n)])
        p.join()
    pool_setup(n)
"""