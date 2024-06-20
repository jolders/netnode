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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 409)
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: \"silver\";\n"
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
"    border-color: \"r"
                        "ed\";\n"
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
"QScrollBa"
                        "r::handle {\n"
"    background-color: \"lightslategrey\";\n"
"    margin: 16px 1px 16px 1px;\n"
"    border-radius: 6px;\n"
"}\n"
"/* --------------------------------------- Status Bar  -----------------------------------*/\n"
"QStatusBar {\n"
"        background: \"silver\";\n"
"        border-top: 2px solid \"gray\";\n"
"}\n"
"QStatusBar, QStatusBar QLabel {\n"
"        color: \"black\";\n"
"}\n"
"QSizeGrip {\n"
"    image: url(window_grip.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: \"silver\";\n"
"}\n"
"\n"
"/* --------------------------------------- Menu Bar  -----------------------------------*/\n"
"QMenuBar {\n"
"	background-color: \"silver\";  /* - Top strip Bar  -*/\n"
"border-bottom: 2px solid \"gray\";\n"
"}\n"
"QMenuBar::item:selected {\n"
"	background: \"lightslategrey\";\n"
"	color: \"white\";\n"
"	font-weight:\"bold\";\n"
"}\n"
"QMenuBar QMenu {\n"
"    background-color: \"silver\"; /* - Drop down menu  -*/\n"
"}\n"
"QMenuBar QMenu::item:selected {\n"
"background-co"
                        "lor: \"slategrey\";\n"
"color: \"white\";\n"
"}\n"
" /* - \n"
"  -*/\n"
"\n"
"\n"
"\n"
"")
        self.actionCreate = QAction(MainWindow)
        self.actionCreate.setObjectName(u"actionCreate")
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.actionCreate.setIcon(icon)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        self.actionCreate.setFont(font1)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        icon1 = QIcon(QIcon.fromTheme(u"edit-redo"))
        self.actionUpdate.setIcon(icon1)
        self.actionUpdate.setFont(font1)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon2 = QIcon(QIcon.fromTheme(u"user-trash"))
        self.actionDelete.setIcon(icon2)
        self.actionDelete.setFont(font1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon(QIcon.fromTheme(u"system-log-out"))
        self.actionExit.setIcon(icon3)
        self.actionExit.setFont(font1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
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
        icon4 = QIcon(QIcon.fromTheme(u"contact-new"))
        self.btn_create.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_create)

        self.btn_update = QPushButton(self.centralwidget)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_exit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 729, 23))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setPointSize(10)
        self.menubar.setFont(font2)
        self.menuDevice = QMenu(self.menubar)
        self.menuDevice.setObjectName(u"menuDevice")
        self.menuDevice.setFont(font2)
        self.menuApp = QMenu(self.menubar)
        self.menuApp.setObjectName(u"menuApp")
        self.menuApp.setFont(font2)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font1)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDevice.menuAction())
        self.menubar.addAction(self.menuApp.menuAction())
        self.menuDevice.addAction(self.actionCreate)
        self.menuDevice.addAction(self.actionUpdate)
        self.menuDevice.addAction(self.actionDelete)
        self.menuDevice.addSeparator()
        self.menuDevice.addAction(self.actionExit)
        self.menuApp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CRUD Application", None))
        self.actionCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
#if QT_CONFIG(statustip)
        self.actionCreate.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a new device.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionCreate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#if QT_CONFIG(statustip)
        self.actionUpdate.setStatusTip(QCoreApplication.translate("MainWindow", u"Update the selected device.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionUpdate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(statustip)
        self.actionDelete.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete the selected device.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(statustip)
        self.actionExit.setStatusTip(QCoreApplication.translate("MainWindow", u"Exit the application.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"Device Database Application", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuDevice.setTitle(QCoreApplication.translate("MainWindow", u"Device", None))
        self.menuApp.setTitle(QCoreApplication.translate("MainWindow", u"App", None))
    # retranslateUi

