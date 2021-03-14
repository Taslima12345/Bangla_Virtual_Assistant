import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
import os
from os import path

class Open_Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(178,205,203);") 
        self.title = '      সহকারী - A Bangla Virtual Assistan    '
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 950
        self.initUI()


        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | 
                            QtCore.Qt.WindowMinimizeButtonHint)

        self.wlcome_msg = QtWidgets.QLabel(self)
        self.wlcome_msg.setGeometry(235,10,300, 50)      
        self.wlcome_msg.setFont(QtGui.QFont('Arial', 15))       
        self.wlcome_msg.setStyleSheet("color: rgb(48,32,152);")
        self.wlcome_msg.setAlignment(QtCore.Qt.AlignCenter) 
        self.wlcome_msg.setText('Welcome Window ')


        self.mikeImagePath = path.join(path.dirname(path.abspath(__file__)), 'inputIcon.png')
        self.mike_icon = QtGui.QPixmap(self.mikeImagePath)
        #self.mike_icon = QtGui.QPixmap("./mike_icon.png")
        self.mike_icon = self.mike_icon.scaled(200,200, QtCore.Qt.KeepAspectRatio)
        self.mike_label = QtWidgets.QLabel(self)
        self.mike_label.setGeometry(300, 90, 200,200)
        self.mike_label.setAlignment(QtCore.Qt.AlignCenter)   
        self.mike_label.setPixmap(self.mike_icon)
       # self.resize(self.mike_icon.width(),self.mike_icon.height())


        self.input_text = QtWidgets.QLabel(self)
        self.input_text.setGeometry(320,300,300,50)
        self.input_text.setFont(QtGui.QFont('Arial', 12))       
        self.input_text.setStyleSheet("color: rgb(0,0,0);")
        self.input_text.setText('Detected Command')

        self.show_input_command = QtWidgets.QLabel(self)
        self.show_input_command.setGeometry(215,343,370,32)
        #self.input_text.styleSheet("background-color: rgb(255,255,255);")
        self.show_input_command.setFont(QtGui.QFont('Arial', 12))       
        self.show_input_command.setStyleSheet("background-color: rgb(255,255,255); color: rgb(14,171,162);")
        self.show_input_command.setAlignment(QtCore.Qt.AlignCenter)
        self.show_input_command.setText('Open Youtube')
        

        self.output_text = QtWidgets.QLabel(self)
        self.output_text.setGeometry(350,390,300,50)
        self.output_text.setFont(QtGui.QFont('Arial', 12))       
        self.output_text.setStyleSheet("color: rgb(0,0,0);")        
        self.output_text.setText('Result Status')

        self.show_output_status = QtWidgets.QLabel(self)
        self.show_output_status.setGeometry(215,433,370,32)
        #self.input_text.styleSheet("background-color: rgb(255,255,255);")
        self.show_output_status.setFont(QtGui.QFont('Arial', 12))       
        self.show_output_status.setStyleSheet("background-color: rgb(255,255,255); color: rgb(14,171,162);")
        self.show_output_status.setAlignment(QtCore.Qt.AlignCenter)
        self.show_output_status.setText('Command Executed')
        

    #     self.output_present = QtWidgets.QLabel(self)
    #     self.output_present.setGeometry(100,500,600,420)
    #     #self.input_text.styleSheet("background-color: rgb(255,255,255);")
    #     self.output_present.setFont(QtGui.QFont('Arial', 12))       
    #     self.output_present.setStyleSheet("background-color: rgb(255,255,255); color: rgb(48,32,152); border: 4px solid teal;")
    #     self.output_present.setAlignment(QtCore.Qt.AlignCenter)
    #    # self.output_present.setText('Output Present ')


        self.screenShootPath = path.join(path.dirname(path.abspath(__file__)), 'Nature.jpg')
        self.screenShot = QtGui.QPixmap(self.screenShootPath)
        self.screenShot = self.screenShot.scaled(400,500, QtCore.Qt.KeepAspectRatio)
        self.output_present = QtWidgets.QLabel(self)
        self.output_present.setGeometry(100,500,600,420)
        self.output_present.setFont(QtGui.QFont('Arial', 12))       
        self.output_present.setStyleSheet("background-color: rgb(255,255,255); color: rgb(48,32,152); border: 4px solid teal;")
        self.output_present.setAlignment(QtCore.Qt.AlignCenter)   
        self.output_present.setPixmap(self.screenShot)
        #self.output_present.setText('Output Present ')


        






        
        # self.mike_icon = QtGui.QPixmap("./Voice_input_icon.png")
        # self.mike_icon = self.mike_icon.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        # self.mike_lebel = QtWidgets.QLabel()
        # #self.mike_lebel.setGeometry(200,60,500, 400)
        # self.mike_lebel.setPixmap(self.mike_icon)
        # #self.mike_lebel.setGeometry(10.15,100,100)
        

        # self.grid = QtWidgets.QGridLayout()
        # self.grid.addWidget(self.wlcome_msg,0,0,1,3)
        # self.grid.addWidget (self.mike_lebel,1,1)
    
        #self.setLayout(self.grid)

        

        self.show()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Open_Window()
    sys.exit(app.exec_())











# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# #from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow


# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         # self.app = QtWidgets.QApplication(sys.argv)
#         self.win = QtWidgets.QMainWindow()
        
#         self.win.setWindowTitle("Sohokari- A Bangla Virtual Assistant")
#         self.win.setGeometry(100,60,200,200)

#         self.wlcome_msg = QtWidgets.QLabel(self)
#         self.wlcome_msg.setText('Welcome....')
#         self.wlcome_msg.setGeometry(10,10,100,50)
#         #self.widget = QtWidgets.QLabel('Hello') 

#         self.win.show()
#         # sys.exit(self.app.exec_())
# app =  QtWidgets.QApplication(sys.argv)
# main = MainWindow()
# sys.exit(app.exec_())