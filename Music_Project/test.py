import random

dataDir = 'DataMatrix/'
output_file = dataDir + 'T_rand2.txt'

temp = []
for x in range(0, 94290):
	temp.append(random.randint(0, 1))
print len(temp)

fOut = open(output_file, 'w')
for outstr in temp:
	fOut.write(str(outstr) + '\n')
    
fOut.close()