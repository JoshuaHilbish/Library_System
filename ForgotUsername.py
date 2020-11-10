# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgotUsername.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from InvalidLoginDialog import Ui_InvalidLoginDialog
from ValidEmailDialog import Ui_ValidEmailDialog

class Ui_ForgotUsername(object):
    def setupUi(self, ForgotUsername):
        ForgotUsername.setObjectName("ForgotUsername")
        ForgotUsername.resize(800, 330)
        self.centralwidget = QtWidgets.QWidget(ForgotUsername)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnForgotUserConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.btnForgotUserConfirm.setGeometry(QtCore.QRect(330, 170, 93, 28))
        self.btnForgotUserConfirm.setObjectName("btnForgotUserConfirm")
        #
        self.btnForgotUserConfirm.clicked.connect(self.checkForgotEmailInfo)
        #
        
        self.txtbxForgotUserEnterEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxForgotUserEnterEmail.setGeometry(QtCore.QRect(320, 130, 113, 22))
        self.txtbxForgotUserEnterEmail.setObjectName("txtbxForgotUserEnterEmail")

        self.lblForgotUserEnterEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblForgotUserEnterEmail.setGeometry(QtCore.QRect(240, 130, 71, 21))
        self.lblForgotUserEnterEmail.setObjectName("lblForgotUserEnterEmail")

        self.lblForgotUserTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblForgotUserTitle.setGeometry(QtCore.QRect(310, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblForgotUserTitle.setFont(font)
        self.lblForgotUserTitle.setObjectName("lblForgotUserTitle")
        
        self.btnForgotUserCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnForgotUserCancel.setGeometry(QtCore.QRect(330, 200, 93, 28))
        self.btnForgotUserCancel.setObjectName("btnForgotUserCancel")
        #
        self.btnForgotUserCancel.clicked.connect(ForgotUsername.close)
        #
        
        ForgotUsername.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForgotUsername)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ForgotUsername.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForgotUsername)
        self.statusbar.setObjectName("statusbar")
        ForgotUsername.setStatusBar(self.statusbar)

        self.retranslateUi(ForgotUsername)
        QtCore.QMetaObject.connectSlotsByName(ForgotUsername)

    def checkForgotEmailInfo(self):
        if self.txtbxForgotUserEnterEmail.text() == 'user@email.com':
            self.window = QtWidgets.QDialog()
            self.ui = Ui_ValidEmailDialog()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_InvalidLoginDialog()
            self.ui.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, ForgotUsername):
        _translate = QtCore.QCoreApplication.translate
        ForgotUsername.setWindowTitle(_translate("ForgotUsername", "ForgotUsername"))
        self.btnForgotUserConfirm.setText(_translate("ForgotUsername", "Confirm"))
        self.lblForgotUserEnterEmail.setText(_translate("ForgotUsername", "Enter Email"))
        self.lblForgotUserTitle.setText(_translate("ForgotUsername", "Forgot Username"))
        self.btnForgotUserCancel.setText(_translate("ForgotUsername", "Close"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotUsername = QtWidgets.QMainWindow()
    ui = Ui_ForgotUsername()
    ui.setupUi(ForgotUsername)
    ForgotUsername.show()
    sys.exit(app.exec_())
