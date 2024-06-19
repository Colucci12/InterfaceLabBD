import oracledb

from .bancoSample import BancoSample

class BancoLider(BancoSample):
    def lider(self):
        print('Iniciou Lider!')

    def relatorio_lider(self, agrupamento):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_LIDERFACCAO', [self.id, agrupamento, ref_cursor])

        return ref_cursor.fetchall()

    def lider_alterarnome_faccao(self, novonome):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCLIDER_ALTERARNOMEFACCAO', [self.id, novonome])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def lider_indicar_novo(self, novolider):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCLIDER_INDICARNOVOLIDER', [self.id, novolider])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message
