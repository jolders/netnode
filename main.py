import sys
#from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6 import QtWidgets as qtw

from mainWindow import MainWindow

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    # Stylesheet option disengaged at the moment
    #with open("mystyle.css", "r") as file:
    #    app.setStyleSheet(file.read())
    app.setStyle('Fusion')
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec())
