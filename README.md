# Modelling and Optimization Project 2

## Proposal

The project proposes the development of an image compression algorithm using K-means clustering to achieve efficient compression while preserving visual quality. The program's core functionality involves grouping similar pixels together using K-means clustering and replacing them with the average color value of the cluster centroid. By reducing the number of unique colors in the image, significant compression can be achieved without compromising the overall visual fidelity.

To illustrate the process, the program will accept an input image and apply K-means clustering to partition the image into clusters of similar colors. Each cluster represents a set of pixels with similar color characteristics. The program then replaces all pixels within each cluster with the average color value of the cluster centroid. This process effectively reduces the number of unique colors in the image, resulting in compression.

The implementation of the algorithm would allow users to interact with a command-line interface where they can input the path to the image that they wish to compress and the desired compression level (number of clusters). The program would then process the image accordingly and save the compressed image to a separate file.

## Introduction

This project is an image compression program that uses K-means clustering to compress images. The user can run the program, select the image they wish to compres and the compression level. The program will then read the image and perform clustering to group the pixels with similar colors. Each pixel is then replaced with the centroid color and saved to a file. By reducing the number of unique colors in the image, compression can be achieved without compromising the overall visual fidelity of the image.

## Implementation Details

The project is implemented in Python. As stated in the proposal, the user can provide the path to the image they wish to compress, the desired compression level, and the path to store the compressed image when running the program. The program will then process the image accordingly.

Here are the descriptions of the three Python files. Furthermore, the code in each file is documented with comments to explain each part in greater detail.

### `process_image.py`

This file contains some helpful functions for image manipulation:

- `read_image` reads an image from a file and returns a 3D matrix of the image's pixel values in a row, column and RGB format.

- `save_image` saves a 3D matrix of pixels in a row, column, and RGB format to a file.

- `compress_image` compresses an image based on the information from k-means clustering. Namely, it replaces each pixel with the centroid color of the cluster it belongs to.

### `k_means.py`

This file contains the main algorithm of the project: k-means clustering. There are two functions in this file:

#### `initialize_centroids`

This function initializes the centroids for clustering. It takes the image and the number of clusters. For each cluster, it randomly chooses $10$ pixels and uses the average of those colors as the initial centroid color.

This is done to get a more representative starting point, especially when the data is noisy. This can help the k-means algorithm converge faster and increase the quality of the compressed image.

#### `k_means`

This function performs the k-means clustering algorithm. It takes in the flattened image, the initalized centroids and the number of clusters.

We do $10$ iterations and for each iteration, there are two main steps:

1. Assign each pixel to the closest centroid. This is done by calculating the Euclidean distance between each pixel and each centroid. The pixel is then assigned to the cluster whose centroid it is closest to.

2. Update the centroids. For each cluster, we calculate the average color of the pixels in the cluster and use that as the new centroid.

After the $10$ iterations, we return the centroids and the labels of the pixels.

### `main.py`

This file is the main runner file. It contains the command-line interface for the user to interact with the program. The user can input the path to the image they wish to compress, the desired compression level, and the path to store the compressed image.

An argument parser is used to get the user's input. This provides helpful information when the user runs the program with the `-h` flag and ensure that the user has provided the input with the correct type. If the user has not provided a compression level, the program will default to $16$ clusters. Similarly, if the user has not provided a path to store the compressed image, the program will default to `compressed.png`.

With the provided arguments, the program will then use the functions defined in the previously mentioned files. It will read the image, initialize the centroids, perform k-means clustering, compress the image, and save the compressed image to a file.

## Further Improvements

An improvement to the program would be to implement a stopping criterion for the k-means algorithm. Currently, the program runs for a fixed number of iterations. However, the algorithm could stop when the centroids don't change anymore or don't change significantly. This would save time and resources, especially for larger images.

Additionally, the program could implement a better way to choose the initial centroids. Currently, the program chooses the initial centroids by randomly selecting $10$ pixels and using the average of those colors. However, a better way to choose the initial centroids could be to use the k-means++ algorithm. This algorithm chooses the initial centroids in a way that makes the algorithm converge faster and increases the quality of the compressed image.

From a purely technical standpoint, there are no assumptions made in this project and the alogithm is guaranteed to work every time, even with larger images and more cluster. However, the program would definitely start to slow down with large images and a large number of clusters.

## How to Run

### Setting up the enviroment

1. Ensure that you have a working install of Python 3.11.7.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program

1. Navigate to the project directory.
2. Make sure that the virtual environment is activated. If it is not, use `source .venv/bin/activate`.
3. Run the program using `python main.py` and pass in the correct arguments.
    - You can use the `-h` flag to see the help message and the available arguments.
4. You must provide the path to the image you wish to compress.
    - For example, you can compress the `rocks.png` image by running `python main.py rocks.png`.
5. Additionally, you can provide the compression level with `--number_of_clusters` and the path to store the compressed image with `--save_path`.
    - If you do not provide the optional arguments, the program will default to $16$ clusters and `compressed.png` respectively.
    - An example command would be `python main.py rocks.png --number_of_clusters 32 --save_path rocks-compressed.png`. This would compress the `rocks.png` image with $32$ clusters and save the compressed image to `rocks-compressed.png`.
    - Another example command would be `python main.py rocks.png --save_path rocks-compressed.png`. This would compress the `rocks.png` image with the default $16$ clusters and save the compressed image to `rocks-compressed.png`.
4. View the compressed image at the path you provided.

