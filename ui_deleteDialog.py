# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(399, 579)
        Dialog.setStyleSheet(u"QDialog {\n"
"        background-color: \"gainsboro\";\n"
"}\n"
"/* --------------------------------------- CANCEL DIALOG BUTTON  -----------------------------------*/\n"
"QDialogButtonBox > QPushButton[text=\"Cancel\"]{\n"
"    color: \"black\";\n"
"    background-color: \"lightcoral\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"lightslategrey\";\n"
"    border-style: solid;\n"
"	width:100px;\n"
"height:30px;\n"
"font-size: 16px;\n"
"}\n"
"QDialogButtonBox > QPushButton[text=\"Cancel\"]:hover {\n"
"  color: \"black\";\n"
"background-color: \"orangered\";\n"
"font-weight: bold;\n"
"}\n"
"/* --------------------------------------- OK DIALOG BUTTON  -----------------------------------*/\n"
"QDialogButtonBox > QPushButton[text=\"OK\"]{\n"
"    color: \"black\";\n"
"    background-color: \"lightgreen\";\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"lightslategrey\";\n"
"    border-style: solid;\n"
"	wid"
                        "th:100px;\n"
"height:30px;\n"
"font-size: 16px\n"
"}\n"
"QDialogButtonBox > QPushButton[text=\"OK\"]:hover {\n"
"  color: \"white\";\n"
"background-color: \"green\";\n"
"font-weight: bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_title = QLabel(Dialog)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 0))
        self.lbl_title.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(14)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet(u"")
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setMargin(0)
        self.lbl_title.setIndent(0)

        self.verticalLayout_2.addWidget(self.lbl_title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, 21)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lbl_id = QLabel(Dialog)
        self.lbl_id.setObjectName(u"lbl_id")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(12)
        self.lbl_id.setFont(font1)
        self.lbl_id.setMargin(12)
        self.lbl_id.setIndent(10)

        self.horizontalLayout_8.addWidget(self.lbl_id)

        self.lbl_idresult = QLabel(Dialog)
        self.lbl_idresult.setObjectName(u"lbl_idresult")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_idresult.sizePolicy().hasHeightForWidth())
        self.lbl_idresult.setSizePolicy(sizePolicy)
        self.lbl_idresult.setFont(font1)
        self.lbl_idresult.setLayoutDirection(Qt.RightToLeft)
        self.lbl_idresult.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lbl_idresult.setMargin(10)
        self.lbl_idresult.setIndent(0)

        self.horizontalLayout_8.addWidget(self.lbl_idresult)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_hostname = QLabel(Dialog)
        self.lbl_hostname.setObjectName(u"lbl_hostname")
        self.lbl_hostname.setFont(font1)
        self.lbl_hostname.setMargin(12)
        self.lbl_hostname.setIndent(10)

        self.horizontalLayout_2.addWidget(self.lbl_hostname)

        self.lbl_hostnameresult = QLabel(Dialog)
        self.lbl_hostnameresult.setObjectName(u"lbl_hostnameresult")
        self.lbl_hostnameresult.setFont(font1)
        self.lbl_hostnameresult.setMargin(12)
        self.lbl_hostnameresult.setIndent(0)

        self.horizontalLayout_2.addWidget(self.lbl_hostnameresult)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_ipaddress = QLabel(Dialog)
        self.lbl_ipaddress.setObjectName(u"lbl_ipaddress")
        self.lbl_ipaddress.setFont(font1)
        self.lbl_ipaddress.setMargin(12)
        self.lbl_ipaddress.setIndent(10)

        self.horizontalLayout_3.addWidget(self.lbl_ipaddress)

        self.lbl_ipaddressresult = QLabel(Dialog)
        self.lbl_ipaddressresult.setObjectName(u"lbl_ipaddressresult")
        self.lbl_ipaddressresult.setFont(font1)
        self.lbl_ipaddressresult.setMargin(12)
        self.lbl_ipaddressresult.setIndent(0)

        self.horizontalLayout_3.addWidget(self.lbl_ipaddressresult)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_username = QLabel(Dialog)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setMaximumSize(QSize(16777215, 60))
        self.lbl_username.setSizeIncrement(QSize(10, 0))
        self.lbl_username.setBaseSize(QSize(0, 0))
        self.lbl_username.setFont(font1)
        self.lbl_username.setMargin(12)
        self.lbl_username.setIndent(10)

        self.horizontalLayout_4.addWidget(self.lbl_username)

        self.lbl_usernameresult = QLabel(Dialog)
        self.lbl_usernameresult.setObjectName(u"lbl_usernameresult")
        self.lbl_usernameresult.setMaximumSize(QSize(16777215, 60))
        self.lbl_usernameresult.setSizeIncrement(QSize(10, 0))
        self.lbl_usernameresult.setBaseSize(QSize(0, 0))
        self.lbl_usernameresult.setFont(font1)
        self.lbl_usernameresult.setMargin(12)
        self.lbl_usernameresult.setIndent(0)

        self.horizontalLayout_4.addWidget(self.lbl_usernameresult)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_password = QLabel(Dialog)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setFont(font1)
        self.lbl_password.setMargin(12)
        self.lbl_password.setIndent(10)

        self.horizontalLayout_5.addWidget(self.lbl_password)

        self.lbl_passwordresult = QLabel(Dialog)
        self.lbl_passwordresult.setObjectName(u"lbl_passwordresult")
        self.lbl_passwordresult.setFont(font1)
        self.lbl_passwordresult.setMargin(12)
        self.lbl_passwordresult.setIndent(0)

        self.horizontalLayout_5.addWidget(self.lbl_passwordresult)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.lbl_location = QLabel(Dialog)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setFont(font1)
        self.lbl_location.setMargin(12)
        self.lbl_location.setIndent(10)

        self.horizontalLayout_6.addWidget(self.lbl_location)

        self.lbl_locationresult = QLabel(Dialog)
        self.lbl_locationresult.setObjectName(u"lbl_locationresult")
        self.lbl_locationresult.setFont(font1)
        self.lbl_locationresult.setMargin(12)
        self.lbl_locationresult.setIndent(0)

        self.horizontalLayout_6.addWidget(self.lbl_locationresult)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_description = QLabel(Dialog)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setFont(font1)
        self.lbl_description.setMargin(12)
        self.lbl_description.setIndent(10)

        self.horizontalLayout_7.addWidget(self.lbl_description)

        self.lbl_descriptionresult = QLabel(Dialog)
        self.lbl_descriptionresult.setObjectName(u"lbl_descriptionresult")
        self.lbl_descriptionresult.setFont(font1)
        self.lbl_descriptionresult.setMargin(12)
        self.lbl_descriptionresult.setIndent(0)

        self.horizontalLayout_7.addWidget(self.lbl_descriptionresult)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_title.setText(QCoreApplication.translate("Dialog", u"Delete device from the database ?", None))
        self.lbl_id.setText(QCoreApplication.translate("Dialog", u"ID :", None))
        self.lbl_idresult.setText(QCoreApplication.translate("Dialog", u"lbl_showid", None))
        self.lbl_hostname.setText(QCoreApplication.translate("Dialog", u"Hostname :", None))
        self.lbl_hostnameresult.setText(QCoreApplication.translate("Dialog", u"hostnameresult", None))
        self.lbl_ipaddress.setText(QCoreApplication.translate("Dialog", u"IP Address :", None))
        self.lbl_ipaddressresult.setText(QCoreApplication.translate("Dialog", u"ipaddressresult", None))
        self.lbl_username.setText(QCoreApplication.translate("Dialog", u"Username :", None))
        self.lbl_usernameresult.setText(QCoreApplication.translate("Dialog", u"usernameresult", None))
        self.lbl_password.setText(QCoreApplication.translate("Dialog", u"Password :", None))
        self.lbl_passwordresult.setText(QCoreApplication.translate("Dialog", u"passwordresult", None))
        self.lbl_location.setText(QCoreApplication.translate("Dialog", u"Location :", None))
        self.lbl_locationresult.setText(QCoreApplication.translate("Dialog", u"locationresult", None))
        self.lbl_description.setText(QCoreApplication.translate("Dialog", u"Description :", None))
        self.lbl_descriptionresult.setText(QCoreApplication.translate("Dialog", u"descriptionresult", None))
    # retranslateUi

