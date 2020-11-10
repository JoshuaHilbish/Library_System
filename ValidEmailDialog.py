# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ValidEmailDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ValidEmailDialog(object):
    def setupUi(self, ValidEmailDialog):
        ValidEmailDialog.setObjectName("ValidEmailDialog")
        ValidEmailDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ValidEmailDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ValidEmailDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ValidEmailDialog)
        self.label.setGeometry(QtCore.QRect(120, 80, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ValidEmailDialog)
        self.buttonBox.accepted.connect(ValidEmailDialog.accept)
        self.buttonBox.rejected.connect(ValidEmailDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ValidEmailDialog)

    def retranslateUi(self, ValidEmailDialog):
        _translate = QtCore.QCoreApplication.translate
        ValidEmailDialog.setWindowTitle(_translate("ValidEmailDialog", "ValidEmailDialog"))
        self.label.setText(_translate("ValidEmailDialog", "Username is Admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ValidEmailDialog = QtWidgets.QDialog()
    ui = Ui_ValidEmailDialog()
    ui.setupUi(ValidEmailDialog)
    ValidEmailDialog.show()
    sys.exit(app.exec_())
