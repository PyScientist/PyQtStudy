import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from layout_1_responce import Ui_MainWindow


class QC(QMainWindow):
    def __init__(self):
        super(QC, self).__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.log_out_btn(self)

    def log_out_btn(self):
        text = ui.btn_log_out.text('jkdhdsbfvcx')
        return text



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
