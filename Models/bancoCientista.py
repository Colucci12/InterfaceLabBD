from .bancoSample import BancoSample

class BancoCientista(BancoSample):
    def cientista(self):
        print('Iniciou cientista!')

    def relatorio_cientista_planeta(self):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_CIENTISTA_PLANETAS', [ref_cursor])

        return ref_cursor.fetchall()

    def relatorio_cientista_estrela(self):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_CIENTISTA_ESTRELAS', [ref_cursor])

        return ref_cursor.fetchall()

    def relatorio_cientista_sistema(self):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_CIENTISTA_SISTEMAS', [ref_cursor])

        return ref_cursor.fetchall()