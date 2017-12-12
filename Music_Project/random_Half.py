import random

dataDir = 'DataMatrix/'
read_file = dataDir + 'recOutput.txt'
output_file = dataDir + 'randAll2.txt'
data = []
fTrain = open(read_file, 'r')
for line in fTrain: 
	data.append(int(line)) 
fTrain.close()

cnt = 0
ct0 = 0
ct1 = 0
index = 0
print len(data)
for x in range(0, 94290):
    if cnt < 6:
        if ct0 == 3:
            data[x] = 1
        elif ct1 == 3:
            data[x] = 0
        else:
        	temp = random.randint(0, 1)
        	data[x] = temp
        	if temp == 1:
        	    ct1 += 1
        	else:
        		ct0 += 1
        cnt += 1
    else:
    	cnt = 0
    	ct0 = 0
    	ct1 = 0

print cnt, ct0, ct1
fOut = open(output_file, 'w')
for outstr in data:
     fOut.write(str(outstr) + '\n')
fOut.close()