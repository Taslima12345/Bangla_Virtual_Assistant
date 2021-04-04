from Test_thread import VoiceCommandListener
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
import os
from os import path
# from Model_backend_thread import VoiceCommandsListener
import time



class Open_Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(178,205,203);") 
        self.title = '      সহকারী - A Bangla Virtual Assistant   '
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 950
        self.initUI()
        
        self.backendObj = VoiceCommandListener(self)
        self.backendObj.start()
  
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | 
                            QtCore.Qt.WindowMinimizeButtonHint)

        self.wlcome_msg = QtWidgets.QLabel(self)
        self.wlcome_msg.setGeometry(190,15,450, 50)      
        self.wlcome_msg.setFont(QtGui.QFont('Arial', 15))       
        self.wlcome_msg.setStyleSheet("color: rgb(48,32,152);")
        self.wlcome_msg.setAlignment(QtCore.Qt.AlignCenter) 
        self.wlcome_msg.setText('সহকারী - A Bangla Virtual Assistant')

        
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        self.mikeIconImagePath = path.join(application_path, 'images', 'inputIcon.png')
        
        # self.mikeImagePath = path.join(iconImagePath)
        self.mike_icon = QtGui.QPixmap(self.mikeIconImagePath)
        #self.mike_icon = QtGui.QPixmap("./mike_icon.png")
        self.mike_icon = self.mike_icon.scaled(200,205, QtCore.Qt.KeepAspectRatio)
        self.mike_label = QtWidgets.QLabel(self)
        self.mike_label.setGeometry(300, 90, 200,200)
        self.mike_label.setAlignment(QtCore.Qt.AlignCenter)   
        self.mike_label.setPixmap(self.mike_icon)
       # self.resize(self.mike_icon.width(),self.mike_icon.height())

        self.input_text = QtWidgets.QLabel(self)
        self.input_text.setGeometry(340,320,300,50)
        self.input_text.setFont(QtGui.QFont('Arial', 12))       
        self.input_text.setStyleSheet("color: rgb(0,0,0);")
        self.input_text.setText('শনাক্তকৃত কমান্ড')

        self.show_input_command = QtWidgets.QLabel(self)
        self.show_input_command.setGeometry(215,370,370,32)
        #self.input_text.styleSheet("background-color: rgb(255,255,255);")
        self.show_input_command.setFont(QtGui.QFont('Arial', 12))       
        self.show_input_command.setStyleSheet("background-color: rgb(255,255,255); color: rgb(14,171,162);")
        self.show_input_command.setAlignment(QtCore.Qt.AlignCenter)
        self.show_input_command.setText("")
        
        self.output_text = QtWidgets.QLabel(self)
        self.output_text.setGeometry(350,450,300,50)
        self.output_text.setFont(QtGui.QFont('Arial', 12))       
        self.output_text.setStyleSheet("color: rgb(0,0,0);")        
        self.output_text.setText('আউটপুট')


        
        
        self.output_present = QtWidgets.QLabel(self)
        self.output_present.setGeometry(100,500,600,420)
        self.output_present.setFont(QtGui.QFont('Arial', 12))       
        self.output_present.setStyleSheet("background-color: rgb(255,255,255); color: rgb(48,32,152); border:4px solid teal; \
                                            padding: 5px;")

        self.output_present.setAlignment(QtCore.Qt.AlignCenter)
        self.output_present.setWordWrap(True)   
        self.show()
        

    def showScreenshotImage(self, path):
        self.screenShot = QtGui.QPixmap(path)
        self.screenShot = self.screenShot.scaled(400,500, QtCore.Qt.KeepAspectRatio)
        self.output_present.setPixmap(self.screenShot)
    
    def closeEvent(self, event):
        self.backendObj.raise_exception()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Open_Window()
    sys.exit(app.exec_())

