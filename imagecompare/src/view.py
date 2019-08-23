import tkinter as tkin
from tkinter import ttk, filedialog, scrolledtext, messagebox
from imagecompare.src.controller import Controller
from imagecompare.src.model import Model

class View(tkin.Tk):
	"""View will be the Root Window. This provides all the user interface for the model"""
	def __init__(self):
		#Inheriting from tkinter
		super().__init__()
		self.title('Image Compare')
		self.minsize(850, 525)

		# Instantiating the Model and Controller
		# Passing this(self) instance of View and the Model to the Controller
		self.model = Model()
		self.controller = Controller(self, self.model)

		# Configuring gui grid to 50 x 50
		rows = 0
		while rows < 50:
			self.rowconfigure(rows, weight=1)
			self.columnconfigure(rows, weight=1)
			rows += 1

		#Creating instances of input and output Scrollboxes
		self.scrollbox_in = Scrollbox(self,'Input CSV Preview',1,2)
		self.scrollbox_out = Scrollbox(self,'Output CSV Preview',1,20)

		#Creating LabelFrame and buttons for input file, as well as adding components to the root window
		file_lf = ttk.LabelFrame(self, text='CSV Input')
		file_lf.grid(column=24, row = 2, columnspan=2)

		#file_btn calls file_dialog_action method, to allow user to open CSV file, and will display its path once chosen
		file_btn = ttk.Button(file_lf, text='Browse File', command=self.controller.file_dialog_action)
		file_btn.grid(column=0, row = 1)

		# compare_btn calls the comp_files_action method, which will execute the image comparison process for
		# image paths specified in the file
		compare_btn = ttk.Button(file_lf, text='Compare', command=self.controller.comp_files_action)
		compare_btn.grid(column=1, row = 1)
		
		self.file_label = ttk.Label(file_lf, text='No File Selected')
		self.file_label.grid(column=0, row=2, columnspan=2)

		#Creating LableFrame and Text to display the output file directory and adding component to the root window
		out_lf = ttk.LabelFrame(self, text='CSV Output Directory')
		out_lf.grid(column=24, row = 20, sticky='ew', columnspan=2)
		self.output_dir = tkin.Text(out_lf, height=1, width=20, wrap='none')
		self.output_dir.pack(expand='yes', fill='x')

	
	def noInput(self):
		"""Alert box is displayed when no file is attempted to be compared"""
		messagebox.showinfo('Image Compare Message', 'No input CSV selected.')
		

class Scrollbox:
	"""Scrollbox class to display csv file data"""
	def __init__(self, root_window, name, column_pos, row_pos):
		
		# Configuring Scrolling text box size
		self.column_pos = column_pos
		self.row_pos = row_pos
		self.name = name
		self.root_window = root_window
		self.scroll_h = 14
		self.scroll_w = 65
		
		# Frames and textboxes for csv file previewing added to the root window
		lf = ttk.LabelFrame(self.root_window, text=self.name)
		lf.grid(column = self.column_pos, row = self.row_pos, pady=5)

		self.st = scrolledtext.ScrolledText(lf, width = self.scroll_w, height=self.scroll_h, wrap ='none')
		self.st.grid(column=0, row = 0)

		# Implementing horizontal scroll bars 
		sb = tkin.Scrollbar(lf, orient='horizontal', command = self.st.xview)
		sb.grid(column=0, row=1, sticky='ew')
		self.st['xscrollcommand'] = sb.set

	
	def printCsv(self, filename):
		"""This method is used to print the corresponding CSV file to its Scrollbox"""
		csv_str = ""
		try:
			with open(filename, 'r') as f_obj:
				for line in f_obj:
					csv_str += line

		#Catches FileNotFoundError of input csv file if it is not found
		except FileNotFoundError:
			pass

		#Will insert empty string ("") if file not found, or the csv file if it exists
		self.st.delete('1.0', 'end')
		self.st.insert('1.0', csv_str)

		