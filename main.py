from process_image import read_image, compress_image, write_image
from k_means import initialize_means, k_means


# Read the rocks image
img = read_image("images/rocks.jpg")

clusters = 32

points, centroids = initialize_means(img, clusters)
centroids, index = k_means(points, centroids, clusters)
compressed = compress_image(centroids, index, img)

write_image("compressed.jpg", compressed)
