import argparse
from process_image import read_image, compress_image, write_image
from k_means import initialize_centroids, k_means

# Make the parser to handle command line arguments for user input.
parser = argparse.ArgumentParser("main")
parser.add_argument(
    "image_path",
    type = str,
    help = "the path of the image to be compressed")
parser.add_argument(
    "--number_of_clusters",
    type = int,
    default = 16,
    help = "number of clusters (colors)")
parser.add_argument(
    "--save_path",
    type = str,
    default = "compressed.jpg",
    help = "the path to save the compressed image")
args = parser.parse_args()

# Get the user input from the argument parser.
input_path = args.image_path
clusters = args.number_of_clusters
output_path= args.save_path

# Read the image from the file, initialise the centroids,
# perform k-means, compress the image using the clusters, and
# save the image.
img = read_image(input_path)
points, centroids = initialize_centroids(img, clusters)
centroids, index = k_means(points, centroids, clusters)
compressed = compress_image(centroids, index, img)
write_image(output_path, compressed)
