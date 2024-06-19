import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw # QApplication, QMainWindow, QWidget, QDialog
from PySide6 import QtGui as qtg
from PySide6 import QtSql as qts # QSqlQuery, QSqlDatabase

from ui_createUpdateWindow import Ui_createUpdate
from ui_deleteDialog import Ui_Dialog
from sqlConnection import SqlDataConnection

#   MainWIndow         pyside6-uic mainWindow.ui -o Ui_mainWindow.py
#   CreateWindow       pyside6-uic createUpdateWindow.ui -o ui_createUpdateWindow.py

class CreateWindow(qtw.QWidget, Ui_createUpdate):

    createmessage = qtc.Signal(str)

    def __init__(self):
        super().__init__()

        self.uic = Ui_createUpdate()
        self.uic.setupUi(self)

        self.uic.lbl_title.setText("CREATE window")
        self.uic.lbl_title.setProperty("class", "heading")
        self.uic.btn_submit.clicked.connect(self.btn_submit_create)

        self.uic.lbl_showid.setText("A new ID will be created")
        self.uic.le_hostname.setPlaceholderText("enter a hostname")
        self.uic.le_ipaddress.setPlaceholderText("enter a ipaddress")
        self.uic.le_username.setPlaceholderText("enter a username")
        self.uic.le_password.setPlaceholderText("enter a password")
        self.uic.le_location.setPlaceholderText("enter a location")
        self.uic.pte_description.setPlaceholderText("enter a description")

        self.uic.btn_exit.clicked.connect(self.close)


    @qtc.Slot()
    def btn_submit_create(self):
        print("uic-btn_submit_create")

        hostname = self.uic.le_hostname.text()
        ipaddress = self.uic.le_ipaddress.text()
        username = self.uic.le_username.text()
        password = self.uic.le_password.text()
        location = self.uic.le_location.text()
        pte_description = self.uic.pte_description.toPlainText()

        # Brfore we send for isertion lets check we're getting the results
        print (f"hostname: {hostname}")
        print (f"ipaddress: {ipaddress}")
        print (f"username: {username}")
        print (f"password: {password}")
        print (f"location: {location}")
        print (f"pte_description: {pte_description}")

        # SQL CREATE | Send message to reset the viewtable | Close the CREATE window
        SqlDataConnection.create_new_device(self, hostname, ipaddress, username, password, location, pte_description)
        self.createmessage.emit("I am just another CREATE window")
        self.close()


class UpdateWindow(qtw.QWidget, Ui_createUpdate):

    updatemessage = qtc.Signal(str)

    def __init__(self, id, hostname, ipaddress, username, password, location, description):
        super().__init__()

        self.uiu = Ui_createUpdate()
        self.uiu.setupUi(self)

        print (f"id: {id}")
        print (f"hostname: {hostname}")
        print (f"ipaddress: {ipaddress}")
        print (f"username: {username}")
        print (f"password: {password}")
        print (f"location: {location}")
        print(f"pte_description = {description}")

        self.uiu.lbl_showid.setText(f"{id}")
        self.uiu.le_hostname.setText(hostname)
        self.uiu.le_ipaddress.setText(ipaddress)
        self.uiu.le_username.setText(username)
        self.uiu.le_password.setText(password)
        self.uiu.le_location.setText(location)
        self.uiu.pte_description.setPlainText(description)

        self.uiu.lbl_title.setText("UPDATE window")
        self.uiu.lbl_title.setProperty("class", "heading")
        self.uiu.btn_submit.clicked.connect(lambda : self.btn_submit_update(id))
        self.uiu.btn_exit.clicked.connect(self.close)


    @qtc.Slot()
    def btn_submit_update(self, id):
        print(f"uicu-btn_submit_update: id = {id}")

        new_hostname = self.uiu.le_hostname.text()
        new_ipaddress = self.uiu.le_ipaddress.text()
        new_username = self.uiu.le_username.text()
        new_password = self.uiu.le_password.text()
        new_location = self.uiu.le_location.text()
        new_description = self.uiu.le_description.text()
        pte_description = self.uiu.pte_description.toPlainText()

        print(f"id = {id}")
        print(f"input_hostname = {new_hostname}")
        print(f"input_ipaddress = {new_ipaddress}")
        print(f"input_username = {new_username}")
        print(f"input_password = {new_password}")
        print(f"input_location = {new_location}")
        print(f"pte_description = {pte_description}")

        # SQL UPDATE | Send message to reset the viewtable | Close the UPDATE window
        SqlDataConnection.update_device(self, new_hostname, new_ipaddress, new_username, new_password, new_location, pte_description, id)
        self.updatemessage.emit("I am just another UPDATE window")
        self.close()


class DeleteDialog(qtw.QDialog, Ui_Dialog):
    dialogmessage = qtc.Signal(str)
    def __init__(self, id, hostname, ipaddress, username, password, location, description):
        super().__init__()
        self.uid = Ui_Dialog()
        self.uid.setupUi(self)

        self.uid.lbl_idresult.setText(id)
        self.uid.lbl_hostnameresult.setText(hostname)
        self.uid.lbl_ipaddressresult.setText(ipaddress)
        self.uid.lbl_usernameresult.setText(username)
        self.uid.lbl_passwordresult.setText(password)
        self.uid.lbl_locationresult.setText(location)
        self.uid.lbl_descriptionresult.setText(description)
        #self.uid.pte_description.toPlainText(description)


        self.uid.buttonBox.accepted.connect(lambda : self.btn_accepted_clicked(id))
        #self.uid.buttonBox.rejected.connect(Dialog.reject)
        #self.uid.buttonBox.accepted.setText("Delete")

    def btn_accepted_clicked(self, id):
        print(f"btn_accepted_clicked | id = {id}")

        # SQL DELETE | Send message to reset the viewtable | Window closes automatically
        SqlDataConnection.delete_device(self, id)
        self.dialogmessage.emit("I am just another DIALOG window")







