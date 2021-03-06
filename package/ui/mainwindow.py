from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import (QStandardItem, QStandardItemModel, QColor)
from PyQt5.QtCore import (QVariant, Qt)

from .widgets.mainwindow import Ui_MainWindow

from ..odoo import Manager
from ..data import ProgramData

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None, Qt.WindowStaysOnTopHint)

        self.setupUi(self)

        self.update_list_button.clicked.connect(self.update_list)
        self.upgrade_button.clicked.connect(self.upgrade_selected_modules)
        self.install_button.clicked.connect(self.install_selected_modules)
        self.uninstall_button.clicked.connect(self.uninstall_selected_modules)

        # self.save_button.clicked.connect(self.save_selected_modules)

        # self._data = ProgramData()

        self._odoo_manager = Manager()
        self._odoo_manager.connect()

    def update_list(self):
        model = QStandardItemModel(self.modules_list)
        
        for module in self._odoo_manager.get_modules():
            item = QStandardItem()
            item.setCheckable(True)

            item.setData(module.name, Qt.DisplayRole)
            item.setData(QVariant(module), Qt.UserRole)

            if module.state != 'installed':
                item.setBackground(QColor('#7fc97f'))
            
            model.appendRow(item)

        self.modules_list.setModel(model)

    def upgrade_selected_modules(self):
        self._odoo_manager.upgrade_modules(self._get_selected_modules())

    def install_selected_modules(self):
        self._odoo_manager.install_modules(self._get_selected_modules())

    def uninstall_selected_modules(self):
        self._odoo_manager.uninstall_modules(self._get_selected_modules())

    # def save_selected_modules(self):
    #     self._data.set_modules(self._get_selected_modules())

    def _get_selected_modules(self):
        model = self.modules_list.model()
        for index in range(model.rowCount()):
            yield model.item(index).data(Qt.UserRole).name