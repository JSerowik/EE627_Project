import math
from random import *

import numpy as np



dataDir = 'DataMatrix/'
file = 'Sopt.txt'
output_file = dataDir + 'zeros.txt'
#T = open(file, 'r')

'''def sigmoid(x, med):
    return 1 / (1 + math.exp(-(x-med)))

data = []
for line in fT:
	data.append(float(line)) 
fT.close()
tmpNp = np.array(data)
median =  np.median(tmpNp)
sigData = []
for item in data:
    sigData.append(np.round(sigmoid(item, median)))'''

data = []
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))
for x in range(0, 9429):
	data.append(randint(0,1))

print len(data)
fOut = open(output_file, 'w')
for outstr in data:
	fOut.write(str(outstr) + '\n')
    
fOut.close()