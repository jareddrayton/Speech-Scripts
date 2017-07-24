# This script generates n random artwords with a duration of 1 second for synthesisng with praat.
# This gives a rough estimate as to the performance with the Genetic Algorithm
# Outputs a the total time, plus a rough how much faster than realtime simulation is.

import subprocess
import random

n = 100

length = '1.0'

# define praat location

def artword_generator(index):
    """This function generates a random artword/praat script"""

    # List of articulator parameters
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
    [round(random.uniform(-1, 1), 1) for x in range(len(parameters))]


    f = open("wdwd.praat", 'w')

    f.write("test")
    f.write("test")
    f.write('Create Speaker... Robovox Male 2\r\n')
    f.write('Create Artword... Individual' + str(index) + ' ' + length + '\r\n')
    f.write('Set target... 0.0  0.07  Lungs\r\n')
    f.write('Set target... 0.04  0.0  Lungs\r\n')
    f.write('Set target... %s   0.0  Lungs\r\n' % length)
    f.write('Set target... 0.00 1 LevatorPalatini\r\n')
    f.write('Set target... ' + length + ' 1 LevatorPalatini\r\n')

    for i in range(len(self.parameters)):
        f.seek(0, 2)
        f.write('Set target... 0.0 ' + str(self.values[i]) + ' ' + self.parameters[i] + '\r\n')
        f.write('Set target... ' + length + ' ' + str(self.values[i]) + ' ' + self.parameters[i] + '\r\n')

    f.write('select Artword Individual' + self.name + '\r\n')
    f.write('plus Speaker Robovox\r\n')
    f.write('To Sound... 22500 25    0 0 0    0 0 0   0 0 0\r\n')
    f.write('''nowarn do ("Save as WAV file...", "Individual''' + self.name + '''.wav")\r\n''')



# Generate n number of artowrds
index = 1

artword_generator(index)


for i in range(0, n):
    print(i)


def parallel():
    subprocess.run(praat - -run)

    pass


artword_generator()

print()
