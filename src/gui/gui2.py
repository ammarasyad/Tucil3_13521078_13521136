# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import plot


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(334, 449)
        Form.setStyleSheet("background-color: rgb(163, 163, 163);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalFrame = QtWidgets.QFrame(Form)
        self.verticalFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalFrame.setAutoFillBackground(False)
        self.verticalFrame.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"background-color: rgb(153, 153, 153);")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalFrame.setLineWidth(1)
        self.verticalFrame.setMidLineWidth(4)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 13)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browseFile)
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.visualizePlot)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalFrame)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.verticalFrame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalFrame)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label_5 = QtWidgets.QLabel(self.verticalFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_3.raise_()
        self.label_5.raise_()
        self.verticalLayout_2.addWidget(self.verticalFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Route Search"))
        self.pushButton.setText(_translate("Form", "Open File"))
        self.label_2.setText(_translate("Form", "File :"))
        self.pushButton_2.setText(_translate("Form", "Visualize"))
        self.label_3.setText(_translate("Form", "Source node:"))
        self.label_4.setText(_translate("Form", "Destination node:"))
        self.pushButton_3.setText(_translate("Form", "Search Route"))
        self.label_5.setText(_translate("Form", "Route:"))

    def browseFile(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(Form, "Open File", "c:", "Text files (*.txt)")
        
    def visualizePlot(self):
        graphMatrix = plot.parseFile(filename)
        
        plot.createGraphsWithoutSave(plot.getEdge(graphMatrix))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
