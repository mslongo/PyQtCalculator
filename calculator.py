#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, uic
from calculatorDesign import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initialButtons()

	def initialButtons(self):
		print("Here")
		for button in self.ui.numbers.findChildren():
			print(button.text)



def main():
	app = QtWidgets.QApplication([])
	application = mywindow()
	application.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	try: 
		main()
	except KeyboardInterrupt:
		print("User quit program.")
		sys.exit()