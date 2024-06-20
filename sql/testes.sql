/*
USERS PARA TESTAR:
ID:1 - SENHA:senha_padrao - Lider de faccao(sem registros filhos) e Cientista
ID:2 - SENHA:senha_padrao - Lider de faccao e Cientista
ID:3 - SENHA:senha_padrao - Lider de faccao e Comandante
ID:4 - SENHA:senha_padrao - Lider de faccao e Oficial
ID:5 - SENHA:senha_padrao - Cientista
ID:6 - SENHA:senha_padrao - Comandante
ID:7 - SENHA:senha_padrao - Oficial
ID:8 - SENHA:senha_padrao - Aspirante a lider de faccao (recebe indicacao) e Comandante
*/


--:: TESTE DAS FUNCIONALIDADES DE LIDER //////////////////////////////////////////////////////////////////////////////////

/*
FUNCLIDER_ALTERARNOMEFACCAO
*/
DECLARE
    p_Userid NUMBER;
    p_NovoNome VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    p_novonome := 'Testes abaixo';
    FUNCLIDER_ALTERARNOMEFACCAO(p_userid, p_novonome);
END;
/*
Teste sucesso:
p_userid := '1';
p_novonome := 'FaccaoNova';

Teste erro (Já existe uma facção com o nome fornecido.):
p_userid := '1';
p_novonome := 'Faccao1';

Teste erro (Não é possível alterar o nome porque a facção possui registros filhos.):
p_userid := '2';
p_novonome := 'Faccao1Nova';
*/


/*
FUNCLIDER_INDICARNOVOLIDER
*/
DECLARE
    p_Userid NUMBER;
    p_NovoLider CHAR(14);
BEGIN
    p_userid := 'Testes abaixo';
    p_novolider := 'Testes abaixo';
    FUNCLIDER_INDICARNOVOLIDER(p_userid, p_novolider);
END;
/*
Teste sucesso:
p_userid := '1';
p_novolider := '222.222.222-22';     --UserID=8

Teste erro (Usuário não é líder de facção ou novo lider nao encontrado.):
p_userid := '1';
p_novolider := '123.123.123-56';

Teste erro (O novo lider indicado ja lidera uma faccao.):
p_userid := '1';
p_novolider := '123.123.123-11';
*/


/*
FUNCLIDER_CREDENCIARCOMUNIDADE
*/
DECLARE
    p_Userid NUMBER;
    p_Faccao VARCHAR2(15);
    p_Especie VARCHAR2(15);
    p_Comunidade VARCHAR2(15);
    p_Planeta VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    p_faccao := 'Testes abaixo';
    p_especie := 'Testes abaixo';
    p_comunidade := 'Testes abaixo';
    p_planeta := 'Testes abaixo';
    FUNCLIDER_CREDENCIARCOMUNIDADE(p_userid, p_faccao, p_especie, p_comunidade, p_planeta);
END;
/*
Teste sucesso:
p_userid := '2';
p_faccao := 'Faccao1';
p_especie := 'EspecieY';
p_comunidade := 'Comunidade2';
p_planeta := 'PlanetaXX';

Teste erro (Esse credenciamento ja existe.):
p_userid := '2';
p_faccao := 'Faccao1';
p_especie := 'EspecieX';
p_comunidade := 'Comunidade1';
p_planeta := 'PlanetaXX';

Teste erro (Os dados passados como parametros nao foram encontrados.):
p_userid := '20';
p_faccao := 'Faccao1';
p_especie := 'EspecieX';
p_comunidade := 'Comunidade1';
p_planeta := 'PlanetaXX';

Teste erro (A facção não está presente em nações que dominam o planeta especificado.):
p_userid := '20';
p_faccao := 'Faccao1';
p_especie := 'EspecieX';
p_comunidade := 'Comunidade1';
p_planeta := 'PlanetaXX';
*/


/*
FUNCLIDER_REMOVERFACCAONACAO
*/
DECLARE
    p_Userid NUMBER;
    p_Faccao VARCHAR2(15);
    p_Nacao VARCHAR(15);
BEGIN
    p_userid := 'Testes abaixo';
    p_nacao := 'Testes abaixo';
    FUNCLIDER_REMOVERFACCAONACAO(p_userid, p_nacao);
END;
/*
Teste sucesso:
p_userid := '2';
p_nacao := 'NacaoY';

Teste erro (Os dados passados como parametros nao foram encontrados.):
p_userid := '20';
p_nacao := 'NacaoZ';
*/





--:: TESTE DAS FUNCIONALIDADES DE COMANDANTE //////////////////////////////////////////////////////////////////////////////////

/*
FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO
*/
DECLARE
    p_Userid NUMBER;
    p_federacao VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    p_federacao  := 'Testes abaixo';
    FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO(p_userid, p_federacao);
END;
/*
Teste sucesso:
p_userid := '3';
p_federacao  := 'FederacaoX';

Teste erro (Federação não encontrada.):
p_userid := '3';
p_federacao  := 'FedFedFed';

Teste erro (Usuário não é comandante ou nação não encontrada.):
p_userid := '2';
p_federacao  := 'FederacaoX';
*/


/*
FUNCCOMANDANTE_EXLUIRNACAOFEDERACAO
*/
DECLARE
    p_Userid NUMBER;
BEGIN
    p_userid := 'Testes abaixo';
    FUNCCOMANDANTE_EXCLUIRNACAOFEDERACAO(p_userid);
END;
/*
Teste sucesso:
p_userid := '3';

Teste erro(A nação não possui nenhuma federação atrelada.):
Aqui na verdade nao acontece um erro, ele so seta a faccao como nula;
*/


/*
FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO
*/
DECLARE
    p_Userid NUMBER;
    federacao VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    federacao := 'Testes abaixo';
    FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO(p_userid,federacao);
END;
/*
Teste sucesso:
p_userid := '3';
federacao := 'FederacaoNova';

Teste erro(Federacao ja existe.):
p_userid := '3';
federacao := 'FederacaoX';
*/


/*
FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO
*/
DECLARE
    p_Userid NUMBER;
    federacao VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    federacao := 'Testes abaixo';
    FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO(p_userid,federacao);
END;
/*
Teste sucesso:
p_userid := '3';
federacao := 'FederacaoNova';

Teste erro(Federacao ja existe.):
p_userid := '3';
federacao := 'FederacaoX';
*/


/*
FUNCCOMANDANTE_INSERIRDOMINANCIA
*/
DECLARE
    p_Userid NUMBER;
    p_planeta VARCHAR2(15);
BEGIN
    p_userid := 'Testes abaixo';
    p_planeta := 'Testes abaixo';
    FUNCCOMANDANTE_INSERIRDOMINANCIA(p_userid,p_planeta);
END;
/*
Teste sucesso:
p_userid := '3';
federacao := 'PlanetaWW';

Teste erro(O planeta já está sendo dominado por outra nação.):
p_userid := '3';
federacao := 'PlanetaXX';
*/





--:: TESTE DAS FUNCIONALIDADES DE CIENTISTA //////////////////////////////////////////////////////////////////////////////////

/*
FUNCCIENTISTA_INSEREESTRELA
*/
DECLARE
    p_Userid NUMBER;
    id_estrela VARCHAR2(31);
    nome VARCHAR2(31);
    classificacao VARCHAR2(31);
    massa NUMBER;
    x NUMBER;
    y NUMBER;
    z NUMBER;
BEGIN
    p_userid := 'Testes abaixo';
    id_estrela := 'Testes abaixo';
    nome := 'Testes abaixo';
    classificacao := 'Testes abaixo';
    massa := 'Testes abaixo';
    x := 'Testes abaixo';
    y := 'Testes abaixo';
    z := 'Testes abaixo';
    FUNCCIENTISTA_INSEREESTRELA(p_userid, id_estrela, nome, classificacao, massa, x, y, z);
END;
/*
Teste sucesso:
p_userid := '2';
id_estrela := 'IDExemplo1';
nome := 'NomeExemplo1';
classificacao := 'ClassExemplo1';
massa := '31278';
x := '2';
y := '2';
z := '2';

Teste erro (ID ou coordenada da estrela ja existe.):
p_userid := '2';
id_estrela := 'IDExemplo1';
nome := 'NomeExemplo1';
classificacao := 'ClassExemplo1';
massa := '31278';
x := '1';
y := '1';
z := '1';

Teste erro (A massa deve ser maior ou igual a 0.):
p_userid := '2';
id_estrela := 'IDExemplo2';
nome := 'NomeExemplo2';
classificacao := 'ClassExemplo2';
massa := '-20';
x := '3';
y := '4';
z := '5';
*/


/*
FUNCCIENTISTA_ATUALIZAESTRELA
*/
DECLARE
    p_Userid NUMBER;
    id_estrela_antigo VARCHAR2(31);
    id_estrela_novo VARCHAR2(31);
    nome_estrela VARCHAR2(31);
    classificacao_estrela VARCHAR2(31);
    massa_estrela NUMBER;
    x_estrela NUMBER;
    y_estrela NUMBER;
    z_estrela NUMBER;
BEGIN
    p_userid := 'Testes abaixo';
    id_estrela_antigo := 'Testes abaixo';
    id_estrela_novo := 'Testes abaixo';
    nome_estrela := 'Testes abaixo';
    classificacao_estrela := 'Testes abaixo';
    massa_estrela := 'Testes abaixo';
    x_estrela := 'Testes abaixo';
    y_estrela := 'Testes abaixo';
    z_estrela := 'Testes abaixo';
    FUNCCIENTISTA_ATUALIZASTRELA(p_userid, id_estrela_antigo, id_estrela_novo, nome_estrela, classificacao_estrela, massa_estrela, x_estrela, y_estrela, z_estrela);
END;
/*
Teste sucesso:
p_userid := '2';
id_estrela_antigo := 'IDExemplo';
id_estrela_novo := 'IDExemploX';
nome_estrela := 'NomeExemplo1';
classificacao_estrela := 'ClassExemplo1';
massa_estrela := '20';
x_estrela := '1';
y_estrela := '1';
z_estrela := '1';

Teste erro (A estrela nao foi encontrada.):
p_userid := '2';
id_estrela_antigo := 'EstreNaoExiste';
id_estrela_novo := 'IDExemploX';
nome_estrela := 'NomeExemplo1';
classificacao_estrela := 'ClassExemplo1';
massa_estrela := '20';
x_estrela := '1';
y_estrela := '1';
z_estrela := '1';

Teste erro (ID ou coordenada da estrela ja existente.):
p_userid := '2';
id_estrela_antigo := 'IDExemplo';
id_estrela_novo := 'IDExemplo1';
nome_estrela := 'NomeExemplo1';
classificacao_estrela := 'ClassExemplo1';
massa_estrela := '20';
x_estrela := '1';
y_estrela := '1';
z_estrela := '1';

Teste erro (A massa deve ser maior ou igual a 0.):
p_userid := '2';
id_estrela_antigo := 'IDExemplo';
id_estrela_novo := 'IDExemploX';
nome_estrela := 'NomeExemplo1';
classificacao_estrela := 'ClassExemplo1';
massa_estrela := '-20';
x_estrela := '1';
y_estrela := '1';
z_estrela := '1';
*/


/*
FUNCCIENTISTA_REMOVEESTRELA
*/
DECLARE
    p_Userid NUMBER;
    id_estrela VARCHAR2(31);
BEGIN
    p_userid := 'Testes abaixo';
    id_estrela := 'Testes abaixo';
    FUNCCIENTISTA_REMOVEESTRELA(p_userid, id_estrela);
END;
/*
Teste sucesso:
p_userid := '2';
id_estrela := 'IDExemplo';

Teste erro (A estrela nao foi encontrada.):
p_userid := '2';
id_estrela := 'IDExemplo90';