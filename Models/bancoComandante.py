from .bancoSample import BancoSample
import oracledb

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

    def incluir_nacao_federacao(self, federacao):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO', [self.id, federacao])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def excluir_nacao_federacao(self):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCOMANDANTE_EXCLUIRNACAOFEDERACAO', [self.id])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def criar_federacao(self, federacao):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO', [self.id, federacao])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message

    def inserir_dominancia(self, planeta):
        try:
            self.cursor.callproc('PACKAGE_FUNCIONALIDADES.FUNCCOMANDANTE_INSERIRDOMINANCIA', [self.id, planeta])

            return 'SUCESSO'

        except oracledb.DatabaseError as e:
            erro, = e.args
            return erro.message
