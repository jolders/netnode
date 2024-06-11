# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainWindow import Ui_MainWindow
from createUpdateWindow import CreateUpdateWindow

#   MainWIndow         pyside6-uic mainWindow.ui -o ui_mainWindow.py
#   CreateWindow       pyside6-uic createUpdateWindow.ui -o ui_createUpdateWindow.py


class MainWindow(QMainWindow, Ui_MainWindow):



    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        id = "4"
        hostname = ""
        username = ""
        ipaddress = ""


        # Buttons
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_create.clicked.connect(self.btn_create_clicked)
        self.ui.btn_update.clicked.connect(lambda : self.btn_update_clicked(id))
        self.ui.btn_delete.clicked.connect(self.btn_delete_clicked)

    # Button Connections
    def btn_create_clicked(self, id):
        # id = "5"
        print(f"btn_create_clicked id {id}")
        title = "CREATE"
        id = "0"
        self.create_window = CreateUpdateWindow(title, id)
        self.create_window.submitted.connect(self.updateview)
        self.create_window.show()

    def btn_update_clicked(self, id):
        print("btn_update_clicked")
        title="UPDATE"
        self.update_window = CreateUpdateWindow(title, id)
        self.update_window.submitted.connect(self.updateview)
        self.update_window.show()


    def btn_delete_clicked(self):
        print("btn_delete_clicked")

    @qtc.Slot(str)
    def updateview(self, message):
        print(f"UPDATEVIEW PRINT = {message}")


