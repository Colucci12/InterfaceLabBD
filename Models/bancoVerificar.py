from .bancoSample import BancoSample

class BancoVerificar(BancoSample):
    def verificar(self, key, senha):
        #TODO: verificar quais "roles" o usuario logado pertence
        return ['Comandante', 'Lider']