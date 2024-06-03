
from auth import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import *
from main import PrinterMain
import sys

class Avtoriza(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_auth.clicked.connect(self.open)
        self.pb_exit.clicked.connect(self.exit)

    def open(self):
        if self.lineEdit_log.text() == 'admin' and self.lineEdit_psw.text() == '1234':
            self.admin_window = PrinterMain()
            self.admin_window.show()
            self.close()
    


    def exit(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Avtoriza()
    window.show()
    sys.exit(app.exec_())
