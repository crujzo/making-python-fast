import time
from multiprocessing import Pool
import math

elementList = list(range(1,100000000))

def run_multiprocessing(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)

def calculate(n):
	return math.pow(math.sqrt(math.pow((n*2),4)/4*math.sqrt((n+5))),1.5)

starttime = time.time()

result = run_multiprocessing(calculate,elementList,12)

print('That took {} seconds'.format(time.time() - starttime))


