# Image Compare Tool

Image Compare is a tool used to automate the comparison of N pairs of images. The tool will compute the similarities between each image pair, and then output a CSV file with records of similarity score and computation time per pair.

The user must input a CSV file with two fields (image1, image2) with the names of the images being their absolute path.

## Dependencies/Libraries

Image Compare Tool was developed using Python 3.7.2 using the following dependencies:

* numpy 1.17.0
* Pillow 6.1.0
* Tkinter 8.5 (included with Python)

## Setup

Start by installing the required libraries. You may find it preferable to install them in a virtual environment. Navigate to a directory that you would like the environment to reside and run 

```sh
$ python -m venv your-environment-name
```

To use the environment on MacOS

```sh
$ source your-environment-name/bin/activate
```

On Windows

```sh
$ your-environment-name\Scripts\activate.bat
```

If you have not already, clone the repository to your computer. Navigate to the top directory of the project and install the required libraries

```sh
$ pip install -r requirements.txt
```

Start the application from the top directory, running imagecompare as a module

```sh
$ python -m imagecompare
```

## Development Process

My implementation of this solution started with coming up with my own algorithm to actually compare each image pair. I also wrote functions to parse and write test CSV files. I found that working on the algorithmic problems before implementing a user interface was helpful. 

A bulk of my time was spent researching a library to use to handle images in Python. I chose the Pillow library because it made loading the images into a numpy array easiest and it served well for my algorithm to compare images. During this process, I found out about Structural Similarity Index, which would work great from this project. It is an algorithm developed for assessing image/video quality. I was able to implement it when testing, but wanted to stick to my own solution for the actual image comparison.

After testing my solutions for individual image comparisons and CSVs, I began researching for a suitable GUI library to use. Tkinter was a great choice due to its cross platform capabilities for use on MacOS and Windows. It is also built-in and up-to-date with modern versions of Python.

#### MacOS Preview

(./images/mac_preview.png)

#### Windows Preview

(./images/windows_preview.png)
