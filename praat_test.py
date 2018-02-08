# This script generates n random artwords of a given duration for synthesisng with praat.
# It is intended to give a rough estimate as to the single vs parallel performance.
# Outputs a the total time, plus a rough how much faster than realtime simulation is.

import subprocess
import random
import time
import os
import shutil

import multiprocessing
from concurrent import futures

# set number of artwords to be generated. should be equal to at least the number of threads available
n = 10

# set the duration of each artword sound
duration = '1.0'

# praat folder location
praat_fp = 'Praat'

# set the name of the temporary directory
temp_fp = 'temp'


def artword_generator(index):
    #This function generates a random artword/praat script

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
    f.write('select Artword Individual{!s}\r\n'.format(index))
    f.write('plus Speaker Robovox\r\n')
    f.write('To Sound... 22500 25    0 0 0    0 0 0   0 0 0\r\n')
    f.write('''nowarn do ("Save as WAV file...", "Individual{!s}.wav")\r\n'''.format(index))
    f.write('''selectObject ("Sound Individual''' + str(index) + '''_Robovox")\r\n''')
    f.write('To Formant (burg): 0, 5, 5000, 1.0, 50\r\n')
    f.write('List: "no", "yes", 6, "no", 3, "no", 3, "no"\r\n')
    f.write('''appendFile ("formants''' + str(index) + '''.txt", info$ ())\r\n''')
    f.write('''selectObject ("Sound Individual''' + str(index) + '''_Robovox")\r\n''')
    f.write('To Pitch: 1.0, 75, 600\r\n')
    f.write('Get mean: 0, 0, "Hertz"\r\n')
    f.write('''appendFile ("pitch''' + str(index) + '''.txt", info$ ())\r\n''')
    f.write('''selectObject ("Sound Individual''' + str(index) + '''_Robovox")\r\n''')
    f.write('To Intensity: 100, 0, "yes"\r\n')
    f.write('Get standard deviation: 0, 0\r\n')
    f.write('''appendFile ("intensity''' + str(index) + '''.txt", info$ ())\r\n''')


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





def praat_serial():
    start = time.time()
    for i in range(n):
        subprocess.run(['./{}/praat'.format(praat_fp), '--run', './{}/test{!s}.praat'.format(temp_fp,i)])
    end = round(time.time() - start, 2)

    print('Total time to synthesise {!s} sounds of duration {} in seconds = {!s}'.format(n, duration, end))
    print('This is equivalent to ', round(n * float(duration) / end, 2), 'x real time')


def praat_parallel():
    start = time.time()
    for i in range(n):
        p = subprocess.Popen(['./{}/praat'.format(praat_fp), '--run', './{}/test{!s}.praat'.format(temp_fp,i)])

    p.communicate()
    end = round(time.time() - start, 2)

    print('Total time to synthesise {!s} sounds of duration {} in seconds = {!s}'.format(n, duration, end))
    print('This is equivalent to ', round(n * float(duration) / end, 2), 'x real time')

    time.sleep(4)

def running(i):    
    subprocess.call(['./{}/praat'.format(praat_fp), '--run', '--ansi', './{}/test{!s}.praat'.format(temp_fp,i)], stdout=subprocess.DEVNULL)

def pool_setup(n):
    start = time.time()
    ex = futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    ex.map(running, [i for i in range(n)])
    ex.shutdown()
    end = round(time.time() - start, 2)
    
    print('Total time to synthesise {!s} sounds of duration {} in seconds = {!s}'.format(n, duration, end))
    print('This is equivalent to ', round(n * float(duration) / end, 2), 'x real time')


os.mkdir(temp_fp)
for i in range(n):
    artword_generator(i)

pool_setup(n)
shutil.rmtree(temp_fp)