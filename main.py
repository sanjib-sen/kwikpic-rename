# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kwikpic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import shutil
from urllib.parse import unquote
from PyQt6 import QtCore, QtGui, QtWidgets
import os
import threading
import sys


if getattr(sys, 'frozen', False):
    image = os.path.join(sys._MEIPASS, 'logo.png')
else:
    image = "LOGO/logo.png"


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(636, 590)
        icon = QtGui.QIcon(image)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 321, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(image))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 290, 300, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 290, 111, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 360, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 501, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kwikpic Rename"))
        self.label_2.setText(_translate("Form", "Source Folder"))
        self.pushButton.setText(_translate("Form", "Choose"))
        self.pushButton_3.setText(_translate("Form", "Rename"))
        self.pushButton.clicked.connect(self.selectSourceFolder)
        self.pushButton_3.clicked.connect(self.renameThread)

    def selectSourceFolder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            Form, "Choose Source Folder")
        self.lineEdit.setText(folder)

    def renameThread(self):
        if self.lineEdit.text() == None or self.lineEdit.text() == "":
            self.label_4.setText("Please Select a Source Folder.")
            return
        x = threading.Thread(target=self.rename)
        x.start()

    def rename(self):
        UNKNOWN_DIR = self.lineEdit.text()
        path = UNKNOWN_DIR
        try:
            currentPath = path
            filesList = os.listdir(currentPath)
            newDir = currentPath
            newDir = os.path.join(currentPath, 'renamed')
            print("Debug", currentPath+"/"+"renamed",
                  os.path.exists(currentPath+"/"+"renamed"))
            if not os.path.exists(currentPath+"/"+"renamed"):
                os.mkdir(newDir)

            for item in filesList:
                try:
                    if os.path.isfile(currentPath+"/"+item) and ".py" not in item:
                        # execute rename operation
                        filteredName = unquote(item.rsplit("@", 1)[-1])
                        shutil.copyfile(os.path.join(
                            currentPath, item), os.path.join(newDir, filteredName))
                        print("done", filteredName)
                    else:
                        print("skipped", item)
                except Exception as e:
                    print("failed for", item)
            print("Rename and copy done.")
            print()
        except Exception as e:
            self.label_4.setText("Error occurred:")

        self.label_4.setText("Rename and copy done.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
