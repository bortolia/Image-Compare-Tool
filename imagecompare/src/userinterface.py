import tkinter as tkin
from tkinter import ttk, filedialog
from imagecompare.src.scrollbox import Scrollbox
from imagecompare.src import compare

class Root(tkin.Tk):
	"""Root Window"""
	def __init__(self):
		#Inheriting from tkinter
		super().__init__()
		self.title('Image Compare')
		self.minsize(850, 525)

		# Configuring gui grid to 50 x 50
		rows = 0
		while rows < 50:
			self.rowconfigure(rows, weight=1)
			self.columnconfigure(rows, weight=1)
			rows += 1

	def init_ui(self):

		#Creating instances of input and output Scrollboxes
		self.scrollbox_in = Scrollbox(self,'Input CSV Preview',1,2)
		self.scrollbox_out = Scrollbox(self,'Output CSV Preview',1,20)

		#Input for Csv file
		file_lf = ttk.LabelFrame(self, text='CSV Input')
		file_lf.grid(column=24, row = 2, columnspan=2)
		file_btn = ttk.Button(file_lf, text='Browse File', command=self.file_dialog)
		file_btn.grid(column=0, row = 1)
		#
		compare_btn = ttk.Button(file_lf, text='Compare', command=self.comp_files)
		compare_btn.grid(column=1, row = 1)
		#
		self.file_label = ttk.Label(file_lf, text='No File Selected')
		self.file_label.grid(column=0, row=2, columnspan=2)

		#Output
		out_lf = ttk.LabelFrame(self, text='CSV Output Directory')
		out_lf.grid(column=24, row = 20, sticky='ew', columnspan=2)
		self.output_dir = tkin.Text(out_lf, height=1, width=20, wrap='none')
		self.output_dir.pack(expand='yes', fill='x')


	def file_dialog(self):
		
		self.filename = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV files', '*.csv')])
		
		if not self.filename:
			self.file_label.configure(text='No File Selected')
		else:
			if len(self.filename) > 40:
				shortName = ""
				shortName += self.filename[0:20]
				shortName += "..."
				shortName += self.filename[-20:]

				self.file_label.configure(text=shortName)

			else:
				self.file_label.configure(text=self.filename)

			self.scrollbox_in.printCsv(self.filename)
			
			#Parse csv file for comparison of image pairs
			self.csv_pairs_list = compare.parse_csv(self.filename)


	def comp_files(self):

		if not self.filename:
			return None

		output_pairs_list = []
		for img1, img2 in self.csv_pairs_list[1:]:
			output_pairs_list.append(compare.compare_images(img1,img2))

		new_file = compare.write_csv(self.filename, self.csv_pairs_list, output_pairs_list)
		self.scrollbox_out.printCsv(new_file)
		
		self.output_dir.delete('1.0', 'end')
		self.output_dir.insert('1.0', new_file)	


