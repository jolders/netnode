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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(706, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(170, 20, 371, 20))
        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setGeometry(QRect(60, 240, 80, 23))
        self.btn_update = QPushButton(self.centralwidget)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(320, 240, 80, 23))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(560, 240, 80, 23))
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(610, 340, 80, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 706, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"Ui_mainWindow.py", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

