# import sys
# import math
#
# epsilon=0.001
# maxIter=1000
#
# def Kmeans(K,iter,inputFileData,outputFileData):
#
#
#     dataPoints=[] #the N datapoints x1, ... , xN
#     N=-1 #number of datapoints that were given
#     prevCentroids=[] #the unupdated centroids u1, ... , uK
#     newCentroids=[] #the updated centroids u1, ... , uK
#
#     # Read the data directly from the file
#     fileOpener = open(inputFileData, "r") #"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
#     #take the date points into the lists
#     #Initialize centroids as first k datapoints: µk = xk, ∀k ∈ K
#
#     initializeKCentroids=0
#     while True:
#         currentLine = fileOpener.readline()
#         if currentLine == '': # there is no more data points
#             break
#         currDataPoint=[float(x) for x in currentLine.split(",")]
#         dataPoints.append(currDataPoint)  #put the all datapoints in "dataPoints" list
#         if  initializeKCentroids < K:  #Initialize centroids as first k datapoints: µk = xk, ∀k ∈ K
#             newCentroids.append(currDataPoint)
#             prevCentroids.append(currDataPoint)
#         initializeKCentroids += 1
#     fileOpener.close()
#
#     #update number of centroids
#     N= len(dataPoints)
#
#     #check if 1 < K < N, K ∈ N
#
#     if (K>1 and K<N)==False:
#         print("Invalid number of clusters!")
#         sys.exit()
#
#
#     for i in range(iter):
#
#         for j in range(N):
#
#         #Assign every xi to the closest cluster k: argmin d(xi, µk), ∀k 1 ≤ k ≤ K
#
# #
# # def EuclideanDistance():
# #
# # def updateCentroids():
#
#
#
# def main(argv):
#     if(len(argv)!=3 or len(argv)!=4):
#         print("Inavlid Input!")
#         sys.exit()
#
#     if (len(argv) == 4):  # argument "iter" has been given by user
#         # checking if the first 2 arguments (K, maxIter) are integers
#         if(argv[1].isnumeric()==False or argv[2].isnumeric()==False):
#             print("Inavlid Input!")
#             sys.exit()
#         else:
#             iter=(int)(argv[2])
#
#     if (len(argv) == 3):  # argument "iter" has not been given by user
#         # checking if  K is integer
#         if (argv[1].isnumeric() == False or argv[2].isnumeric() != False):
#             print("Inavlid Input!")
#             sys.exit()
#
#     if(iter <= 0):
#         print("Inavlid Input!")
#         sys.exit()
#
#     K = (int)(argv[1])
#
#     if (len(argv) == 3):  # argument "iter" has been given by user
#         defaultIter=200
#         return Kmeans(K, defaultIter, argv[3], argv[4])
#     return Kmeans(K, iter, argv[2], argv[3])
#
#
# if __name__ == '__main__':
#     main(sys.argv)
#
#
#
#
