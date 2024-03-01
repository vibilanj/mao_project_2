import sys
from process_image import read_image, compress_image, write_image
from k_means import initialize_centroids, k_means

# img = read_image(sys.argv[1])
# clusters = sys.argv[2]

# write_image("rocks_alt.png", img)

img = read_image("rocks.png")

# Clusters are the number of colors that we choose
clusters = 32

points, centroids = initialize_centroids(img, clusters)
centroids, index = k_means(points, centroids, clusters)
compressed = compress_image(centroids, index, img)

write_image("rocks-compressed.png", compressed)
