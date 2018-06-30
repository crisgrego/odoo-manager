import sys
import odoorpc
from .modules import Modules
from .cfg import Cfg

class Manager():
    def __init__(self):
       self._odoo = None
       self._cfg = Cfg('./config.ini')

    def connect(self):
        self._odoo = odoorpc.ODOO(host=self._cfg.host, port=self._cfg.port, timeout=400)
        self._odoo.login(self._cfg.db_name, self._cfg.db_user, self._cfg.db_password)

    def upgrade_modules(self, names):
        Modules(self._odoo).upgrade_modules(names)
    
    def install_modules(self, names):
        Modules(self._odoo).install_modules(names)

    def uninstall_modules(self, names):
        Modules(self._odoo).uninstall_modules(names)

    def get_modules(self):
        return Modules(self._odoo).get_all()

    def print_all_modules(self):
        for module in Modules(self._odoo).getAll():
            print(module.name)
