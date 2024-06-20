import oracledb
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

    def insere_estrela(self, estrela, nome, classificacao, massa, x, y, z):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCIENTISTA_INSEREESTRELA', [self.id, estrela, nome, classificacao, massa, x, y, z])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def altera_estrela(self, antigo_estrela, novo_estrela, nome, classificacao, massa, x, y, z):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCIENTISTA_ATUALIZAESTRELA', [self.id, antigo_estrela, novo_estrela, nome, classificacao, massa, x, y, z])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def remove_estrela(self, estrela):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCIENTISTA_REMOVEESTRELA', [self.id, estrela])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message