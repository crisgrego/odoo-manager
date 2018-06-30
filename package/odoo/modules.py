
class Modules():
    def __init__(self, odoo):
        self._manager = odoo.env['ir.module.module']

    def upgrade_modules(self, names):
        self._bulk_act(modules_names=names, act=self._upgrade_module)
    
    def install_modules(self, names):
        self._bulk_act(modules_names=names, act=self._install_module)

    def uninstall_modules(self, names):
        self._bulk_act(modules_names=names, act=self._uninstall_module)
    
    def get_all(self):
        self.update_list()
        return self._manager.browse(self._manager.search([]))
    
    def update_list(self):
        self._manager.update_list()

    def _upgrade_module(self, module):
        if module.state == 'installed':
            module.button_immediate_upgrade()

    def _install_module(self, module):
        if module.state != 'installed':
            module.button_immediate_install()

    def _uninstall_module(self, module):
        if module.state == 'installed':
            module.button_immediate_uninstall()

    def _bulk_act(self, modules_names, act):      
        for name in modules_names:
            module_id = self._manager.search([['name', '=', name]])
            for module in self._manager.browse(module_id):
                act(module)

