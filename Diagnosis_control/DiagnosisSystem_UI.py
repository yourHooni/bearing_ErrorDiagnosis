# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JYP\Desktop\고장진단시스템.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import UI_resource
import Diagnosis_control as control

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backGround = QtWidgets.QLabel(self.centralwidget)
        self.backGround.setGeometry(QtCore.QRect(0, -1, 1024, 640))
        self.backGround.setText("")
        self.backGround.setPixmap(QtGui.QPixmap(":/메인/KakaoTalk_20180605_222409007.jpg"))
        self.backGround.setScaledContents(True)
        self.backGround.setObjectName("backGround")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(320, 440, 671, 181))
        self.startButton.setText("")
        self.startButton.setCheckable(False)
        self.startButton.setAutoExclusive(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setFlat(True)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startBtn_clicked)

        self.tireLabel = QtWidgets.QLabel(self.centralwidget)
        self.tireLabel.setGeometry(QtCore.QRect(782, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tireLabel.setFont(font)
        self.tireLabel.setTextFormat(QtCore.Qt.AutoText)
        self.tireLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tireLabel.setObjectName("tireLabel")
        self.bearingLabel = QtWidgets.QLabel(self.centralwidget)
        self.bearingLabel.setGeometry(QtCore.QRect(782, 282, 161, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.bearingLabel.setFont(font)
        self.bearingLabel.setTextFormat(QtCore.Qt.AutoText)
        self.bearingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bearingLabel.setObjectName("bearingLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tireLabel.setText(_translate("MainWindow", "TextLabel"))
        self.bearingLabel.setText(_translate("MainWindow", "BearingLabel"))

    def startBtn_clicked(self):

        tire_result = control.main()
        tire_result = do_check(tire_result)
        
        self.tireLabel.setText(tire_result)
        self.bearingLabel.setText("변경")

def do_check(value):
    if(int(value) == 0):
        result = '고장'
    elif(int(value) == 1):
        result = '정상'

    return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

