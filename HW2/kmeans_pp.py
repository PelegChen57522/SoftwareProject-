import sys
import numpy as np
import pandas as pd
import mykmeanssp

def kmeanspp_init(data, k):
    data_np = data.to_numpy()  
    np.random.seed(0)
    centroids_idx = [np.random.choice(len(data_np))]
    centroids = [list(data_np[centroids_idx[0]])] 

    for _ in range(1, k):
        dist_sq = np.array([min([0 if np.array_equal(x, c) else np.linalg.norm(x - c) for c in centroids]) for x in data_np])
        probs = dist_sq / dist_sq.sum()
        i = np.random.choice(len(data_np), p=probs)
        
        centroids_idx.append(i)
        centroids.append(list(data_np[i]))

    return centroids_idx, centroids


def main(k, iter, eps, file1, file2):
    try:
        df1 = pd.read_csv(file1,index_col = 0, header = None)
        df2 = pd.read_csv(file2,index_col = 0, header = None)
        data = pd.merge(df1, df2, left_on=df1.index, right_on=df2.index).sort_values(by="key_0", ascending=True).iloc[:,1:]

        N = len(data)

        if k >= N:
            print("Invalid number of clusters!")
            sys.exit()


        initial_centroids_idx, initial_centroids = kmeanspp_init(data, k)
        
        
        data = [x.tolist() for index, x in data.iterrows()]
        final_centroids = mykmeanssp.fit(data,initial_centroids, k, iter,eps)
        print(",".join(str(x) for x in initial_centroids_idx))
        for center in final_centroids:
            print(",".join(str("{:.4f}".format(round(x, 4))) for x in center))

    except:
        print("An Error Has Occurred")


if __name__ == '__main__':
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print("An Error Has Occurred")
        sys.exit()

    k = int(sys.argv[1])
    if k < 1:
        print("Invalid number of clusters!")
        sys.exit()

    if len(sys.argv) == 6:
        iter = int(sys.argv[2])
        if iter < 1 or iter > 1000:
            print("Invalid maximum iteration!")
            sys.exit()
        eps = float(sys.argv[3])
        file1 = sys.argv[4]
        file2 = sys.argv[5]
    else:
        iter = 300  # default value
        eps = float(sys.argv[2])
        file1 = sys.argv[3]
        file2 = sys.argv[4]

    main(k, iter, eps, file1, file2)
