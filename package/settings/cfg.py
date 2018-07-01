import configparser

class Cfg():
    def __init__(self, path):
        cfg = configparser.ConfigParser()
        cfg.read(path)

        self.host = cfg.get('host', 'host')
        self.port = int(cfg.get('host', 'port'))
        self.db_name = cfg.get('database', 'name')
        self.db_user = cfg.get('database', 'user')
        self.db_password = cfg.get('database', 'password')
        