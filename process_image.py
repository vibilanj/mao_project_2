import numpy as np
import matplotlib.pyplot as plt
import cv2


def read_image(image_path):
    img = cv2.imread(image_path)
    img = img / 255.0 # Scaling the image
    return img
