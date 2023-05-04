import sys
import math
Epsilon=0.001



def InitalizeKMeans(K,iter,inputFileData):

    dataPoints = []  # the N datapoints x1, ... , xN
    N = -1  # number of datapoints that were given
    prevCentroids = []  # the unupdated centroids u1, ... , uK
    newCentroids = []  # the updated centroids u1, ... , uK
    CentroidsSizeList = [0 for i in range(K)]

    # Read the data directly from the file
    fileOpener = open(inputFileData,"r")  # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    # take the date points into the lists
    # Initialize centroids as first k datapoints: µk = xk, ∀k ∈ K

    initializeKCentroids = 0
    while True:
        currentLine = fileOpener.readline()
        if currentLine == '':  # there is no more data points
            break
        currDataPoint = [float(x) for x in currentLine.split(",")] #datapoint
        dataPoints.append(currDataPoint)  # put the all datapoints in "dataPoints" list
        if initializeKCentroids < K:  # Initialize centroids as first k datapoints: µk = xk, ∀k ∈ K
            newCentroids.append(currDataPoint)
            prevCentroids.append(currDataPoint)
        initializeKCentroids += 1
    fileOpener.close()

    # update the number of datapoints that were given
    N = len(dataPoints)

    # check if 1 < K < N

    if (K > 1 and K < N) == False:
        print("Invalid number of clusters!")
        sys.exit()

    return mainKMeans(K,iter,dataPoints,N,prevCentroids,newCentroids,CentroidsSizeList)



def mainKMeans(K,iter,dataPoints,N,prevCentroids,newCentroids,CentroidsSizeList):
    # for each 0<=i<N data_points_cluster[i]=S for s is the cluster of xi
    datapointsCluster = [0 for i in range(N)]

    for iteration in range(iter):
        for i in range(N) :
            datapointsCluster[i]=findClosestCluster(dataPoints[i],newCentroids) #Assign every xi to the closest cluster k: argmind(xi, µk), ∀k 1 ≤ k ≤ K
            CentroidsSizeList[datapointsCluster[i] - 1] += 1

        newCentroids = [[float(0) for i in range(len(dataPoints[0]))]for j in range(K)]

        # calculate updated clusters
        for i in range(len(dataPoints)):
            addVectors(newCentroids[datapointsCluster[i]-1], dataPoints[i], len(dataPoints[0]))
        for i in range(len(newCentroids)):
            divVectors(newCentroids[i], CentroidsSizeList[i], len(dataPoints[0]))

        CentroidsSizeList = [0 for i in range(K)]

        if (checkEuclideanDistanceEpsilon==False): #until convergence: (∆µk < epsilon)
            break;

        updateOldCentroid(newCentroids, prevCentroids,K)


    #printing!!


    # writing K centroids with 4 digits after the point to the output file
    Centroids_array = [['%.4f' % (newCentroids[j][i]) for i in range(len(dataPoints[0]))] for j in range(K)]

    for mean in Centroids_array:
        for i in range(len(dataPoints[0])):
            if i != (len(dataPoints[0]) - 1):
                print(str(mean[i]) + ",")
            else:
                print(str(mean[i]) + "\n")




#compute the Euclidean Distance between 2 vectors
def EuclideanDistance(v1,v2):
    assert len(v1)==len(v2)
    sum=0
    for i in range(len(v1)):
        sum+=(math.pow()(v1[i]-v2[i]),2)
    res=math.sqrt(sum)
    return res


#function that find the closeset cluster of datapoint
def findClosestCluster(dataPoint,CentroidsList):
    meanIndex = 0
    minSum = math.inf
    index = 0
    for mean in CentroidsList:
        index += 1
        sum =EuclideanDistance(dataPoint,mean)
        if sum <= minSum:
            minSum = sum
            meanIndex = index
    return meanIndex

# updating the centroids by summing and dividing them by their size
def addVectors(mean, data_point, dimension):
    for i in range(dimension):
        mean[i] += data_point[i]


def divVectors(mean, clusterSize, dimension):
    if clusterSize != 0:
        for i in range(dimension):
            mean[i] = mean[i] / clusterSize



def checkEuclideanDistanceEpsilon(newCentroids, prevCentroids,K):
    for i in range(K):
        if ((EuclideanDistance(newCentroids[i],prevCentroids[i])>=Epsilon)==False):
            return False
        else:
            return True

def updateOldCentroid(newCentroids, oldCentroids,K):
    for i in range(K):
        for j in range(len(newCentroids[0])):
            oldCentroids[i][j] = newCentroids[i][j]


def main(argv):
    print(argv)
    print(len(argv))
    if (len(argv) < 3 or len(argv) > 4): #the user gives less/more inputs from what we need
        print("check1")
        print("Inavlid Input!")
        sys.exit()

    if (len(argv) == 4):  # argument "iter" has been given by user
        # checking if the first 2 arguments (K, iter) are integers
        print("check4")
        if (argv[1].isnumeric() == False or argv[2].isnumeric() == False):
            print("Inavlid Input!")
            sys.exit()
        if (((int)(argv[2]) <= 0) or  ((int)(argv[2]) >= 1000)):#check the number of iterations were given
            print("Inavlid Input!")
            sys.exit()
        else:
            K = (int)(argv[1])
            iter = (int)(argv[2])
            return InitalizeKMeans(K, iter,argv[3])

    if (len(argv) == 3):  # argument "iter" has not been given by user
        # checking if  K is integer
        if (argv[1].isnumeric() == False):
            print("Inavlid Input!")
            sys.exit()
        else:
            K = (int)(argv[1])
            iter = 200 #default
            return InitalizeKMeans(K, iter, argv[2])

if __name__ == '__main__':
    main(sys.argv)