import sys
import numpy as np
import pandas as pd
#import mykmeanssp

def kmeanspp_init(data, k):
    np.random.seed(0)
    centroids_idx = [np.random.choice(len(data))]
    centroids = [data[centroids_idx[0]]]

    for _ in range(1, k):
        dist_sq = np.array([min([np.linalg.norm(x - c) ** 2 for c in centroids]) for x in data])
        probs = dist_sq / dist_sq.sum()
        cumulative_probs = probs.cumsum()
        r = np.random.rand()

        for j, p in enumerate(cumulative_probs):
            if r < p:
                i = j
                break

        centroids_idx.append(i)
        centroids.append(data[i])

    return centroids_idx, centroids


def main(k, iter, eps, file1, file2):
    try:
        df1 = pd.read_csv(file1, sep=" ", header=None, dtype={0: int, 1: float})
        df2 = pd.read_csv(file2, sep=" ", header=None, dtype={0: int, 1: float})

        df = pd.merge(df1, df2, on=0, how='inner')
        df.sort_values(by=[0], inplace=True)

        data = df.values[:, 1:]
        N = len(data)

        if k >= N:
            print("Invalid number of clusters!")
            sys.exit()

        initial_centroids_idx, initial_centroids = kmeanspp_init(data, k)



        final_centroids = mykmeanssp.fit(initial_centroids, data, eps, iter)

        print(','.join(map(str, df.iloc[initial_centroids_idx, 0].values)))
        for centroid in final_centroids:
            print(','.join(map(lambda x: f'{x:.4f}', centroid)))
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
