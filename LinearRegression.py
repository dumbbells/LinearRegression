import math

def trainData(trainingData):
    meanX = sum([entry[0] for entry in trainingData]) / float(len(trainingData))
    meanY = sum([entry[1] for entry in trainingData]) / float(len(trainingData))
    top = 0
    bottom = 0
    for i in range(len(trainingData)):
        top += (trainingData[i][0] - meanX) * (trainingData[i][1] - meanY)
        bottom += (trainingData[i][0] - meanX) ** 2
    b1 = top / bottom
    b0 = meanY - (b1 * meanX)
    return b0, b1

def getRMSE(b0, b1, data, lam):
    rmse = 0
    for i in range(len(data)):
        yHat = b0 + b1 * data[i][0]
        rmse += (data[i][1] - yHat) ** 2
    penalty = lam * b0 ** 2 + lam * b1 ** 2
    return  math.sqrt(rmse/len(data)) + penalty

with open("data.txt") as file:
    masterData = []
    for line in file:
        masterData.append([float(x) for x in line.split()])
lambdas = [0.1, 1, 10, 100]
portion = int(len(masterData) / 3)
bestRMSE = 1000000
bestLambda = 0
bestWeights = []
for groups in range(len(lambdas)):
    bestWeights.append([0,0])
    print("\t<-----lambda {}----->".format(lambdas[groups]))
    totalRMSE = 0
    for trial in range(3):
        localBestRMSE = 1000000
        data = list(masterData)
        testData = []
        for split in range(trial * portion, portion * (trial + 1)):
            testData.append(masterData[split])
            data.remove(masterData[split])
        b0, b1 = trainData(data) 
        rmse = getRMSE(b0, b1, testData, lambdas[groups])
        if (localBestRMSE > rmse):
            bestWeights[groups] = [b0, b1]
        totalRMSE += rmse
        print("Weights:\n\tw0: {}\n\tw1: {}\nRMSE: {}\n".format(b0, b1, rmse))
    print("Total RMSE: {}\n".format(totalRMSE))
    if (totalRMSE < bestRMSE):
        bestRMSE = totalRMSE
        bestLambda = groups
print("Best Lambda is: {} ".format(lambdas[bestLambda]))
b0, b1 = bestWeights[bestLambda]
rmse = getRMSE(b0, b1, masterData, lambdas[bestLambda])
print("Weights:\n\tw0: {}\n\tw1: {}\nRMSE: {}\n".format(b0, b1, rmse))
