import cv2
import numpy as np


def read_image(image_path):
    img = cv2.imread(image_path)
    img = img / 255.0 # Scaling the image
    return img


def write_image(image_path, image):
    cv2.imwrite(image_path, 255 * image)


def compress_image(centroids, index, img):
    # Assign each pixel to the corresponding centroid
    centroid = np.array(centroids)
    compressed = centroid[index.astype(int), :]

    # Reshape back to the 3D matrix (row, col, rgb(3))
    return compressed.reshape(img.shape)
