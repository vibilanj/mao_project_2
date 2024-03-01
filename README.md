# Modelling and Optimization Project 2

## Proposal

The project proposes the development of an image compression algorithm using K-means clustering to achieve efficient compression while preserving visual quality. The program's core functionality involves grouping similar pixels together using K-means clustering and replacing them with the average color value of the cluster centroid. By reducing the number of unique colors in the image, significant compression can be achieved without compromising the overall visual fidelity.

To illustrate the process, the program will accept an input image and apply K-means clustering to partition the image into clusters of similar colors. Each cluster represents a set of pixels with similar color characteristics. The program then replaces all pixels within each cluster with the average color value of the cluster centroid. This process effectively reduces the number of unique colors in the image, resulting in compression.

The implementation of the algorithm would allow users to interact with a command-line interface where they can input the path to the image that they wish to compress and the desired compression level (number of clusters). The program would then process the image accordingly and save the compressed image to a separate file.

## Introduction

This project is an image compression algorithm that uses K-means clustering to compress images. The user can run the program and select the image they wish to compress. The program will then group the pixels with similar colors and replace them with the color of the centroid. By reducing the number of unique colors in the image, compression can be achieved without compromising the overall visual fidelity of the image.

## Implementation Details

The project is implemented in Python. As stated in the proposal, the user can provide the path to the image and the desired compression level when running the program. The program will then process the image and save the compressed image to a separate file.

Here are the descriptions of the two Python files. Furthermore, the code in each file is documented with comments to explain each part in greater detail.

### `.py`

#### Notes (DELETE LATER)

- Using jpeg did not provide nice results as the original jpeg was already very compressed. However, using provided better results with decreasing size with less clusters
- Using numpy broadcasting in the k-means code made the program much faster. Originally, with the rocks.png and 32 clusters, it took 336s (5m36s) while after the change it took 27 seconds. 12x faster / 91% less time.
- Taking a random color when init centroids allows us to get a more representative starting point especially when the data is noisy. This can help the k-means algorithm converge faster and increase the quality of the compressed image.

## Further Improvements

## How to Run

### Setting up the enviroment

1. Ensure that you have a working install of Python 3.11.7.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program


