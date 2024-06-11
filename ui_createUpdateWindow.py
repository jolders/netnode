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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_createUpdate(object):
    def setupUi(self, createUpdate):
        if not createUpdate.objectName():
            createUpdate.setObjectName(u"createUpdate")
        createUpdate.resize(391, 476)
        self.lbl_title = QLabel(createUpdate)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setGeometry(QRect(80, 30, 261, 20))
        self.btn_exit = QPushButton(createUpdate)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(280, 430, 80, 23))
        self.btn_submit = QPushButton(createUpdate)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setGeometry(QRect(150, 350, 80, 23))

        self.retranslateUi(createUpdate)

        QMetaObject.connectSlotsByName(createUpdate)
    # setupUi

    def retranslateUi(self, createUpdate):
        createUpdate.setWindowTitle(QCoreApplication.translate("createUpdate", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("createUpdate", u"createWindow or updateWindow", None))
        self.btn_exit.setText(QCoreApplication.translate("createUpdate", u"Exit", None))
        self.btn_submit.setText(QCoreApplication.translate("createUpdate", u"Submit", None))
    # retranslateUi

