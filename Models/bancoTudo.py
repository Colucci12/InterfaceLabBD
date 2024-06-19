from .bancoLider import BancoLider
from .bancoOficial import BancoOficial
from .bancoCientista import BancoCientista
from .bancoComandante import BancoComandante
from .bancoVerificar import BancoVerificar
from .bancoSample import BancoSample

class BancoTudo(BancoLider, BancoCientista, BancoOficial, BancoComandante):
    def preencher(self, dados):
        self.id = int(dados['id'])
        self.cpi = str(dados['cpi'])
        self.nome = str(dados['nome'])
        self.cargo = str(dados['cargo']).strip()
        if str(dados['lider_faccao']).strip() == 'TRUE':
            self.lider_faccao = True
        else:
            self.lider_faccao = False