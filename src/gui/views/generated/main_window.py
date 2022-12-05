# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.team_combobox = QComboBox(self.centralwidget)
        self.team_combobox.setObjectName(u"team_combobox")

        self.gridLayout.addWidget(self.team_combobox, 3, 1, 1, 1)

        self.team_label = QLabel(self.centralwidget)
        self.team_label.setObjectName(u"team_label")

        self.gridLayout.addWidget(self.team_label, 0, 1, 1, 1)

        self.game_number_label = QLabel(self.centralwidget)
        self.game_number_label.setObjectName(u"game_number_label")

        self.gridLayout.addWidget(self.game_number_label, 0, 2, 1, 1)

        self.game_number_combobox = QComboBox(self.centralwidget)
        self.game_number_combobox.setObjectName(u"game_number_combobox")

        self.gridLayout.addWidget(self.game_number_combobox, 3, 2, 2, 1)

        self.display_table = QTableView(self.centralwidget)
        self.display_table.setObjectName(u"display_table")

        self.gridLayout.addWidget(self.display_table, 7, 0, 1, 3)

        self.display_button = QPushButton(self.centralwidget)
        self.display_button.setObjectName(u"display_button")

        self.gridLayout.addWidget(self.display_button, 5, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.year_line_edit = QLineEdit(self.centralwidget)
        self.year_line_edit.setObjectName(u"year_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_line_edit.sizePolicy().hasHeightForWidth())
        self.year_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.year_line_edit, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.team_label.setText(QCoreApplication.translate("MainWindow", u"Team:", None))
        self.game_number_label.setText(QCoreApplication.translate("MainWindow", u"Game Number:", None))
        self.display_button.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Season Year:", None))
    # retranslateUi

