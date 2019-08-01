from PIL import Image
import numpy as np
import csv
import os
import time

def parse_csv(filename):

	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		line_holder = []

		for line in csv_reader:
			line_holder.append(line)

		return line_holder


def compare_images(file1, file2):

	img1 = Image.open(file1)
	img2 = Image.open(file2)

	if img1.size != img2.size:
		return [1, 0]

	img1 = img1.convert('L')
	img2 = img2.convert('L')

	imgArr1 = np.asarray(img1)
	imgArr2 = np.asarray(img2)

	start = time.time()

	diff_count = 0
	for x, y in np.nditer([imgArr1, imgArr2]):
		if(x != y):
			#Threshold is 5
			if abs(int(x) - int(y)) > 5:
				diff_count += 1

	end = time.time()

	sim = diff_count/(imgArr1.shape[0] * imgArr1.shape[1])

	if sim == 0:
		return [int(sim), "{0:.5f}".format(end-start)]
	else:
		return ["{0:.5f}".format(sim), "{0:.5f}".format(end-start)]


def write_csv(filename, original_pairs, new_pairs):
	
	original_pairs[0].append('similar')
	original_pairs[0].append('elapsed')

	directory = os.path.split(filename)
	out_file_path = os.path.join(directory[0], 'out_file.csv')

	with open(out_file_path, 'w') as new_file:
		csv_writer = csv.writer(new_file)

		csv_writer.writerow(original_pairs[0])

		for i in range(len(new_pairs)):
			for j in range(2):
				original_pairs[i+1].append(new_pairs[i][j])

		for row in original_pairs[1:]:
			csv_writer.writerow(row)

	return out_file_path


