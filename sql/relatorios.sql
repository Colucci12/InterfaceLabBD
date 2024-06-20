--:: CRIACAO DAS VIEWS DE RELATORIOS) //////////////////////////////////////////////////////////////////////////////////

/*
Criacao da view para o relatorio de um lider da faccao.
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_LIDERFACCAO AS
SELECT
    f.LIDER AS faccao_lider,
    f.NOME AS faccao_nome,
    c.NOME AS comunidade_nome,
    c.QTD_HABITANTES,
    n.NOME AS nacao,
    e.NOME AS especie,
    p.ID_ASTRO AS planeta,
    p.CLASSIFICACAO AS planeta_classificacao,
    s.NOME AS sistema
FROM
    FACCAO f
    JOIN PARTICIPA pa ON f.NOME = pa.FACCAO
    JOIN COMUNIDADE c ON pa.ESPECIE = c.ESPECIE AND pa.COMUNIDADE = c.NOME
    JOIN ESPECIE e ON c.ESPECIE = e.NOME
    LEFT JOIN HABITACAO h ON c.ESPECIE = h.ESPECIE AND c.NOME = h.COMUNIDADE
    LEFT JOIN PLANETA p ON h.PLANETA = p.ID_ASTRO
    LEFT JOIN DOMINANCIA d ON p.ID_ASTRO = d.PLANETA
    LEFT JOIN NACAO n ON d.NACAO = n.NOME
    LEFT JOIN ORBITA_PLANETA op ON p.ID_ASTRO = op.PLANETA
    LEFT JOIN ESTRELA es ON op.ESTRELA = es.ID_ESTRELA
    LEFT JOIN SISTEMA s ON es.ID_ESTRELA = s.ESTRELA
    WHERE h.DATA_FIM IS NULL;


/*
Criacao da view para o relatorio de um oficial.
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_OFICIAL AS
SELECT
    h.planeta AS planeta,
    c.especie AS especie,
    c.nome AS comunidade_nome,
    c.qtd_habitantes,
    h.data_ini,
    h.data_fim,
    n.nome AS nacao_nome,
    nf.faccao AS faccao,
    s.nome AS sistema
FROM
    habitacao h
    JOIN comunidade c ON h.especie = c.especie AND h.comunidade = c.nome
    JOIN especie e ON c.especie = e.nome
    JOIN planeta p ON h.planeta = p.id_astro
    LEFT JOIN orbita_planeta op ON p.id_astro = op.planeta
    LEFT JOIN estrela est ON op.estrela = est.id_estrela
    LEFT JOIN sistema s ON est.id_estrela = s.estrela
    JOIN dominancia d ON h.planeta = d.planeta
    JOIN nacao n ON n.nome = d.nacao
    LEFT JOIN nacao_faccao nf ON nf.nacao = n.nome;


/*
Criacao da view para o relatorio de um comandante (planetas dominados).
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_COMANDANTE_PLANETASDOMINADOS AS
SELECT 
    d.PLANETA,
    d.NACAO AS NacaoDominante,
    d.DATA_INI AS DataInicioDominancia,
    d.DATA_FIM AS DataFimDominancia,
    (SELECT COUNT(*) FROM HABITACAO h WHERE h.PLANETA = d.PLANETA) AS QuantidadeComunidades,
    (SELECT COUNT(DISTINCT h.ESPECIE) FROM HABITACAO h WHERE h.PLANETA = d.PLANETA) AS QuantidadeEspecies,
    (SELECT SUM(c.QTD_HABITANTES) FROM HABITACAO h JOIN COMUNIDADE c ON h.ESPECIE = c.ESPECIE AND h.COMUNIDADE = c.NOME WHERE h.PLANETA = d.PLANETA) AS QuantidadeHabitantes,
    (SELECT COUNT(DISTINCT p.FACCAO) FROM HABITACAO h JOIN PARTICIPA p ON h.ESPECIE = p.ESPECIE AND h.COMUNIDADE = p.COMUNIDADE WHERE h.PLANETA = d.PLANETA) AS QuantidadeFaccoes,
    (SELECT p.FACCAO FROM HABITACAO h JOIN PARTICIPA p ON h.ESPECIE = p.ESPECIE AND h.COMUNIDADE = p.COMUNIDADE WHERE h.PLANETA = d.PLANETA GROUP BY p.FACCAO ORDER BY COUNT(*) DESC FETCH FIRST ROW ONLY) AS FaccaoMajoritaria
FROM DOMINANCIA d;


/*
Criacao da view para o relatorio de um comandante (planetas em potencial dominacao).
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO AS
SELECT 
    p.ID_ASTRO AS Planeta,
    s.NOME AS Sistema
FROM
    PLANETA p
    LEFT JOIN DOMINANCIA d ON p.ID_ASTRO = d.PLANETA AND (d.DATA_FIM IS NULL OR d.DATA_FIM > SYSDATE)
    JOIN ORBITA_PLANETA op ON p.ID_ASTRO = op.PLANETA
    JOIN SISTEMA s ON op.ESTRELA = s.ESTRELA
    WHERE d.PLANETA IS NULL;


/*
Criacao da view para o relatorio de um cientista (dados de estrelas).
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_CIENTISTA_ESTRELAS AS
SELECT id_estrela, nome, classificacao, massa, x, y, z
FROM ESTRELA;


/*
Criacao da view para o relatorio de um cientista (dados de planetas).
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_CIENTISTA_PLANETAS AS
SELECT id_astro, massa, raio, classificacao
FROM PLANETA;


/*
Criacao da view para o relatorio de um cientista (dados de planetas).
*/
CREATE OR REPLACE VIEW VIEW_RELATORIO_CIENTISTA_SISTEMAS AS
SELECT estrela, nome
FROM SISTEMA;





--:: CRIACAO DO PACKAGE COM OS RELATORIOS) //////////////////////////////////////////////////////////////////////////////////

/*
Estrutura do package
*/
CREATE OR REPLACE PACKAGE PACKAGE_RELATORIOS AS
    PROCEDURE PROCED_RELATORIO_LIDERFACCAO (p_userid IN USERS.USERID%TYPE, p_agrupamento IN VARCHAR2, p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_OFICIAL (p_userid IN USERS.USERID%TYPE, p_agrupamento IN VARCHAR2, p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_COMANDANTE_PLANETASDOMINADOS (p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO (p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_CIENTISTA_ESTRELAS (p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_CIENTISTA_PLANETAS (p_cursor OUT SYS_REFCURSOR);
    PROCEDURE PROCED_RELATORIO_CIENTISTA_SISTEMAS (p_cursor OUT SYS_REFCURSOR);
END PACKAGE_RELATORIOS;

/
/*
Corpo do package
*/
CREATE OR REPLACE PACKAGE BODY PACKAGE_RELATORIOS AS


    /*
    Procedimento para retornar relatorio de acordo com
    faccao do lider e atributo selecionado para agrupamento.
    */ 
    PROCEDURE PROCED_RELATORIO_LIDERFACCAO (
        p_userid IN USERS.USERID%TYPE,
        p_agrupamento IN VARCHAR2,
        p_cursor OUT SYS_REFCURSOR
    ) IS
        v_cpi LIDER.CPI%TYPE;
    BEGIN

        -- Seleciona qual o CPI do lider
        SELECT IDLIDER INTO v_cpi FROM USERS WHERE USERID = p_userid;

        -- Faz a busca de acordo com a faccao do lider
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_LIDERFACCAO
            WHERE faccao_lider = v_cpi
            ORDER BY p_agrupamento;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');
        
    END PROCED_RELATORIO_LIDERFACCAO;


    /*
    Procedimento para retornar relatorio de acordo com
    nacao do oficial e atributo selecionado para agrupamento.
    */ 
    PROCEDURE PROCED_RELATORIO_OFICIAL (
        p_userid IN USERS.USERID%TYPE,
        p_agrupamento IN VARCHAR2,
        p_cursor OUT SYS_REFCURSOR
    ) IS
        v_nacao NACAO.NOME%TYPE;
    BEGIN

        -- Seleciona qual a nacao do lider
        SELECT l.NACAO INTO v_nacao 
        FROM LIDER l
        JOIN USERS u ON u.IDLIDER = l.CPI
        WHERE u.USERID = p_userid;

        -- Faz a busca de acordo com a nacao do lider
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_OFICIAL
            WHERE nacao_nome = v_nacao
            ORDER BY p_agrupamento;
    
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');

    END PROCED_RELATORIO_OFICIAL;


    /*
    Procedimento para retornar relatorio de
    planetas dominados para o comandante
    */
    PROCEDURE PROCED_RELATORIO_COMANDANTE_PLANETASDOMINADOS (
        p_cursor OUT SYS_REFCURSOR
    ) IS

    BEGIN
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_COMANDANTE_PLANETASDOMINADOS;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');

    END PROCED_RELATORIO_COMANDANTE_PLANETASDOMINADOS;


    /*
    Procedimento para retornar relatorio de
    planetas em potencial dominacao para o comandante
    */
    PROCEDURE PROCED_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO (
        p_cursor OUT SYS_REFCURSOR
    ) IS

    BEGIN
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');

    END PROCED_RELATORIO_COMANDANTE_PLANETASPOTENCIALDOMINACAO;


    /*
    Procedimento para retornar
    relatorio de estrelas para cientista
    */
    PROCEDURE PROCED_RELATORIO_CIENTISTA_ESTRELAS (
        p_cursor OUT SYS_REFCURSOR
    ) IS

    BEGIN
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_CIENTISTA_ESTRELAS;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');

    END PROCED_RELATORIO_CIENTISTA_ESTRELAS;


    /*
    Procedimento para retornar
    relatorio de planetas para cientista
    */
    PROCEDURE PROCED_RELATORIO_CIENTISTA_PLANETAS (
        p_cursor OUT SYS_REFCURSOR
    ) IS

    BEGIN
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_CIENTISTA_PLANETAS;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');

    END PROCED_RELATORIO_CIENTISTA_PLANETAS;


    /*
    Procedimento para retornar
    relatorio de sistemas para cientista
    */
    PROCEDURE PROCED_RELATORIO_CIENTISTA_SISTEMAS (
        p_cursor OUT SYS_REFCURSOR
    ) IS

    BEGIN
        OPEN p_cursor FOR
            SELECT * FROM VIEW_RELATORIO_CIENTISTA_SISTEMAS;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Nao foi encontrado nenhum dado.');
            
    END PROCED_RELATORIO_CIENTISTA_SISTEMAS;


END PACKAGE_RELATORIOS;