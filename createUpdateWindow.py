import sys
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_createUpdateWindow import Ui_createUpdate

#   MainWIndow         pyside6-uic mainWindow.ui -o Ui_mainWindow.py
#   CreateWindow       pyside6-uic createUpdateWindow.ui -o Ui_createUpdateWindow.py

class CreateUpdateWindow(QWidget, Ui_createUpdate):

    submitted = qtc.Signal(str)

    def __init__(self, title, id):
        super().__init__()

        print (f"id: {id}")

        self.uicu = Ui_createUpdate()
        self.uicu.setupUi(self)

        # Decide if window is CREATE or UPDATE
        if title == "CREATE":
            self.uicu.lbl_title.setText("CREATE window")
            self.uicu.btn_submit.clicked.connect(self.btn_submit_create)


        elif title == "UPDATE":
            self.uicu.lbl_title.setText("UPDATE window")
            self.uicu.btn_submit.clicked.connect(self.btn_submit_update)

        self.uicu.btn_exit.clicked.connect(self.close)

    @qtc.Slot()
    def btn_submit_create(self):
        print("uicu-btn_submit_create")
        self.submitted.emit("I am just another CREATE window")
    @qtc.Slot()
    def btn_submit_update(self):
        print("uicu-btn_submit_update")
        self.submitted.emit("I am just another UPDATE window")
