import sqlite3

class ProgramData():
    def __init__(self):
        self._exe([lambda c: c.execute('CREATE TABLE IF NOT EXISTS modules (name TEXT PRIMARY KEY)')]) #id INTEGER PRIMARY KEY AUTOINCREMENT, 

    def set_modules(self, modules):
        self._exe([lambda c: c.execute('REPLACE INTO modules (name) VALUES (?)', modules)])
    
    def delete_modules(self, modules):
        self._exe(lambda c: c.execute('DELETE FROM modules WHERE name=?', modules))

    def get_modules(self):
        for row in self._select(lambda c: c.execute('SELECT * FROM modules ORDER BY name')):
            yield row

    def _set_tables(self, c):
        c.execute('''CREATE TABLE IF NOT EXISTS modules
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')


    def _exe(self, operations):
        db = sqlite3.connect('base.db')
        for operation in operations:
            operation(db.cursor())
        db.commit()
        db.close()

    def _select(self, operation):
        db = sqlite3.connect('base.db')
        for row in operation(db.cursor()):
            yield row
        db.commit()
        db.close()
        
