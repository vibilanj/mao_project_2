# Modelling and Optimization Project 2

## Proposal

The project proposes the development of an image compression algorithm using K-means clustering to achieve efficient compression while preserving visual quality. The program's core functionality involves grouping similar pixels together using K-means clustering and replacing them with the average color value of the cluster centroid. By reducing the number of unique colors in the image, significant compression can be achieved without compromising the overall visual fidelity.

To illustrate the process, the program will accept an input image and apply K-means clustering to partition the image into clusters of similar colors. Each cluster represents a set of pixels with similar color characteristics. The program then replaces all pixels within each cluster with the average color value of the cluster centroid. This process effectively reduces the number of unique colors in the image, resulting in compression.

The implementation of the algorithm would allow users to interact with a command-line interface where they can input the path to the image that they wish to compress and the desired compression level (number of clusters). The program would then process the image accordingly and save the compressed image to a separate file.

## Introduction

## Implementation Details

## Further Improvements

## How to Run

### Setting up the enviroment

1. Ensure that you have a working install of Python 3.11.7.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program


