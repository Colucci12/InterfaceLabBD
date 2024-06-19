from .bancoLider import BancoLider
from .bancoOficial import BancoOficial
from .bancoCientista import BancoCientista
from .bancoComandante import BancoComandante
from .bancoVerificar import BancoVerificar

mapa = {
    'Oficial': BancoOficial,
    'Lider': BancoLider,
    'Comandante': BancoComandante,
    'Cientista': BancoCientista
}

def login(key: str, senha: int):

    bdVerificar = BancoVerificar()
    retorno_verificacao = bdVerificar.verificar(key, senha) #TODO: realmente verificar
    del bdVerificar

    temp = []
    for x in retorno_verificacao:
        if x in mapa:
            temp.append(mapa[x])

    perfis = tuple(temp)
    class BancoUsuario(*perfis):
        def __init__(self):
            pass

        def guarda_login(self, key):
            self.key = key

    banco = BancoUsuario()
    banco.guarda_login(key)
    return banco