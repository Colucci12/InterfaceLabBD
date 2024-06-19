from .bancoSample import BancoSample

class BancoComandante(BancoSample):
    def comandante(self):
        print('Iniciou Comandante!')

    def relatorio_comandante_dominados(self):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_COMANDANTE_PLANETASDOMINADOS', [ref_cursor])

        return ref_cursor.fetchall()

    def relatorio_comandante_potencial(self):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO', [ref_cursor])

        return ref_cursor.fetchall()