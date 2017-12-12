import numpy as np
import scipy
from math import log

dataDir = 'DataMatrix/'
read1 = dataDir + 'recOutput.txt'
read2 = dataDir + 'T_rand.txt'
read3 = dataDir + 'randSecondHalf.txt'
read4 = dataDir + 'randAll.txt'
read5 = dataDir + 'randFirstHalf.txt'
output_file = dataDir + 'ens2.txt'
a1 = ((2*0.8377)-1)
a2 = ((2*0.5011)-1)
a3 = ((2*0.6927)-1)
a4 = ((2*0.5483)-1)
a5 = ((2*0.5499)-1)


s1 = np.genfromtxt(read1)
tmp1 = s1*a1
s2 = np.genfromtxt(read2)
tmp2 = s2*a2
s3 = np.genfromtxt(read3)
tmp3 = s3*a3
s4 = np.genfromtxt(read4)
tmp4 = s4*a4
s5 = np.genfromtxt(read5)
tmp5 = s5*a5

sopt = tmp1+tmp2
print max(sopt)

fOut = open(output_file, 'w')
for outstr in sopt:
	if outstr > 0.5:
	    fOut.write(str(1) + '\n')
	else:
		fOut.write(str(0) + '\n')
    
fOut.close()
#temp = np.dot(t1.T, t1)
