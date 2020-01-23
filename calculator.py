#!/usr/bin/env python3

import sys
import math
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
		self.operation_done = False
		self.last_equal_clicked = False
		self.dec_mode = False

	def initialize_buttons(self):
		for button in self.ui.numbers.buttons():
			button.clicked.connect(self.set_number(button.text()))
		for operator in self.ui.operators.buttons():
			operator.clicked.connect(self.op_clicked(operator.text()))
		for saved in self.ui.saved.buttons():
			saved.clicked.connect(self.save_clicked(saved))
		self.ui.button_equals.clicked.connect(self.equals_clicked)
		self.ui.button_sin.clicked.connect(self.sin_clicked)
		self.ui.button_cos.clicked.connect(self.cos_clicked)
		self.ui.button_dec.clicked.connect(self.dec_check)

	def dec_check(self):
		if not self.dec_mode:
			self.dec_mode = True
			if self.first:
				self.first_num = (str(self.first_num) + '.')
				set_number = self.first_num
			else:
				self.second_num = (str(self.second_num) + '.')
				set_number = self.second_num
			self.set_line(set_number)


	def save_clicked(self, button):
		def save_clicked():
			value = button.text()
			try:
				number = float(value)
				if self.first:
					self.first_num = number
					set_number = self.first_num
				else:
					self.second_num = number
					set_number = self.second_num
				self.set_line(set_number)
			except ValueError:
				set_number = float(self.ui.main_line.text()) if (self.curr != 0 and float(self.ui.main_line.text()) != 0) else 0
				if value == "A":
					self.ui.button_A.setText("%.3f" % set_number)
				elif value == "B":
					self.ui.button_B.setText("%.3f" % set_number)
				elif value == "C":
					self.ui.button_C.setText("%.3f" % set_number)
				elif value == "D":
					self.ui.button_D.setText("%.3f" % set_number)
		return save_clicked

	def op_clicked(self, op):
		def operation():
			self.dec_mode = False
			self.last_equal_clicked = False
			if self.operation_done:
				self.op_equals()
			self.currentop = op
			# self.do_operation(op)
			# self.first_num = self.curr
			self.first = False
			# self.set_line(self.curr)
			self.operation_done = True
		return operation

	def do_operation(self, op):
		self.first = False
		self.first_num = float(self.first_num)
		self.second_num = float(self.second_num)
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

	def sin_clicked(self):
		self.curr = math.sin(self.curr)
		self.set_line(self.curr)

	def cos_clicked(self):
		self.curr = math.cos(self.curr)
		self.set_line(self.curr)

	def op_equals(self):
		self.do_operation(self.currentop)
		self.first_num = self.curr
		self.second_num = 0
		self.first = True
		self.set_line(self.curr)
		self.operation_done = False

	def equals_clicked(self):
		self.dec_mode = False
		self.do_operation(self.currentop)
		self.first_num = self.curr
		self.second_num = 0
		self.first = True
		self.set_line(self.curr)
		self.operation_done = False
		self.last_equal_clicked = True

	def set_number(self, number):
		def print_number():
			if self.last_equal_clicked:
				self.last_equal_clicked = False
				self.first_num = 0
			try:
				if self.first:
					check = int(number)
					if not self.dec_mode:
						self.first_num = (int(self.first_num) + int(check))
					else:
						self.first_num = (str(self.first_num) + str(check))
					set_number = self.first_num
				else:
					check = int(number)
					if not self.dec_mode:
						self.second_num = (int(self.second_num) + int(check))
					else:
						self.second_num = (str(self.second_num) + str(check))
					set_number = self.second_num
				self.set_line(set_number)
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
		self.operation_done = False
		self.first_num = 0
		self.second_num = 0
		self.curr = 0
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
