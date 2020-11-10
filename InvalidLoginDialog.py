# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InvalidLoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InvalidLoginDialog(object):
    def setupUi(self, InvalidLoginDialog):
        InvalidLoginDialog.setObjectName("InvalidLoginDialog")
        InvalidLoginDialog.resize(400, 300)

        self.buttonBox = QtWidgets.QDialogButtonBox(InvalidLoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(InvalidLoginDialog)
        self.label.setGeometry(QtCore.QRect(100, 80, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(InvalidLoginDialog)
        self.buttonBox.accepted.connect(InvalidLoginDialog.accept)
        self.buttonBox.rejected.connect(InvalidLoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InvalidLoginDialog)

    def retranslateUi(self, InvalidLoginDialog):
        _translate = QtCore.QCoreApplication.translate
        InvalidLoginDialog.setWindowTitle(_translate("InvalidLoginDialog", "InvalidLoginDialog"))
        self.label.setText(_translate("InvalidLoginDialog", "Invalid Info Was Entered"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InvalidLoginDialog = QtWidgets.QDialog()
    ui = Ui_InvalidLoginDialog()
    ui.setupUi(InvalidLoginDialog)
    InvalidLoginDialog.show()
    sys.exit(app.exec_())
