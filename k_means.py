import numpy as np


def initialize_means(img, clusters):
    # Flatten image into a 2D matrix
    points = img.reshape((-1, img.shape[2]))
    m, n = points.shape

    # Clusters are the number of color (cluster) that we choose.

    # Centroids is the array of assumed centroids (means)
    centroids = np.zeros((clusters, n))

    # Randomly initialize the centroids
    for i in range(clusters):
        rand_indices = np.random.choice(m, size = 10, replace = False)
        centroids[i] = np.mean(points[rand_indices], axis = 0)

    return points, centroids


def distance(x1, y1, x2, y2):
    return np.sqrt((np.square(x2 - x1)) + np.square(y2 - y1))


def k_means(points, centroids, clusters):
    iterations = 10
    m, n = points.shape

    # These are the index values corresponding to the cluster to which pixel
    # belongs.
    index = np.zeros(m)

    # K-means algorithm
    while iterations > 0:
        for j in range(m):
            # Initialize minimum value to a large value
            min_dist = float("inf")
            temp = None

            for k in range(clusters):
                x1, y1 = points[j, 0], points[j, 1]
                x2, y2 = centroids[k, 0], centroids[k, 1]

                dist = distance(x1, y1, x2, y2) 
                if dist <= min_dist:
                    min_dist = dist
                    temp = k
                    index[j] = k

        for k in range(clusters):
            cluster_points = points[index == k] 
            if len(cluster_points) > 0:
                centroids[k] = np.mean(cluster_points, axis = 0)

        iterations -= 1

    return centroids, index
