from InterfaceLabBD.Models.bancoTudo import BancoTudo
from InterfaceLabBD.Models import login

acessos = login(1, 'senha_padrao')
banco = BancoTudo()
banco.preencher(acessos)


"""# =============== RELATORIOS =================
rci1 = banco.relatorio_cientista_estrela()
rci2 = banco.relatorio_cientista_planeta()
rci3 = banco.relatorio_cientista_sistema()
print(rci1)
print(rci2)
print(rci3)"""


"""
rco1 = banco.relatorio_comandante_dominados()
rco2 = banco.relatorio_comandante_potencial()
print(rco1)
print(rco2)

rof = banco.relatorio_oficial('faccao')
print(rof)

rlf = banco.relatorio_lider('faccao')
print(rlf)
"""


# =============== FUNCIONALIDADES =================
fl1 = banco.lider_alterarnome_faccao('FaccaoNova')
fl2 = banco.lider_indicar_novo('123.123.123-11')
fl3 = banco.lider_credenciar_comunidade('Faccao1', 'EspecieY', 'Comunidade2', 'PlanetaXX')
fl4 = banco.lider_remover_faccao_nacao('NacaoZ')
print(fl1)
print(fl2)
print(fl3)
print(fl4)

