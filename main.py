from InterfaceLabBD.Models.bancoTudo import BancoTudo
from InterfaceLabBD.Models import login

acessos = login(2, 'senha_padrao')
banco = BancoTudo()
banco.preencher(acessos)

x = banco.relatorio_lider('faccao')