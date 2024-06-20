# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
#from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtSql import QSqlTableModel
from sqlConnection import SqlDataConnection

from ui_mainWindow import Ui_MainWindow
from createUpdateWindow import UpdateWindow, CreateWindow, DeleteDialog

#   MainWIndow         pyside6-uic mainWindow.ui -o ui_mainWindow.py
#   CreateWindow       pyside6-uic createUpdateWindow.ui -o ui_createUpdateWindow.py

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    # def __init__(self, *args, **kwargs):
    def __init__(self):
        super().__init__()
        #super().__init__(*args, **kwargs)

        self.getSelectedDeviceID = ""
        self.hostname = ""
        self.ipaddress = ""
        self.username = ""
        self.password = ""
        self.location = ""
        self.description = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = SqlDataConnection()
        try:
            self.view_data()
        except:
            print("view data error in first run - normal if unable to find database file")

        # QMenuBar | QMenu
        self.ui.actionCreate.triggered.connect(self.btn_create_clicked)
        self.ui.actionUpdate.triggered.connect(lambda : self.btn_update_clicked(self.getSelectedDeviceID, self.hostname, self.ipaddress, self.username, self.password, self.location, self.description))
        self.ui.actionDelete.triggered.connect(lambda : self.btn_delete_clicked(self.getSelectedDeviceID, self.hostname, self.ipaddress, self.username, self.password, self.location, self.description))
        self.ui.actionExit.triggered.connect(self.close)


        # Buttons
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_create.clicked.connect(self.btn_create_clicked)
        # self.editButton = qtw.QPushButton('Edit', clicked=self.editMessages))
        self.ui.btn_update.clicked.connect(lambda : self.btn_update_clicked(self.getSelectedDeviceID, self.hostname, self.ipaddress, self.username, self.password, self.location, self.description))
        self.ui.btn_delete.clicked.connect(lambda : self.btn_delete_clicked(self.getSelectedDeviceID, self.hostname, self.ipaddress, self.username, self.password, self.location, self.description))

    # Button Connections
    def btn_create_clicked(self):
        print("btn_create_clicked id")
        self.create_window = CreateWindow()
        self.create_window.createmessage.connect(self.updateview)
        self.create_window.show()

    def btn_update_clicked(self, id, hostname, ipaddress, username, password, location, description):
        print("btn_update_clicked")
        #title="UPDATE"
        self.update_window = UpdateWindow(id, hostname, ipaddress, username, password, location, description)
        self.update_window.updatemessage.connect(self.updateview)
        self.update_window.show()

    def btn_delete_clicked(self, id, hostname, ipaddress, username, password, location, description):
        print("btn_delete_clicked")
        self.delete_dialog = DeleteDialog(id, hostname, ipaddress, username, password, location, description)
        self.delete_dialog.dialogmessage.connect(self.updateview)
        self.delete_dialog.open()


    @qtc.Slot(str)
    def updateview(self, message):
        print(f"UPDATEVIEW PRINT = {message}")
        self.view_data()

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('devices')
        self.model.select()
        self.ui.tv_tableView.setModel(self.model)

        ## Auto stretch columns except for column 0
        self.ui.tv_tableView.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.ui.tv_tableView.horizontalHeader().setSectionResizeMode(0, qtw.QHeaderView.ResizeToContents)
        # FOR Column 0 Set horizontalHeaderMinimumSectionSize = 40

        ## QTableView minipulations that are handled in the Ui, don't seem to work perhaps being overidden by other methods
        # FOR Column 0 Set horizontalHeaderMinimumSectionSize = 40
        #self.ui.tv_tableView.horizontalHeader().setSectionResizeMode(0, qtw.QHeaderView.setMinimumSectionSize(30))
        #self.ui.tv_tableView.horizontalHeader().setMinimumSectionSize(20)
        #self.ui.tv_tableView.horizontalHeader().resizeSection(0, 10) # resize the first column to 100 pixels
        #self.ui.tv_tableView.horizontalHeader().setMinimumSectionSize(15)
        #self.ui.tv_devicetable.resizeColumnsToContents()
        #self.ui.tv_tableView.resizeColumnsToContents()
        #self.ui.tv_tableView.setFocus()
        #self.ui.tv_tableView.setEditTriggers(QAbstractItemView.NoEditTriggers) # Not able to edit cells
        #self.ui.tv_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.ui.tv_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.resize(660, 530) # Resize window so table adjusts to space not needed
        #self.ui.tv_tableView.horizontalHeader().horizontalHeader.resizeSection(0, 30)
        #self.ui.tv_tableView.setColumnWidth(0, 10)
        #self.ui.tv_tableView.horizontalHeader().setMinimumSectionSize(50)
        #self.ui.tv_tableView.setColumnWidth(10)
        #self.ui.tv_tableView.resizeColumnToContents()



        # Get Row selection
        selection = self.ui.tv_tableView.selectionModel()
        selection.selectionChanged.connect(self.selectedDeviceID)

        try:
            self.ui.tv_tableView.selectRow(1)
            self.ui.tv_tableView.selectRow(0)
        except:
            print("Unable to select tableview row 0")

    def selectedDeviceID(self):
        self.getSelectedDeviceID = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[0]))
        self.hostname = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[1]))
        self.ipaddress = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[2]))
        self.username = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[3]))
        self.password = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[4]))
        self.location = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[5]))
        self.description = str(self.ui.tv_tableView.model().data(self.ui.tv_tableView.selectedIndexes()[6]))
        self.ui.statusbar.showMessage(f"Selected ID: {self.getSelectedDeviceID}") # Time option , 60000
