# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ValidMaidDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ValidMaidDialog(object):
    def setupUi(self, ValidMaidDialog):
        ValidMaidDialog.setObjectName("ValidMaidDialog")
        ValidMaidDialog.resize(400, 300)

        self.buttonBox = QtWidgets.QDialogButtonBox(ValidMaidDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(ValidMaidDialog)
        self.label.setGeometry(QtCore.QRect(110, 80, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ValidMaidDialog)
        self.buttonBox.accepted.connect(ValidMaidDialog.accept)
        self.buttonBox.rejected.connect(ValidMaidDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ValidMaidDialog)

    def retranslateUi(self, ValidMaidDialog):
        _translate = QtCore.QCoreApplication.translate
        ValidMaidDialog.setWindowTitle(_translate("ValidMaidDialog", "ValidMaidDialog"))
        self.label.setText(_translate("ValidMaidDialog", "Password is password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ValidMaidDialog = QtWidgets.QDialog()
    ui = Ui_ValidMaidDialog()
    ui.setupUi(ValidMaidDialog)
    ValidMaidDialog.show()
    sys.exit(app.exec_())
