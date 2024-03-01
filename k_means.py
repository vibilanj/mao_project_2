import numpy as np


# Initialize the centroids for the image.
def initialize_centroids(img, clusters):
    # Flatten the image from a 3D matrix to a 2D matrix of
    # rgb(3) values.
    points = img.reshape((-1, img.shape[2]))
    m, n = points.shape

    # The array of assumed centroids (means) for k-means
    centroids = np.zeros((clusters, n))

    # Initialize the centroids by randomly choosing 10 pixels and
    # calculating the mean color of the 10 pixels.
    for i in range(clusters):
        rand_indices = np.random.choice(m, size = 10, replace = False)
        centroids[i] = np.mean(points[rand_indices], axis = 0)

    # Return the flattened image and the initialized centroids
    return points, centroids


# Performs the k-means algorithm on the image.
def k_means(points, centroids, clusters):
    # Number of iterations for the k-means algorithm.
    iterations = 10

    # Stores the index of the cluster to which each pixel is assigned.
    m, _ = points.shape
    index = np.zeros(m)

    # Perform the k-means iterations.
    while iterations > 0:
        # Assign the points to the clusters.
        for j in range(m):
            # Calculate the Euclidean distances from the j-th pixel to each
            # centroid.
            dists = np.sqrt(((points[j] - centroids) ** 2).sum(axis = 1))

            # Assign the j-th pixel to the cluster whose centroid it is
            # closest to.
            index[j] = dists.argmin()

        # Update the centroids for each cluster.
        for k in range(clusters):
            # Get the points that are assigned to the k-th cluster.
            cluster_points = points[index == k]

            # If the k-th cluster is not empty, update its centroid to be
            # the mean of the points assigned to it.
            if len(cluster_points) > 0:
                centroids[k] = np.mean(cluster_points, axis = 0)

        iterations -= 1

    # Return the final centroids and the mapping of each pixel to its
    # centoid.
    return centroids, index
