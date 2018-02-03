import subprocess
import multiprocessing
from multiprocessing import Pool

def running(i):    
    subprocess.call(['Praat/Praat.exe', '--run', '/temp/test{!s}.praat'.format(i)])


def pool_setup(n):
    p = Pool(multiprocessing.cpu_count())
    p.map(running, [i for i in range(n)])
    p.join()