import oracledb

from .bancoSample import BancoSample

class BancoVerificar(BancoSample):
    def login(self, id, senha):
        try:
            status_code = self.cursor.var(oracledb.NUMBER)
            self.cursor.callproc('USER_LOGIN', [id, senha, status_code])

            status_code_value = status_code.getvalue()
            return status_code_value

        except:
            return None

    def verificar(self, id):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('OVERVIEW', [id, ref_cursor])

        return ref_cursor.fetchone()