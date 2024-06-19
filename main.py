from InterfaceLabBD.Models.bancoTudo import BancoTudo
from InterfaceLabBD.Models import login

acessos = login(2, 'senha_padrao')
banco = BancoTudo()
banco.preencher(acessos)

#x = banco.relatorio_lider('faccao')

rc1 = banco.relatorio_cientista_estrela()
rc2 = banco.relatorio_cientista_planeta()
rc3 = banco.relatorio_cientista_sistema()

print(rc1)
print(rc2)
print(rc3)