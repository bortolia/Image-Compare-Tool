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
		file_btn.grid(column=1, row = 1)
		self.file_label = ttk.Label(file_lf, text='No File Selected')
		self.file_label.grid(column=1, row=2)

		#Output
		out_lf = ttk.LabelFrame(self, text='CSV Output Directory')
		out_lf.grid(column=24, row = 20, sticky='ew', columnspan=2)
		self.output_dir = tkin.Text(out_lf, height=1, width=20, wrap='none')
		self.output_dir.pack(expand='yes', fill='x')


	def file_dialog(self):
		
		filename = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV files', '*.csv')])
		
		if not filename:
			self.file_label.configure(text='No File Selected')
		else:
			if len(filename) > 40:
				shortName = ""
				shortName += filename[0:20]
				shortName += "..."
				shortName += filename[-20:]

				self.file_label.configure(text=shortName)

			else:
				self.file_label.configure(text=filename)

			self.scrollbox_in.printCsv(filename)
			
			#Parse csv file for comparison of image pairs
			csv_pairs_list = compare.parse_csv(filename)
			print(csv_pairs_list)

			output_pairs_list = []
			for img1, img2 in csv_pairs_list[1:]:
				output_pairs_list.append(compare.compare_images(img1,img2))

			print(output_pairs_list)

			new_file = compare.write_csv(filename, csv_pairs_list, output_pairs_list)
			self.scrollbox_out.printCsv(new_file)
			
			self.output_dir.delete('1.0', 'end')
			self.output_dir.insert('1.0', new_file)	


