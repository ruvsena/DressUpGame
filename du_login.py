import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1179, 696)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 1181, 711))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("image: url(C:/Users/pc/PycharmProjects/DressUpGame/img/bg2.jpg);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/pc/PycharmProjects/DressUpGame/img/bg5.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(580, 320, 131, 31))
        self.username.setStyleSheet("font: 12pt \"Sitka Small\";\n"
"border-radius:15px;\n"
"")
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(440, 360, 141, 41))
        self.label.setStyleSheet("font: 12pt \"Sitka Small\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 310, 141, 41))
        self.label_3.setStyleSheet("font: 12pt \"Sitka Small\";")
        self.label_3.setObjectName("label_3")
        self.pw = QtWidgets.QLineEdit(Dialog)
        self.pw.setGeometry(QtCore.QRect(580, 370, 131, 31))
        self.pw.setStyleSheet("border-radius:15px;")
        self.pw.setObjectName("pw")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 130, 321, 421))
        self.label_4.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius:15px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 440, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"font: 12pt \"Sitka Small\";\n"
"border-radius:15px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(500, 150, 161, 141))
        self.label_5.setStyleSheet("image: url(C:/Users/pc/PycharmProjects/DressUpGame/img/logo.png);")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label_4.raise_()
        self.pw.raise_()
        self.username.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.setWindowTitle("DressUpGame")
        Dialog.setWindowIcon(QtGui.QIcon("C:/Users/pc/PycharmProjects/DressUpGame/img/logo.png"))
        self.pushButton.clicked.connect(self.Login)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "UserName"))
        self.pushButton.setText(_translate("Dialog", "Login"))

    def Login(self):
        self.db = sqlite3.connect('dress_up.db')
        self.cur = self.db.cursor()

        user_name = self.username.text()
        user_password = self.pw.text()
        self.cur.execute(''' SELECT * FROM user WHERE user_name='%s', user_pw='%s' ''', (user_name, user_password,))
        print(user_name)
        if user_name == user_password:
            print('youre in')
        else:
            print('PASSWORDS ARE NOT MATCHİNG')

        self.username.setText('')
        self.pw.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
