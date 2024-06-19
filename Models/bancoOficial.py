from .bancoSample import BancoSample

class BancoOficial(BancoSample):
    def oficial(self):
        print('Iniciou Oficial!')

    def relatorio_oficial(self, agrupamento):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_OFICIAL', [2, 'faccao', ref_cursor])

        return ref_cursor.fetchall()