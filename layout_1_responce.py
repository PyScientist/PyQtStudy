# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout_1_responce.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 796)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_hide_1 = QPushButton(self.centralwidget)
        self.btn_hide_1.setObjectName(u"btn_hide_1")
        self.btn_hide_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_hide_1)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalFrame_1_main = QFrame(self.centralwidget)
        self.verticalFrame_1_main.setObjectName(u"verticalFrame_1_main")
        self.verticalLayout = QVBoxLayout(self.verticalFrame_1_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalFrame_1_main)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_log_out = QPushButton(self.verticalFrame_1_main)
        self.btn_log_out.setObjectName(u"btn_log_out")
        self.btn_log_out.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_log_out)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.btn_start_stop_scan = QPushButton(self.verticalFrame_1_main)
        self.btn_start_stop_scan.setObjectName(u"btn_start_stop_scan")
        self.btn_start_stop_scan.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_start_stop_scan)

        self.pushButton = QPushButton(self.verticalFrame_1_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalFrame_core_and_cconsole = QFrame(self.verticalFrame_1_main)
        self.horizontalFrame_core_and_cconsole.setObjectName(u"horizontalFrame_core_and_cconsole")
        self.horizontalFrame_core_and_cconsole.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_core_and_cconsole)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget_core = QTableWidget(self.horizontalFrame_core_and_cconsole)
        self.tableWidget_core.setObjectName(u"tableWidget_core")
        self.tableWidget_core.setSizeIncrement(QSize(0, 0))
        self.tableWidget_core.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.tableWidget_core)

        self.textBrowser = QTextBrowser(self.horizontalFrame_core_and_cconsole)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_3.addWidget(self.textBrowser)

        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout.addWidget(self.horizontalFrame_core_and_cconsole)


        self.gridLayout.addWidget(self.verticalFrame_1_main, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btn_hide_2 = QPushButton(self.centralwidget)
        self.btn_hide_2.setObjectName(u"btn_hide_2")
        self.btn_hide_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_hide_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btn_hide_3 = QPushButton(self.centralwidget)
        self.btn_hide_3.setObjectName(u"btn_hide_3")
        self.btn_hide_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 50;\n"
"height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_hide_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.horizontalFrame_3_img_port = QFrame(self.centralwidget)
        self.horizontalFrame_3_img_port.setObjectName(u"horizontalFrame_3_img_port")
        self.horizontalFrame_3_img_port.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_3_img_port)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.horizontalFrame_3_img_port, 5, 0, 1, 1)

        self.horizontalFrame_2_console = QFrame(self.centralwidget)
        self.horizontalFrame_2_console.setObjectName(u"horizontalFrame_2_console")
        self.horizontalFrame_2_console.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame_2_console)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget_console = QTableWidget(self.horizontalFrame_2_console)
        self.tableWidget_console.setObjectName(u"tableWidget_console")

        self.horizontalLayout_7.addWidget(self.tableWidget_console)


        self.gridLayout.addWidget(self.horizontalFrame_2_console, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QC", None))
        self.btn_hide_1.setText("")
        self.label.setText("")
        self.btn_log_out.setText("")
        self.btn_start_stop_scan.setText("")
        self.pushButton.setText("")
        self.btn_hide_2.setText("")
        self.btn_hide_3.setText("")
    # retranslateUi

