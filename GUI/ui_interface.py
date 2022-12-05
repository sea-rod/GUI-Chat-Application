# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 450)
        icon = QIcon()
        icon.addFile(u":/icons/main", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"#sidebar{\n"
"background:rgb(31, 26, 36);\n"
"}\n"
"QMainWindow{\n"
"background:rgb(18, 18, 18);\n"
"}\n"
"QPushButton{\n"
"background:rgb(58, 58, 58);\n"
"border-radius:10;\n"
"color:rgb(209, 209, 209);\n"
"min-width:20;\n"
"}\n"
"QLineEdit{\n"
"border-radius:10;\n"
"border:1 solid rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"background:rgb(58, 58, 58);\n"
"color:rgb(170, 170, 170);\n"
"border-radius:10;\n"
"text-align:center;\n"
"}\n"
"#client,#server{\n"
"background:transparent;\n"
"}\n"
"#main_foot,#client_head{\n"
"border-radius:10;\n"
"}\n"
"#main{\n"
"background:rgb(18, 18, 18);\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(83, 12, 31);\n"
"}\n"
"QInputDialog{\n"
"background:rgb(86, 0, 42);\n"
"border-radius:10;\n"
"color:rgb(209, 209, 209)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(100, 0))
        self.sidebar.setStyleSheet(u"QToolButton{\n"
"border:none;\n"
"color:rgb(214, 214, 214);\n"
"padding:0 10;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:rgb(63, 2, 24);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.sidebar)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 0)
        self.side_main = QWidget(self.sidebar)
        self.side_main.setObjectName(u"side_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_main.sizePolicy().hasHeightForWidth())
        self.side_main.setSizePolicy(sizePolicy1)
        self.side_main.setMinimumSize(QSize(100, 200))
        self.side_main.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.side_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.menu_btn = QToolButton(self.side_main)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy2)
        self.menu_btn.setMinimumSize(QSize(0, 35))
        self.menu_btn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(13)
        self.menu_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/menu", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(25, 25))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.verticalLayout.addWidget(self.menu_btn)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.create_btn = QToolButton(self.side_main)
        self.create_btn.setObjectName(u"create_btn")
        sizePolicy2.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy2)
        self.create_btn.setMinimumSize(QSize(0, 35))
        self.create_btn.setMaximumSize(QSize(16777215, 16777215))
        self.create_btn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/create", QSize(), QIcon.Normal, QIcon.Off)
        self.create_btn.setIcon(icon2)
        self.create_btn.setIconSize(QSize(25, 25))
        self.create_btn.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.verticalLayout.addWidget(self.create_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.join_btn = QToolButton(self.side_main)
        self.join_btn.setObjectName(u"join_btn")
        sizePolicy2.setHeightForWidth(self.join_btn.sizePolicy().hasHeightForWidth())
        self.join_btn.setSizePolicy(sizePolicy2)
        self.join_btn.setMinimumSize(QSize(0, 35))
        self.join_btn.setMaximumSize(QSize(16777215, 16777215))
        self.join_btn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/connect", QSize(), QIcon.Normal, QIcon.Off)
        self.join_btn.setIcon(icon3)
        self.join_btn.setIconSize(QSize(25, 25))
        self.join_btn.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.verticalLayout.addWidget(self.join_btn)


        self.verticalLayout_7.addWidget(self.side_main, 0, Qt.AlignTop)

        self.frame = QFrame(self.sidebar)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.exit_btn = QToolButton(self.frame)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy2.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy2)
        self.exit_btn.setMinimumSize(QSize(0, 35))
        self.exit_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/logout", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon4)
        self.exit_btn.setIconSize(QSize(25, 25))
        self.exit_btn.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.verticalLayout_8.addWidget(self.exit_btn)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.sidebar, 0, Qt.AlignHCenter)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy3)
        self.main.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.join_frame = QWidget()
        self.join_frame.setObjectName(u"join_frame")
        sizePolicy3.setHeightForWidth(self.join_frame.sizePolicy().hasHeightForWidth())
        self.join_frame.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.join_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.client_head = QWidget(self.join_frame)
        self.client_head.setObjectName(u"client_head")
        self.client_head.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.client_head)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.client_head)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 10))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.port_id = QLineEdit(self.client_head)
        self.port_id.setObjectName(u"port_id")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.port_id.sizePolicy().hasHeightForWidth())
        self.port_id.setSizePolicy(sizePolicy4)
        self.port_id.setMinimumSize(QSize(0, 0))
        self.port_id.setFont(font)

        self.horizontalLayout_4.addWidget(self.port_id)

        self.label_2 = QLabel(self.client_head)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 20))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.host_id = QLineEdit(self.client_head)
        self.host_id.setObjectName(u"host_id")
        sizePolicy4.setHeightForWidth(self.host_id.sizePolicy().hasHeightForWidth())
        self.host_id.setSizePolicy(sizePolicy4)
        self.host_id.setMinimumSize(QSize(0, 0))
        self.host_id.setFont(font)

        self.horizontalLayout_4.addWidget(self.host_id)

        self.connect_btn = QPushButton(self.client_head)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setMinimumSize(QSize(20, 30))
        self.connect_btn.setFont(font1)
        self.connect_btn.setCheckable(True)
        self.connect_btn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.connect_btn)


        self.verticalLayout_2.addWidget(self.client_head, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.join_frame)
        self.create_frame = QWidget()
        self.create_frame.setObjectName(u"create_frame")
        self.verticalLayout_6 = QVBoxLayout(self.create_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.create_frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel{\n"
"background:rgb(58, 58, 58);\n"
"color:rgb(170, 170, 170);\n"
"border-radius:10;\n"
"}\n"
"QPushButton{\n"
"background:rgb(58, 58, 58);\n"
"color:rgb(170, 170, 170);\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(83, 12, 31);\n"
"}\n"
"QLineEdit{\n"
"background:rgb(58, 58, 58);\n"
"color:rgb(170, 170, 170);\n"
"border-radius:10;\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 0)
        self.hst_prt = QLineEdit(self.widget_2)
        self.hst_prt.setObjectName(u"hst_prt")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.hst_prt.sizePolicy().hasHeightForWidth())
        self.hst_prt.setSizePolicy(sizePolicy5)
        self.hst_prt.setMinimumSize(QSize(0, 30))
        self.hst_prt.setFont(font1)
        self.hst_prt.setStyleSheet(u"")
        self.hst_prt.setAlignment(Qt.AlignCenter)
        self.hst_prt.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.hst_prt)

        self.start_btn = QPushButton(self.widget_2)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy6)
        self.start_btn.setMinimumSize(QSize(20, 30))
        self.start_btn.setFont(font1)
        self.start_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.start_btn)


        self.verticalLayout_6.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.create_frame)

        self.verticalLayout_3.addWidget(self.stackedWidget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background:transparent;\n"
"border:0;\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.message_area = QWidget()
        self.message_area.setObjectName(u"message_area")
        self.message_area.setGeometry(QRect(0, 0, 640, 368))
        sizePolicy3.setHeightForWidth(self.message_area.sizePolicy().hasHeightForWidth())
        self.message_area.setSizePolicy(sizePolicy3)
        self.message_area.setStyleSheet(u"border-radius:10;\n"
"border:1 solid rgb(71, 71, 71);")
        self.horizontalLayout_5 = QHBoxLayout(self.message_area)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.send_mess_area = QWidget(self.message_area)
        self.send_mess_area.setObjectName(u"send_mess_area")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.send_mess_area.sizePolicy().hasHeightForWidth())
        self.send_mess_area.setSizePolicy(sizePolicy7)
        self.send_mess_area.setStyleSheet(u"background:transparent;\n"
"border:0")
        self.verticalLayout_5 = QVBoxLayout(self.send_mess_area)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)

        self.horizontalLayout_5.addWidget(self.send_mess_area)

        self.scrollArea.setWidget(self.message_area)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.main_foot = QWidget(self.main)
        self.main_foot.setObjectName(u"main_foot")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.main_foot.sizePolicy().hasHeightForWidth())
        self.main_foot.setSizePolicy(sizePolicy8)
        self.main_foot.setStyleSheet(u"QTextEdit{\n"
"border-radius:20;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.main_foot)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sendMessId = QLineEdit(self.main_foot)
        self.sendMessId.setObjectName(u"sendMessId")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(6)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sendMessId.sizePolicy().hasHeightForWidth())
        self.sendMessId.setSizePolicy(sizePolicy9)
        self.sendMessId.setMinimumSize(QSize(0, 30))
        self.sendMessId.setFont(font)
        self.sendMessId.setEchoMode(QLineEdit.Normal)
        self.sendMessId.setCursorPosition(0)

        self.horizontalLayout_3.addWidget(self.sendMessId)

        self.send_btn = QPushButton(self.main_foot)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy10)
        self.send_btn.setMinimumSize(QSize(20, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.send_btn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.send_btn)


        self.verticalLayout_3.addWidget(self.main_foot, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"    Menu", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"    Create", None))
        self.join_btn.setText(QCoreApplication.translate("MainWindow", u"     Join", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"    Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_id.setText(QCoreApplication.translate("MainWindow", u"8080", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.hst_prt.setText(QCoreApplication.translate("MainWindow", u"serevr started on host:port", None))
        self.hst_prt.setPlaceholderText("")
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.sendMessId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

