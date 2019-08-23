from PIL import Image
import numpy as np
import csv
import os
import time

class Model:
	"""The Model interacts with all data including CSV files and images"""
	def __init__(self):

		self.line_holder =[]

	def parse_csv(self, filename):
		"""
		- This method parses the csv file that is passed in
		- Returns a list of each line in the file
		"""

		if self.line_holder:
			self.line_holder = []

		with open(filename, 'r') as csv_file:
			csv_reader = csv.reader(csv_file)

			for line in csv_reader:
				self.line_holder.append(line)

			return self.line_holder


	def compare_images(self, file1, file2):
		"""
		- This method is responsible for the comparison and timing of the comparison of two images.
		- Error handling for FileNotFoundError in csv file is included, and returns a message for output csv 
		- Returns a list of [Bjorn (Comparison) Score, Time Elapsed (seconds)]
		"""
		try:
			img1 = Image.open(file1)
			img2 = Image.open(file2)

		except FileNotFoundError:
			return ['File Not Found','0']

		else:
		
			# If the two images being compared do not have the same dimensions, then they are considered
			# completely different, and have a score of 1, with time elapsed 0 
			if img1.size != img2.size:
				return ['1', '0']

			# The images are converted to greyscale to compare pixels
			# Greyscale pixels will have values 0 to 255
			img1 = img1.convert('L')
			img2 = img2.convert('L')

			# Converting the greyscaled image to a numpy array to easily iterate through
			imgArr1 = np.asarray(img1)
			imgArr2 = np.asarray(img2)

			start = time.time()

			# Comparison Algorithm
			# - This loop iterates through each image array(pixel) and checks if each are not equal
			# - If so, the absolute value of the difference between the pixel values is determined and
			# checked if it is greater than 5. 
			# - I chose this to be the threshold to determine if a pixel is different to help ignore 
			# subtle noise from images taken by cameras (that aren't great quality)
			# - I found this to work well, and compensates for about 2% (5/256 ~= 0.0195)
			# - The threshold can be chanegd to 0 if it is not desired.

			diff_count = 0
			for x, y in np.nditer([imgArr1, imgArr2]):
				if(x != y):
					#Threshold is 5
					if abs(int(x) - int(y)) > 5:
						diff_count += 1

			end = time.time()

			# The comparison is determined by dividing the number of different pixels by the total pixels
			sim = diff_count/(imgArr1.shape[0] * imgArr1.shape[1])

			if sim == 0:
				return [str(int(sim)), "{0:.5f}".format(end-start)]
			else:
				return ["{0:.5f}".format(sim), "{0:.5f}".format(end-start)]


	def write_csv(self, filename, original_pairs, new_pairs):
		"""
		- This method is responsible for writing a new CSV file with the new fields in the first row
		followed by the image paths with their comparison score and time elapsed to compute each pair
		- Returns the path to the result CSV file
		"""

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



		
		