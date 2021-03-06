#from tkinter import *
#import tkinter.font
#
#
#RPi.GPIO.setmode(RPi.GPIO.BCM)
#
#led=LED(14)
#
#win=Tk()
#win.title('LED Toggler')
#myFont=tkinter.font.Font(family='Helvetica', size = 12, weight = 'bold')
#
#def ledToggle():
#    if led.is_lit:
#        led.off()
#        ledButton['text']='Turn LED on'
#    else:
#        led.on()
#        ledButton['text']='Turn LED off'
#
#ledButton=Button(win, text = 'Turn LED on', font=myFont, command=ledToggle, bg='bisque2', height=1, width=24)
#ledButton.grid(row=0,column=1)
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led=LED(14)

def btn_clicked():
	print("Button Pressed")
	QMessageBox.information(MainWindow, 'Welcome', 'PyQt5 + Raspberyy PI')
    

def ledToggle():
        if led.is_lit:
            led.off()
        else:
            led.on()
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 535)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "Click Me"))
        self.pushButton.clicked.connect(btn_clicked)
    

import sys
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

