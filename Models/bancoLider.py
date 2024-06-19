from .bancoSample import BancoSample

class BancoLider(BancoSample):
    def lider(self):
        print('Iniciou Lider!')

    def relatorio_lider(self, agrupamento):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_LIDERFACCAO', [self.id, agrupamento, ref_cursor])

        return ref_cursor.fetchone()
