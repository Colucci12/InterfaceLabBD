import oracledb
import json

class BancoSample():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BancoSample, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.id = int
        self.cpi = str
        self.nome = str
        self.cargo = str
        self.lider_faccao = bool

        with open('Models/credentials.json', 'r') as file:
            credentials = json.load(file)

        try:
            dsn = oracledb.makedsn(host=credentials['hostname'],
                                   port=credentials['port'],
                                   service_name=credentials['service_name'])

            self.connection = oracledb.connect(user=credentials['username'],
                                               password=credentials['password'],
                                               dsn=dsn)

            self.cursor = self.connection.cursor()

        except:
            self._instance = None
            raise oracledb.DatabaseError

    def __del__(self):
        self._instance = None