#from imagecompare import app
from imagecompare.src.userinterface import Root

if __name__ == '__main__':
	#app.main()
	root = Root()
	root.init_ui()
	root.mainloop()