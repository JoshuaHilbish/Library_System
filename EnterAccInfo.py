# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterAccInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterAccInfo(object):
    def setupUi(self, EnterAccInfo):
        EnterAccInfo.setObjectName("EnterAccInfo")
        EnterAccInfo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EnterAccInfo)
        self.centralwidget.setObjectName("centralwidget")

        self.lblEnterAccInfoTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoTitle.setGeometry(QtCore.QRect(310, 70, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblEnterAccInfoTitle.setFont(font)
        self.lblEnterAccInfoTitle.setObjectName("lblEnterAccInfoTitle")

        self.txtbxEnterAccInfoFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoFirstName.setGeometry(QtCore.QRect(250, 120, 113, 22))
        self.txtbxEnterAccInfoFirstName.setObjectName("txtbxEnterAccInfoFirstName")

        self.txtbxEnterAccInfoEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoEmail.setGeometry(QtCore.QRect(250, 180, 113, 22))
        self.txtbxEnterAccInfoEmail.setObjectName("txtbxEnterAccInfoEmail")

        self.txtbxEnterAccInfoLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoLastName.setGeometry(QtCore.QRect(410, 120, 113, 22))
        self.txtbxEnterAccInfoLastName.setObjectName("txtbxEnterAccInfoLastName")

        self.txtbxEnterAccInfoPhoneNum = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoPhoneNum.setGeometry(QtCore.QRect(410, 180, 113, 22))
        self.txtbxEnterAccInfoPhoneNum.setObjectName("txtbxEnterAccInfoPhoneNum")

        self.lblEnterAccInfoFirstName = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoFirstName.setGeometry(QtCore.QRect(274, 100, 71, 20))
        self.lblEnterAccInfoFirstName.setObjectName("lblEnterAccInfoFirstName")

        self.lblEnterAccInfoEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoEmail.setGeometry(QtCore.QRect(290, 160, 55, 16))
        self.lblEnterAccInfoEmail.setObjectName("lblEnterAccInfoEmail")

        self.lblEnterAccInfoLastName = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoLastName.setGeometry(QtCore.QRect(430, 100, 61, 16))
        self.lblEnterAccInfoLastName.setObjectName("lblEnterAccInfoLastName")

        self.lblEnterAccInfoPhoneNum = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoPhoneNum.setGeometry(QtCore.QRect(420, 160, 91, 20))
        self.lblEnterAccInfoPhoneNum.setObjectName("lblEnterAccInfoPhoneNum")

        self.btnEnterAccInfoConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnterAccInfoConfirm.setGeometry(QtCore.QRect(260, 340, 93, 28))
        self.btnEnterAccInfoConfirm.setObjectName("btnEnterAccInfoConfirm")
        #
        self.btnEnterAccInfoConfirm.clicked.connect(EnterAccInfo.close)
        #

        self.btnEnterAccInfoCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnterAccInfoCancel.setGeometry(QtCore.QRect(420, 340, 93, 28))
        self.btnEnterAccInfoCancel.setObjectName("btnEnterAccInfoCancel")
        #
        self.btnEnterAccInfoCancel.clicked.connect(EnterAccInfo.close)
        #

        self.txtbxEnterAccInfoZipCode = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoZipCode.setGeometry(QtCore.QRect(250, 240, 113, 22))
        self.txtbxEnterAccInfoZipCode.setObjectName("txtbxEnterAccInfoZipCode")

        self.txtbxEnterAccInfoSecurQuest = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoSecurQuest.setGeometry(QtCore.QRect(410, 240, 113, 22))
        self.txtbxEnterAccInfoSecurQuest.setObjectName("txtbxEnterAccInfoSecurQuest")

        self.lblEnterAccInfoZipCode = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoZipCode.setGeometry(QtCore.QRect(274, 220, 61, 20))
        self.lblEnterAccInfoZipCode.setObjectName("lblEnterAccInfoZipCode")

        self.lblEnterAccInfoMaidName = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoMaidName.setGeometry(QtCore.QRect(370, 220, 221, 20))
        self.lblEnterAccInfoMaidName.setObjectName("lblEnterAccInfoMaidName")

        self.lblEnterAccInfoSecurQuest = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoSecurQuest.setGeometry(QtCore.QRect(410, 210, 111, 16))
        self.lblEnterAccInfoSecurQuest.setObjectName("lblEnterAccInfoSecurQuest")

        self.txtbxEnterAccInfoUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoUsername.setGeometry(QtCore.QRect(250, 300, 113, 22))
        self.txtbxEnterAccInfoUsername.setObjectName("txtbxEnterAccInfoUsername")

        self.txtbxEnterAccInfoPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbxEnterAccInfoPassword.setGeometry(QtCore.QRect(410, 300, 113, 22))
        self.txtbxEnterAccInfoPassword.setObjectName("txtbxEnterAccInfoPassword")

        self.lblEnterAccInfoUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoUsername.setGeometry(QtCore.QRect(280, 280, 71, 20))
        self.lblEnterAccInfoUsername.setObjectName("lblEnterAccInfoUsername")

        self.lblEnterAccInfoPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterAccInfoPassword.setGeometry(QtCore.QRect(440, 280, 71, 20))
        self.lblEnterAccInfoPassword.setObjectName("lblEnterAccInfoPassword")

        EnterAccInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnterAccInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        EnterAccInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EnterAccInfo)
        self.statusbar.setObjectName("statusbar")
        EnterAccInfo.setStatusBar(self.statusbar)

        self.retranslateUi(EnterAccInfo)
        QtCore.QMetaObject.connectSlotsByName(EnterAccInfo)
    """def close(self):
        self.close()"""

    def retranslateUi(self, EnterAccInfo):
        _translate = QtCore.QCoreApplication.translate
        EnterAccInfo.setWindowTitle(_translate("EnterAccInfo", "EnterAccInfo"))
        self.lblEnterAccInfoTitle.setText(_translate("EnterAccInfo", "Enter Account Info"))
        self.lblEnterAccInfoFirstName.setText(_translate("EnterAccInfo", "First Name"))
        self.lblEnterAccInfoEmail.setText(_translate("EnterAccInfo", "Email"))
        self.lblEnterAccInfoLastName.setText(_translate("EnterAccInfo", "Last Name"))
        self.lblEnterAccInfoPhoneNum.setText(_translate("EnterAccInfo", "Phone Number"))
        self.btnEnterAccInfoConfirm.setText(_translate("EnterAccInfo", "Confirm"))
        self.btnEnterAccInfoCancel.setText(_translate("EnterAccInfo", "Cancel"))
        self.lblEnterAccInfoZipCode.setText(_translate("EnterAccInfo", "ZIP Code"))
        self.lblEnterAccInfoMaidName.setText(_translate("EnterAccInfo", "What is your mother\'s maiden name?"))
        self.lblEnterAccInfoSecurQuest.setText(_translate("EnterAccInfo", "Security Question:"))
        self.lblEnterAccInfoUsername.setText(_translate("EnterAccInfo", "Username"))
        self.lblEnterAccInfoPassword.setText(_translate("EnterAccInfo", "Password"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterAccInfo = QtWidgets.QMainWindow()
    ui = Ui_EnterAccInfo()
    ui.setupUi(EnterAccInfo)
    EnterAccInfo.show()
    sys.exit(app.exec_())
