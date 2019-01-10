import csv
import numpy

with open('train.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    numberOfRows = sum(1 for row1 in readCSV)
with open('train.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    r = 0
    i = 0
    j = 0
    print(numberOfRows)
    features = numpy.zeros((numberOfRows,58))
    print(features)
    print()
    for row in readCSV:
        for i in range(58):
            if row[i] == "1.0":
                features[r][i] = 1
        r += 1
    pSpam = sum(features[:,57])/(numberOfRows - 1)
#    pNotSpam = 1 - pSpam
    pFeatureSpam = numpy.zeros(57)
    pFeature = numpy.zeros(57)
#    pFeatureNotSpam = numpy.zeros(57)
    for j in range(numberOfRows):
        for n in range(57):
            pFeature[n] += features[j][n]
        if features[j][57] == 1:
            for k in range(57):
                pFeatureSpam[k] += features[j][k]
        # if features[j][57] == 0:
        #     for k in range(57):
        #         pFeatureNotSpam[k] += features[j][k]
    for l in range(57):
        pFeatureSpam[l] /= sum(features[:,57])
        pFeature[l] /= numberOfRows
        # pFeatureNotSpam[l] /= numberOfRows
    print(pFeatureSpam)
    # print(pFeatureNotSpam)
    print(pSpam)
    print()
    print(features)
    numpy.savetxt("features.csv", features, delimiter=",")
with open('test.csv') as csvfile:
    readCSV2 = csv.reader(csvfile, delimiter=',')
    numberOfTestRows = sum(1 for row2 in readCSV2)
with open('test.csv') as csvfile:
    result = numpy.zeros(numberOfTestRows)
    readCSV2 = csv.reader(csvfile, delimiter=',')
    r = 0
    for row in readCSV2:
        isSpamUp = pSpam
        isSpamDown = 1
        # isNotSpam = pNotSpam
        for i in range(57):
            if row[i] == "1.0":
                isSpamUp *= pFeatureSpam[i]
                isSpamDown *= pFeature[i]
            # if row[i] == "0.0":
            #     isNotSpam *= pFeatureNotSpam[i]
        # if (isSpam > isNotSpam):
        #     result[r] = 1
        # if (isSpamUp/isSpamDown) > 0.5:
        #     result[r] = 1
        result[r] = isSpamUp/isSpamDown
        if result[r] > 0.5:
            result[r] = 1
        else:
            result[r] = 0
        r += 1
    result = numpy.delete(result, 0, axis=0)
    print(result)
    numpy.savetxt("SPM_9531031.csv", result, delimiter=",")
