import oracledb
import json

class BancoSample():
    def __init__(self):
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)

        try:
            dsn = oracledb.makedsn(host=credentials['hostname'],
                                   port=credentials['port'],
                                   service_name=credentials['service_name'])

            self.connection = oracledb.connect(user=credentials['username'],
                                               password=credentials['password'],
                                               dsn=dsn)

        except:
            raise oracledb.DatabaseError