import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from layout_1_responce import Ui_MainWindow


class QC(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log_out_btn_adjust()
        #self.btn_start_stop_scan.setCheckable(True)
        #self.btn_start_stop_scan.clicked.connect(self.hide_top_layout)

    def log_out_btn_adjust(self):
        text = self.btn_log_out.setText('log out button')
        self.btn_log_out.setCheckable(True)
        self.btn_log_out.clicked.connect(self.hide_top_layout)

        return text

    def hide_top_layout(self):
        if self.btn_log_out.isChecked():
            self.horizontalFrame_core_and_cconsole.show()
        else:
            self.horizontalFrame_core_and_cconsole.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qc = QC()
    qc.show()
    sys.exit(app.exec())
