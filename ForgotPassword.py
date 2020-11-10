# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgotPassword.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from InvalidLoginDialog import Ui_InvalidLoginDialog
from ValidMaidDialog import Ui_ValidMaidDialog


class Ui_ForgotPassword(object):
    def setupUi(self, ForgotPassword):
        ForgotPassword.setObjectName("ForgotPassword")
        ForgotPassword.resize(800, 330)
        self.centralwidget = QtWidgets.QWidget(ForgotPassword)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnForgotPassConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.btnForgotPassConfirm.setGeometry(QtCore.QRect(330, 170, 93, 28))
        self.btnForgotPassConfirm.setObjectName("btnForgotPassConfirm")
        #
        self.btnForgotPassConfirm.clicked.connect(self.checkForgotPassInfo)
        #
        
        self.txtbxForgotPassEnterMaid = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxForgotPassEnterMaid.setGeometry(QtCore.QRect(320, 130, 113, 22))
        self.txtbxForgotPassEnterMaid.setObjectName("txtbxForgotPassEnterMaid")

        self.lblForgotPassEnterMaid = QtWidgets.QLabel(self.centralwidget)
        self.lblForgotPassEnterMaid.setGeometry(QtCore.QRect(80, 130, 250, 21))
        self.lblForgotPassEnterMaid.setObjectName("lblForgotPassEnterMaid")

        self.lblForgotPassTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblForgotPassTitle.setGeometry(QtCore.QRect(310, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblForgotPassTitle.setFont(font)
        self.lblForgotPassTitle.setObjectName("lblForgotPassTitle")
        
        self.btnForgotPassCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnForgotPassCancel.setGeometry(QtCore.QRect(330, 200, 93, 28))
        self.btnForgotPassCancel.setObjectName("btnForgotPassCancel")
        #
        self.btnForgotPassCancel.clicked.connect(ForgotPassword.close)
        #
        
        ForgotPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForgotPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ForgotPassword.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForgotPassword)
        self.statusbar.setObjectName("statusbar")
        ForgotPassword.setStatusBar(self.statusbar)

        self.retranslateUi(ForgotPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgotPassword)
    def checkForgotPassInfo(self):
        if self.txtbxForgotPassEnterMaid.text() == 'Smith':
            self.window = QtWidgets.QDialog()
            self.ui = Ui_ValidMaidDialog()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_InvalidLoginDialog()
            self.ui.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, ForgotPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgotPassword.setWindowTitle(_translate("ForgotPassword", "ForgotPassword"))
        self.btnForgotPassConfirm.setText(_translate("ForgotPassword", "Confirm"))
        self.lblForgotPassEnterMaid.setText(_translate("ForgotPassword", "What is your mother's Maiden Name?"))
        self.lblForgotPassTitle.setText(_translate("ForgotPassword", "Forgot Password"))
        self.btnForgotPassCancel.setText(_translate("ForgotPassword", "Close"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPassword = QtWidgets.QMainWindow()
    ui = Ui_ForgotPassword()
    ui.setupUi(ForgotPassword)
    ForgotPassword.show()
    sys.exit(app.exec_())
