# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createUpdateWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_createUpdate(object):
    def setupUi(self, createUpdate):
        if not createUpdate.objectName():
            createUpdate.setObjectName(u"createUpdate")
        createUpdate.resize(455, 718)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createUpdate.sizePolicy().hasHeightForWidth())
        createUpdate.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Noto Serif Lao"])
        font.setPointSize(12)
        createUpdate.setFont(font)
        createUpdate.setStyleSheet(u"QWidget {\n"
"        background-color: \"gainsboro\";\n"
"}\n"
"/* --------------------------------------- BUTTON EXIT  -----------------------------------*/\n"
"QWidget QPushButton#btn_exit {\n"
"    color: \"black\"; /* Button Text */\n"
"    background-color: \"orange\";\n"
"    padding: 8px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"red\";\n"
"    border-style: solid;\n"
"    width:100px;\n"
"    height:10px;\n"
"}\n"
"QWidget QPushButton::hover#btn_exit {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"red\";\n"
"    border-color: \"orange\";\n"
"    border-width: 0px;\n"
"    font-weight:bold;\n"
"}\n"
"/* --------------------------------------- BUTTON SUBMIT  -----------------------------------*/\n"
"QWidget QPushButton#btn_submit {\n"
"    color: \"black\"; /* Button Text */\n"
"    background-color: \"limegreen\";\n"
"    padding: 8px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"forestgreen\";\n"
"    bord"
                        "er-style: solid;\n"
"    width:100px;\n"
"    height:20px;\n"
"}\n"
"/* --------------------------------------- Line Edits  -----------------------------------*/\n"
"QLineEdit { \n"
"	background-color:rgb(202, 255, 227);\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	padding: 0 8px;\n"
"	selection-background-color: \"darkgray\";\n"
"}\n"
"QLineEdit:focus {\n"
"	background-color:rgb(192, 192, 255);\n"
"}\n"
"/* --------------------------------------- Plain Text Edit box  -----------------------------------*/\n"
"QPlainTextEdit {\n"
"	background-color:rgb(202, 255, 227);\n"
"	border: 1px solid gray;\n"
"	padding: 0 8px;\n"
"	border-top-left-radius: 10px; /* same radius as the QComboBox */\n"
"border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 10px;    \n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	background-color:rgb(192, 192, 255);\n"
"}\n"
"/* --------------------------------------- QScrollBar  ------------------------"
                        "-----------*/\n"
"QScrollBar {\n"
"    background-color: \"powderblue\";\n"
"    width: 16px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle {\n"
"    background-color: \"lightslategrey\";\n"
"    margin: 16px 1px 16px 1px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(createUpdate)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_title = QLabel(createUpdate)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(0, 0))
        self.lbl_title.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_title.setSizeIncrement(QSize(0, 0))
        self.lbl_title.setBaseSize(QSize(0, 0))
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setMargin(10)
        self.lbl_title.setIndent(0)

        self.verticalLayout_2.addWidget(self.lbl_title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, 21)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.lbl_id = QLabel(createUpdate)
        self.lbl_id.setObjectName(u"lbl_id")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(12)
        self.lbl_id.setFont(font1)
        self.lbl_id.setMargin(12)
        self.lbl_id.setIndent(10)

        self.horizontalLayout_8.addWidget(self.lbl_id)

        self.lbl_showid = QLabel(createUpdate)
        self.lbl_showid.setObjectName(u"lbl_showid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_showid.sizePolicy().hasHeightForWidth())
        self.lbl_showid.setSizePolicy(sizePolicy1)
        self.lbl_showid.setFont(font1)
        self.lbl_showid.setMargin(10)
        self.lbl_showid.setIndent(80)

        self.horizontalLayout_8.addWidget(self.lbl_showid)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_hostname = QLabel(createUpdate)
        self.lbl_hostname.setObjectName(u"lbl_hostname")
        self.lbl_hostname.setFont(font1)
        self.lbl_hostname.setMargin(12)
        self.lbl_hostname.setIndent(10)

        self.horizontalLayout_2.addWidget(self.lbl_hostname)

        self.le_hostname = QLineEdit(createUpdate)
        self.le_hostname.setObjectName(u"le_hostname")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_hostname.sizePolicy().hasHeightForWidth())
        self.le_hostname.setSizePolicy(sizePolicy2)
        self.le_hostname.setMaximumSize(QSize(230, 35))
        self.le_hostname.setFont(font1)
        self.le_hostname.setAutoFillBackground(False)
        self.le_hostname.setMaxLength(100)
        self.le_hostname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.le_hostname.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.le_hostname)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_ipaddress = QLabel(createUpdate)
        self.lbl_ipaddress.setObjectName(u"lbl_ipaddress")
        self.lbl_ipaddress.setFont(font1)
        self.lbl_ipaddress.setMargin(12)
        self.lbl_ipaddress.setIndent(10)

        self.horizontalLayout_3.addWidget(self.lbl_ipaddress)

        self.le_ipaddress = QLineEdit(createUpdate)
        self.le_ipaddress.setObjectName(u"le_ipaddress")
        sizePolicy2.setHeightForWidth(self.le_ipaddress.sizePolicy().hasHeightForWidth())
        self.le_ipaddress.setSizePolicy(sizePolicy2)
        self.le_ipaddress.setMaximumSize(QSize(230, 35))
        self.le_ipaddress.setFont(font1)

        self.horizontalLayout_3.addWidget(self.le_ipaddress)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_username = QLabel(createUpdate)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setMaximumSize(QSize(16777215, 60))
        self.lbl_username.setSizeIncrement(QSize(10, 0))
        self.lbl_username.setBaseSize(QSize(0, 0))
        self.lbl_username.setFont(font1)
        self.lbl_username.setMargin(12)
        self.lbl_username.setIndent(10)

        self.horizontalLayout_4.addWidget(self.lbl_username)

        self.le_username = QLineEdit(createUpdate)
        self.le_username.setObjectName(u"le_username")
        sizePolicy2.setHeightForWidth(self.le_username.sizePolicy().hasHeightForWidth())
        self.le_username.setSizePolicy(sizePolicy2)
        self.le_username.setMaximumSize(QSize(230, 35))
        self.le_username.setFont(font1)

        self.horizontalLayout_4.addWidget(self.le_username)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_password = QLabel(createUpdate)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setFont(font1)
        self.lbl_password.setMargin(12)
        self.lbl_password.setIndent(10)

        self.horizontalLayout_5.addWidget(self.lbl_password)

        self.le_password = QLineEdit(createUpdate)
        self.le_password.setObjectName(u"le_password")
        sizePolicy2.setHeightForWidth(self.le_password.sizePolicy().hasHeightForWidth())
        self.le_password.setSizePolicy(sizePolicy2)
        self.le_password.setMaximumSize(QSize(230, 35))
        self.le_password.setFont(font1)

        self.horizontalLayout_5.addWidget(self.le_password)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.lbl_location = QLabel(createUpdate)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setFont(font1)
        self.lbl_location.setMargin(12)
        self.lbl_location.setIndent(10)

        self.horizontalLayout_6.addWidget(self.lbl_location)

        self.le_location = QLineEdit(createUpdate)
        self.le_location.setObjectName(u"le_location")
        sizePolicy2.setHeightForWidth(self.le_location.sizePolicy().hasHeightForWidth())
        self.le_location.setSizePolicy(sizePolicy2)
        self.le_location.setMaximumSize(QSize(230, 35))
        self.le_location.setBaseSize(QSize(0, 25))
        self.le_location.setFont(font1)

        self.horizontalLayout_6.addWidget(self.le_location)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_description = QLabel(createUpdate)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setMaximumSize(QSize(300, 16777215))
        self.lbl_description.setFont(font1)
        self.lbl_description.setStyleSheet(u"QWidget {\n"
"        background-color: \"gainsboro\";\n"
"}")
        self.lbl_description.setMargin(12)
        self.lbl_description.setIndent(10)

        self.horizontalLayout_7.addWidget(self.lbl_description)

        self.pte_description = QPlainTextEdit(createUpdate)
        self.pte_description.setObjectName(u"pte_description")
        self.pte_description.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.pte_description.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pte_description.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.horizontalLayout_7.addWidget(self.pte_description)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btn_submit = QPushButton(createUpdate)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setBaseSize(QSize(0, 22))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_submit.setFont(font2)
        self.btn_submit.setStyleSheet(u"QWidget QPushButton::hover#btn_submit {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"seagreen\";\n"
"    border-color: \"seagreen\";\n"
"    border-width: 0px;\n"
"    font-weight:bold;\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"system-reboot"))
        self.btn_submit.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_submit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(createUpdate)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setStyleSheet(u"width:100px;\n"
"height:12px;")
        icon1 = QIcon(QIcon.fromTheme(u"system-log-out"))
        self.btn_exit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_9.addLayout(self.verticalLayout_2)


        self.retranslateUi(createUpdate)

        QMetaObject.connectSlotsByName(createUpdate)
    # setupUi

    def retranslateUi(self, createUpdate):
        createUpdate.setWindowTitle(QCoreApplication.translate("createUpdate", u"Device Create|Update", None))
        self.lbl_title.setText(QCoreApplication.translate("createUpdate", u"createWindow or updateWindow", None))
        self.lbl_id.setText(QCoreApplication.translate("createUpdate", u"ID :", None))
        self.lbl_showid.setText(QCoreApplication.translate("createUpdate", u"lbl_showid", None))
        self.lbl_hostname.setText(QCoreApplication.translate("createUpdate", u"Hostname :", None))
        self.lbl_ipaddress.setText(QCoreApplication.translate("createUpdate", u"IP Address :", None))
        self.lbl_username.setText(QCoreApplication.translate("createUpdate", u"Username :", None))
        self.lbl_password.setText(QCoreApplication.translate("createUpdate", u"Password :", None))
        self.lbl_location.setText(QCoreApplication.translate("createUpdate", u"Location :", None))
        self.lbl_description.setText(QCoreApplication.translate("createUpdate", u"Description :", None))
        self.btn_submit.setText(QCoreApplication.translate("createUpdate", u"Submit", None))
        self.btn_exit.setText(QCoreApplication.translate("createUpdate", u"Exit", None))
    # retranslateUi

