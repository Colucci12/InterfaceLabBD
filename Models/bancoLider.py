import oracledb

from .bancoSample import BancoSample

class BancoLider(BancoSample):
    def lider(self):
        print('Iniciou Lider!')

    def relatorio_lider(self, agrupamento):
        ref_cursor = self.connection.cursor()
        self.cursor.callproc('PACKAGE_RELATORIOS.PROCED_RELATORIO_LIDERFACCAO', [self.id, agrupamento, ref_cursor])

        temp = ref_cursor.fetchall()
        print(temp)
        return temp

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

    def lider_credenciar_comunidade(self, faccao, especie, comunidade, planeta):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCLIDER_CREDENCIARCOMUNIDADE', [self.id, faccao, especie, comunidade, planeta])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def lider_remover_faccao_nacao(self, nacao):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCLIDER_REMOVERFACCAONACAO', [self.id, nacao])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message
