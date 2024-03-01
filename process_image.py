import cv2
import numpy as np


#  Reads and scales the image from the given path.
def read_image(image_path):
    img = cv2.imread(image_path)
    img = img / 255.0
    return img


# Rescales and saves the image to the given path.
def write_image(image_path, image):
    cv2.imwrite(image_path, 255 * image)


# Compresses the image based on the centroid colors and the
# array of which cluster a pixel is assigned to.
def compress_image(centroids, index, img):
    # Assign each pixel to the corresponding centroid color.
    centroid = np.array(centroids)
    compressed = centroid[index.astype(int), :]

    # Reshape the image back to a 3D matrix of row, col, rgb(3).
    return compressed.reshape(img.shape)
