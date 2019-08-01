import tkinter as tkin
from tkinter import ttk, scrolledtext

class Scrollbox:
	"""Scrollbox to display csv file data"""
	def __init__(self, root_window, name, column_pos, row_pos):
		
		self.column_pos = column_pos
		self.row_pos = row_pos
		self.name = name
		self.root_window = root_window
		self.scroll_h = 14
		self.scroll_w = 65
		
		# Frames and textboxes for csv file previewing
		lf = ttk.LabelFrame(self.root_window, text=self.name)
		lf.grid(column = self.column_pos, row = self.row_pos, pady=5)

		self.st = scrolledtext.ScrolledText(lf, width = self.scroll_w, height=self.scroll_h, wrap ='none')
		self.st.grid(column=0, row = 0)

		# Implementing horizontal scroll bars 
		sb = tkin.Scrollbar(lf, orient='horizontal', command = self.st.xview)
		sb.grid(column=0, row=1, sticky='ew')
		self.st['xscrollcommand'] = sb.set

	def printCsv(self, filename):
		csv_str = ""
		with open(filename, 'r') as f_obj:
			for line in f_obj:
				csv_str += line

		self.st.delete('1.0', 'end')
		self.st.insert('1.0', csv_str)


