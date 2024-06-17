# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 409)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(80, 90, 10);\n"
"}\n"
"QWidget {\n"
"        background-color: \"gainsboro\";\n"
"}\n"
"\n"
"/* --------------------------------------- Style the BUTTONS --------------------------------------- */\n"
"QPushButton#btn_create, QPushButton#btn_update, QPushButton#btn_delete {\n"
"    color: \"black\"; /* Button Text */\n"
"    background-color: \"powderblue\";\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color: \"lightslategrey\";\n"
"    border-style: solid;\n"
"}\n"
"QPushButton::hover#btn_create, QPushButton::hover#btn_update, QPushButton::hover#btn_delete {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"lightslategrey\";\n"
"    border-color: \"powderblue\";\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton#btn_exit {\n"
"    color: \"black\"; /* Button Text */\n"
"    background-color: \"orange\";\n"
"    padding: 8px;\n"
"    border-radius: 5px;\n"
"    border-width: 1px;\n"
"    border-color"
                        ": \"red\";\n"
"    border-style: solid;\n"
"    width:100px;\n"
"    height:10px;\n"
"}\n"
"QPushButton::hover#btn_exit {\n"
"    color: \"white\"; /* Button Text */\n"
"    background-color: \"red\";\n"
"    border-color: \"orange\";\n"
"    border-width: 0px;\n"
"    font-weight:bold;\n"
"}\n"
"/* --------------------------------------- TABLE  -----------------------------------*/\n"
"QTableView {\n"
"    gridline-color: \"orange\";\n"
"    background-color: \"blanchedalmond\";\n"
"    border-color: \"darkgrey\";\n"
"    padding: 1px;\n"
"}\n"
"/* Header style */\n"
"QHeaderView::section {\n"
"    padding-bottom: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: \"cadetblue\";\n"
"    color: white;\n"
"    height: 25px;\n"
"    /* width: 150px; */\n"
"    font: 14px;\n"
"}\n"
"QTableView::item:selected {\n"
"    /* row selected  Green */\n"
"    background-color: \"darkseagreen\";\n"
"}\n"
"QScrollBar {\n"
"    background-color: \"powderblue\";\n"
"    width: 16px;\n"
"    border: none;\n"
"}\n"
"QScr"
                        "ollBar::handle {\n"
"    background-color: \"lightslategrey\";\n"
"    margin: 16px 1px 16px 1px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"        background: \"silver\";\n"
"        border-top: 1px solid \"darkgrey\";\n"
"}\n"
"QStatusBar, QStatusBar QLabel {\n"
"        color: \"white\";\n"
"}\n"
"QSizeGrip {\n"
"    /*image: url(:/qss_icons/rc/sizegrip.png);*/\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: \"powderblue\";\n"
"}\n"
"\n"
"/* --------------------------------------- TABLE  -----------------------------------*/\n"
"QStatusBar {\n"
"        background: rgb(85, 85, 127);\n"
"        border-top: 1px solid #6272a4;\n"
"}\n"
"QStatusBar, QStatusBar QLabel {\n"
"        color: #8be9fd;\n"
"}\n"
"QStatusBar QLabel {\n"
"        padding-left: .1ex;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")

        self.verticalLayout.addWidget(self.lbl_title)

        self.tv_tableView = QTableView(self.centralwidget)
        self.tv_tableView.setObjectName(u"tv_tableView")
        self.tv_tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_tableView.setProperty("showDropIndicator", False)
        self.tv_tableView.setDragDropOverwriteMode(False)
        self.tv_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_tableView.horizontalHeader().setMinimumSectionSize(40)
        self.tv_tableView.horizontalHeader().setDefaultSectionSize(40)
        self.tv_tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tv_tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 20, 10, 20)
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.btn_update = QPushButton(self.centralwidget)
        self.btn_update.setObjectName(u"btn_update")

        self.horizontalLayout.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")

        self.horizontalLayout_2.addWidget(self.btn_exit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 729, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"ui_mainWindow.py", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

