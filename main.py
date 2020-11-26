from PySide2 import QtWidgets
from ui.mainwindow_ui import MainWindow_UI
import sys


class MainWindow(QtWidgets.QMainWindow, MainWindow_UI):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())