
import math
from numba import vectorize
import numpy as np
import time

@vectorize(['float32(float32)','float64(float64)'], target='parallel')
def calculate(n):
	return math.pow(math.sqrt(math.pow((n*2),4)/4*math.sqrt((n))),1.5)

# Prepare input of hundred million entries
elementList = np.array(list(range(1,100000000)),dtype=np.float64)

starttime = time.time()

result = calculate(elementList)

print('That took {} seconds'.format(time.time() - starttime))


