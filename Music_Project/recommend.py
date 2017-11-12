import numpy
# Specifiy the file locations of where to read the inputs from
# And where to output the recommendations
dataDir = 'DataMatrix/'
file_name_test = dataDir + 'testTrack_hierarchy.txt'
file_name_train = dataDir + 'trainIdx2_matrix.txt'
output_file = dataDir + 'recOutput.txt'
fOut = open(output_file, 'w')
# Function for organizing data into matrix to be processed
def dataManage(file_Test, file_Train):
    fTest = open(file_Test, 'r')
    fTrain = open(file_Train, 'r')
    Trainline = fTrain.readline()
    genre_vec = [[]for i in range(6)]
    # Empty vectors to assign hierachy attributes
    trackID_vec = [0]*6
    albumID_vec = [0]*6
    artistID_vec = [0]*6
    lastUserID =- 1
    # Add padding to user rating matrix because some songs have multiple genres
    user_rating_inTrain = numpy.zeros(shape=(6,36))
    textOut = []
    for line in fTest:
        arr_test = line.strip().split('|')
        line_length = len(arr_test)
        userID = arr_test[0]
        trackID = arr_test[1]
        albumID = arr_test[2]
        artistID = arr_test[3]
        user_int = int(userID)
        if userID != lastUserID:
            ii = 0
            user_rating_inTrain=numpy.zeros(shape=(6,36))
        trackID_vec[ii] = trackID
        albumID_vec[ii] = albumID
        artistID_vec[ii] = artistID
        for j in range(4,(line_length)):
            genre_vec[ii].append(arr_test[j])
        ii = ii + 1
        lastUserID = userID
        # Inputs 6 lines at a time
        if ii == 6 :
            while (Trainline):
                arr_train = Trainline.strip().split('|')
                trainUserID = arr_train[0]
                trainItemID = arr_train[1]
                trainRating = arr_train[2]
                Trainline = fTrain.readline()
                trainUser_int = int(trainUserID)

                if trainUser_int < user_int:
                    continue
                # Inputs scores into a matrix
                if trainUser_int == user_int:
                    for nn in range(0, 6):
                        length = len(genre_vec[nn]) 
                        if trainItemID == albumID_vec[nn]:
                                user_rating_inTrain[nn, 0] = trainRating
                        if trainItemID == artistID_vec[nn]:
                                user_rating_inTrain[nn, 1] = trainRating
                        for jj in range(0,length):
                                if trainItemID == genre_vec[nn][jj]:
                                        user_rating_inTrain[nn,(jj+2)] = trainRating
                # Outputs the scores after user changes
                if trainUser_int > user_int:
                    for nn in range(0, 6):
                        length = len(genre_vec[nn])
                        endStr = []
                        for gen in range(0,length):                                                
                                endStr.append(str(user_rating_inTrain[nn, (gen+2)]))
                        
                        outStr = [str(userID), str(trackID_vec[nn]), str(user_rating_inTrain[nn,0]), str(user_rating_inTrain[nn, 1])]
                        outStr = outStr + endStr
                        textOut.append(outStr)
                    genre_vec = [[]for i in range(6)]
                    break
    fTest.close()
    fTrain.close()
    return textOut
# Function that find the user rating averages and outputs recommendations
def averageScores(matIn):
    cnt = 0
    outstr = ''
    scoreOut = []
    avgList = [0]*36
    outList = [0]*6
    avgList[0] = 1
    avgList[1] = 1
    pt=numpy.zeros(shape=(6,1))
    # avgList contain the rated averages based on the song hierarchy
    for line in matIn:
        sumList = 0
        count = 2
        lineLen = len(line)
        userID = line[0]
        trackID = line[1]
        # avg is the average value of a song as rated by that user
        # We sum up the averages to be able to recommend other like songs
        for j in range(2,36):
            if lineLen == 4:
                avgList[j] = 0
            else:
                avgList[j] = 1     
        for i in range(2,lineLen):
            score = float(line[i])
            sumList += score * avgList[i-2]
            if score != 0:
                count = count+1
        avg = 0
        if sumList == 0:
            avg = 0
        else:
            avg = (sumList/(count-1))
        scoreOut.append(float(avg))
    # Outputs the highest three values in scoreOut as 1s
    for line in scoreOut:
        outList[cnt] = line
        cnt = cnt + 1
        if cnt == 6:
            cnt = 0
            for ll in range(0,3):
                for nn in range(0,6):
                    if outList[nn] == max(outList):
                        pt[nn,0] = 1
                        outList[nn] =- 188580
                        break
            # Output the list of 1s to the specified txt file
            for index in range(0,6):
                outstr = str(int(pt[index,0]))
                fOut.write(outstr + '\n')
        outstr = ''
        pt = numpy.zeros(shape=(6,1))

p1 = dataManage(file_name_test, file_name_train)
print len(p1)
averageScores(p1)
fOut.close()