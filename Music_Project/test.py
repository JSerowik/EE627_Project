import math
import numpy as np

def sigmoid(x, med):
    return 1 / (1 + math.exp(-(x-med)))

dataDir = 'DataMatrix/'
file = 'Sopt.txt'
output_file = dataDir + 'Sout.txt'
fT = open(file, 'r')

data = []
for line in fT:
	data.append(float(line)) 
fT.close()
tmpNp = np.array(data)
median =  np.median(tmpNp)
sigData = []
for item in data:
    sigData.append(np.round(sigmoid(item, median)))

'''fOut = open(output_file, 'w')
for outstr in temp:
	fOut.write(str(outstr) + '\n')
    
fOut.close()'''