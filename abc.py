import numpy as np
np1 = np.genfromtxt('abc.txt', 'int64', delimiter=' ', encoding="utf-8",skip_header=1)
print( np.sum( np1 ) )