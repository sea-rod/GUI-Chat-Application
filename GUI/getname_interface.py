from .ui_GetName import Ui_diaName
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Qt


class NameWind(QDialog, Ui_diaName):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Name")
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.ok.clicked.connect(self.close)
        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)
