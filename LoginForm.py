# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#
from InvalidLoginDialog import Ui_InvalidLoginDialog
from main import Ui_MainWindow
from EnterAccInfo import Ui_EnterAccInfo
from ForgotPassword import Ui_ForgotPassword
from ForgotUsername import Ui_ForgotUsername
#

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(391, 391)

        self.lblLoginFormTitle = QtWidgets.QLabel(LoginForm)
        self.lblLoginFormTitle.setGeometry(QtCore.QRect(80, 40, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblLoginFormTitle.setFont(font)
        self.lblLoginFormTitle.setObjectName("lblLoginFormTitle")

        self.lblLoginFormUser = QtWidgets.QLabel(LoginForm)
        self.lblLoginFormUser.setGeometry(QtCore.QRect(80, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLoginFormUser.setFont(font)
        self.lblLoginFormUser.setObjectName("lblLoginFormUser")

        self.txtbxLoginFormUser = QtWidgets.QLineEdit(LoginForm)
        self.txtbxLoginFormUser.setGeometry(QtCore.QRect(170, 120, 141, 22))
        self.txtbxLoginFormUser.setObjectName("txtbxLoginFormUser")
        self.txtbxLoginFormUser.setPlaceholderText('Enter your username')

        self.lblLoginFormPass = QtWidgets.QLabel(LoginForm)
        self.lblLoginFormPass.setGeometry(QtCore.QRect(80, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLoginFormPass.setFont(font)
        self.lblLoginFormPass.setObjectName("lblLoginFormPass")

        self.btnLoginFormLogin = QtWidgets.QPushButton(LoginForm)
        self.btnLoginFormLogin.setGeometry(QtCore.QRect(80, 210, 93, 28))
        self.btnLoginFormLogin.setObjectName("btnLoginFormLogin")
        #
        self.btnLoginFormLogin.clicked.connect(self.checkLoginInfo)#adds functionality to login button
        #
        
        self.btnLoginFormCreateAcc = QtWidgets.QPushButton(LoginForm)
        self.btnLoginFormCreateAcc.setGeometry(QtCore.QRect(180, 210, 131, 28))
        self.btnLoginFormCreateAcc.setObjectName("btnLoginFormCreateAcc")
        #
        self.btnLoginFormCreateAcc.clicked.connect(self.createAcc)
        #
        
        self.btnLoginFormForgotUser = QtWidgets.QPushButton(LoginForm)
        self.btnLoginFormForgotUser.setGeometry(QtCore.QRect(80, 250, 111, 28))
        self.btnLoginFormForgotUser.setObjectName("btnLoginFormForgotUser")
        #
        self.btnLoginFormForgotUser.clicked.connect(self.forgotUser)
        #

        self.btnLoginFormForgotPass = QtWidgets.QPushButton(LoginForm)
        self.btnLoginFormForgotPass.setGeometry(QtCore.QRect(200, 250, 111, 28))
        self.btnLoginFormForgotPass.setObjectName("btnLoginFormForgotPass")
        #
        self.btnLoginFormForgotPass.clicked.connect(self.forgotPass)
        #

        self.btnLoginFormClose = QtWidgets.QPushButton(LoginForm)
        self.btnLoginFormClose.setGeometry(QtCore.QRect(80, 290, 231, 28))
        self.btnLoginFormClose.setObjectName("btnLoginFormClose")
        #
        self.btnLoginFormClose.clicked.connect(self.close)
        #

        self.txtbxLoginFormPass = QtWidgets.QLineEdit(LoginForm)
        self.txtbxLoginFormPass.setGeometry(QtCore.QRect(170, 170, 141, 22))
        self.txtbxLoginFormPass.setObjectName("txtbxLoginFormPass")
        self.txtbxLoginFormPass.setPlaceholderText('Enter your password')
        #
        self.txtbxLoginFormPass.setEchoMode(QtWidgets.QLineEdit.Password)#hides password
        #
        
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
    def checkLoginInfo(self):
        if self.txtbxLoginFormUser.text() == 'Admin' and self.txtbxLoginFormPass.text() == 'password':
            self.txtbxLoginFormUser.setText("")
            self.txtbxLoginFormPass.setText("")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        elif self.txtbxLoginFormUser.text() == 'Admin2' and self.txtbxLoginFormPass.text() == 'pass':
            self.txtbxLoginFormUser.setText("")
            self.txtbxLoginFormPass.setText("")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_InvalidLoginDialog()
            self.ui.setupUi(self.window)
            self.window.show()
    def createAcc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterAccInfo()
        self.ui.setupUi(self.window)
        self.window.show()
    def forgotUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ForgotUsername()
        self.ui.setupUi(self.window)
        self.window.show()
    def forgotPass(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ForgotPassword()
        self.ui.setupUi(self.window)
        self.window.show()
    def close(self):
        self.close()
            
    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "LoginForm"))
        self.lblLoginFormTitle.setText(_translate("LoginForm", "Library Circulation System"))
        self.lblLoginFormUser.setText(_translate("LoginForm", "Username:"))
        self.lblLoginFormPass.setText(_translate("LoginForm", "Password:"))
        self.btnLoginFormLogin.setStatusTip(_translate("LoginForm", "Press To Validate Login Info"))
        self.btnLoginFormLogin.setText(_translate("LoginForm", "Login"))
        self.btnLoginFormCreateAcc.setStatusTip(_translate("LoginForm", "Press To Create New Account"))
        self.btnLoginFormCreateAcc.setText(_translate("LoginForm", "Create new Account"))
        self.btnLoginFormForgotUser.setStatusTip(_translate("LoginForm", "Press To Answer Security Question To Reclaim Username"))
        self.btnLoginFormForgotUser.setText(_translate("LoginForm", "Forgot Username?"))
        self.btnLoginFormForgotPass.setStatusTip(_translate("LoginForm", "Press To Answer Security Question And Reclaim Password"))
        self.btnLoginFormForgotPass.setText(_translate("LoginForm", "Forgot Password?"))
        self.btnLoginFormClose.setStatusTip(_translate("LoginForm", "Press To Close Program"))
        self.btnLoginFormClose.setText(_translate("LoginForm", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QMainWindow()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
