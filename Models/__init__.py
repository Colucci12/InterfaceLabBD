from .bancoLider import BancoLider
from .bancoOficial import BancoOficial
from .bancoCientista import BancoCientista
from .bancoComandante import BancoComandante
from .bancoVerificar import BancoVerificar

mapa = {
    'C': BancoCientista,
    'L': BancoLider,
    'Comandante': BancoComandante,
    'Oficial': BancoOficial
}

def login(key: str, senha: int):

    bdVerificar = BancoVerificar()
    retorno_verificacao = bdVerificar.verificar(key, senha) #TODO: realmente verificar
    del bdVerificar

    perfis = tuple(mapa[char] for char in retorno_verificacao if char in mapa)
    class BancoUsuario(*perfis):
        def __init__(self, key):
            self.key = key

        def teste(self):
            print('Teste com êxito!')

    return BancoUsuario(key)