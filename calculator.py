#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from calculatorDesign import Ui_MainWindow


class Mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(Mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.currentop = "+"
		self.ui.setupUi(self)
		self.first = True
		self.first_num = 0
		self.second_num = 0
		self.curr = 0
		self.initialize_buttons()
		self.initial = True

	def initialize_buttons(self):
		for button in self.ui.numbers.buttons():
			button.clicked.connect(self.set_number(button.text()))
		for operator in self.ui.operators.buttons():
			operator.clicked.connect(self.op_clicked(operator.text()))
		self.ui.button_equals.clicked.connect(self.equals_clicked)

	def op_clicked(self, op):
		def operation():
			self.currentop = op
			# self.do_operation(op)
			# self.first_num = self.curr
			self.first = False
			# self.set_line(self.curr)
		return operation

	def do_operation(self, op):
		if op == "+":
			self.curr = self.first_num + self.second_num
		elif op == "-":
			self.curr = self.first_num - self.second_num
		elif op == "*":
			self.curr = self.first_num * self.second_num
		elif op == "/":
			if self.second_num != 0:
				self.curr = self.first_num / self.second_num
			else:
				self.set_line("Err")

	def equals_clicked(self):
		self.do_operation(self.currentop)
		self.first_num = self.curr
		self.first = False
		self.set_line(self.curr)

	def set_number(self, number):
		def print_number():
			try:
				if self.first:
					self.first_num = int(number)
					self.first = False
				else:
					self.second_num = int(number)
					self.first = True
				self.set_line(number)
			except ValueError:
				if number == 'C':
					self.clear()
				else:
					print("There was a button error")
					sys.exit(1)
		return print_number

	def set_line(self, number):
		self.ui.main_line.setText(str(number))

	def clear(self):
		self.first_num = 0
		self.second_num = 0
		self.set_line(0)
		self.first = True
		self.currentop = "+"


def main():
	app = QtWidgets.QApplication([])
	application = Mywindow()
	application.show()
	sys.exit(app.exec())


if __name__ == "__main__":
	try: 
		main()
	except KeyboardInterrupt:
		print("User quit program.")
		sys.exit()
