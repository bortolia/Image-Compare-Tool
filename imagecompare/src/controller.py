import tkinter as tkin
from tkinter import ttk, filedialog
import copy

class Controller:
	"""The Controller ties the View and Model together, orchestrating actions between them"""
	def __init__(self, theView, theModel):

		self.theModel = theModel
		self.theView = theView
		self.filename = ""
		self.csv_pairs_list = []

	def file_dialog_action(self):
		"""Handles the interaction for when the 'Browse File' button is clicked"""
		if self.csv_pairs_list:
			self.csv_pairs_list = []

		# The file to be chosen for input is restricted to *.csv files only
		self.filename = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV files', '*.csv')])
		
		if not self.filename:
			self.theView.file_label.configure(text='No File Selected')
			self.theView.scrollbox_in.printCsv(self.filename)
		else:
			# Falling into this else block will display a short-hand string of the input csv file (with an ellipsis)
			# or will print the full path if it not longer than 40 characters
			if len(self.filename) > 40:
				shortName = ""
				shortName += self.filename[0:20]
				shortName += "..."
				shortName += self.filename[-20:]

				self.theView.file_label.configure(text=shortName)

			else:
				self.theView.file_label.configure(text=self.filename)

			#Printing the input CSV file to the first display box
			self.theView.scrollbox_in.printCsv(self.filename)
			
			#Parse csv file for comparison of image pairs
			self.csv_pairs_list = self.theModel.parse_csv(self.filename)


	def comp_files_action(self):
		"""Handles the interaction for when the 'Compare' button is clicked"""

		if not self.filename:
			# if no file has been selceted, then self.filename will be empty. This calls noInput() to alert the user
			self.theView.noInput()
			return None

		else:
			# Making a deep copy of the csv_pairs_list to manipulate when passed to theModel.write_csv
			output_pairs_list = []
			csv_pairs_list_copy = copy.deepcopy(self.csv_pairs_list)

			#Each pair of images is compared, and their Bjorn Score(similarity) and time elapsed are stored in output_pairs_list
			for img1, img2 in csv_pairs_list_copy[1:]:
				output_pairs_list.append(self.theModel.compare_images(img1,img2))

			# new_file is the returned file path of the result csv file
			new_file = self.theModel.write_csv(self.filename, csv_pairs_list_copy, output_pairs_list)
			self.theView.scrollbox_out.printCsv(new_file)
			
			self.theView.output_dir.delete('1.0', 'end')
			self.theView.output_dir.insert('1.0', new_file)	

		
		
