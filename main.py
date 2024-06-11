import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec())
