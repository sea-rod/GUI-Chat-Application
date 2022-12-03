# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GetName.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_diaName(object):
    def setupUi(self, diaName):
        if not diaName.objectName():
            diaName.setObjectName(u"diaName")
        diaName.resize(238, 109)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(diaName.sizePolicy().hasHeightForWidth())
        diaName.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/main", QSize(), QIcon.Normal, QIcon.Off)
        diaName.setWindowIcon(icon)
        diaName.setStyleSheet(u"*{\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"QDialog{\n"
"background:rgb(18, 18, 18);\n"
"}\n"
"QPushButton{\n"
"background:rgb(58, 58, 58);\n"
"border-radius:10;\n"
"color:rgb(209, 209, 209);\n"
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
"QPushButton:hover{\n"
"background:rgb(83, 12, 31);\n"
"}\n"
"QInputDialog{\n"
"background:rgb(86, 0, 42);\n"
"border-radius:10;\n"
"color:rgb(209, 209, 209)\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(diaName)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(diaName)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.name = QLineEdit(diaName)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(220, 25))
        self.name.setMaximumSize(QSize(16777215, 16777215))
        self.name.setFont(font)

        self.verticalLayout_2.addWidget(self.name, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(diaName)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok = QPushButton(self.frame)
        self.ok.setObjectName(u"ok")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy2)
        self.ok.setMinimumSize(QSize(80, 25))
        font1 = QFont()
        font1.setPointSize(10)
        self.ok.setFont(font1)

        self.horizontalLayout.addWidget(self.ok, 0, Qt.AlignHCenter)

        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(80, 25))
        self.cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.cancel, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(diaName)

        QMetaObject.connectSlotsByName(diaName)
    # setupUi

    def retranslateUi(self, diaName):
        diaName.setWindowTitle(QCoreApplication.translate("diaName", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("diaName", u"Enter Your Name", None))
        self.name.setText(QCoreApplication.translate("diaName", u"User1", None))
        self.ok.setText(QCoreApplication.translate("diaName", u"Ok", None))
        self.cancel.setText(QCoreApplication.translate("diaName", u"Cancel", None))
    # retranslateUi

