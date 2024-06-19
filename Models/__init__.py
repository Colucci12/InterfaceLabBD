from .bancoLider import BancoLider
from .bancoOficial import BancoOficial
from .bancoCientista import BancoCientista
from .bancoComandante import BancoComandante
from .bancoVerificar import BancoVerificar
from .bancoSample import BancoSample

mapa = {
    'Oficial': BancoOficial,
    'Lider': BancoLider,
    'Comandante': BancoComandante,
    'Cientista': BancoCientista
}

def login(key: int, senha: str):

    bdVerificar = BancoVerificar()
    retorno_login = bdVerificar.login(key, senha)

    if not retorno_login:
        del bdVerificar
        return 'Erro inesperado.'

    elif retorno_login == 500:
        del bdVerificar
        return 'Erro na conexão.'

    elif retorno_login == 404:
        del bdVerificar
        return 'Usuário não encontrado.'

    elif retorno_login == 401:
        del bdVerificar
        return 'Senha incorreta'

    elif retorno_login == 200:
        overview = bdVerificar.verificar(key)
        del bdVerificar

        dados = {
            'id': overview[0],
            'cpi': overview[1].strip(),
            'nome': overview[2].strip(),
            'cargo': overview[3].strip(),
            'lider_faccao': overview[4].strip()
        }

        return dados