--:: CRIACAO DO PACKAGE COM AS FUNCIONALIDADES) //////////////////////////////////////////////////////////////////////////////////

/*
Estrutura do package
*/
CREATE OR REPLACE PACKAGE PACKAGE_FUNCIONALIDADES AS
    PROCEDURE FUNCLIDER_ALTERARNOMEFACCAO(p_Userid NUMBER,p_NovoNome VARCHAR2);
    PROCEDURE FUNCLIDER_INDICARNOVOLIDER(p_Userid NUMBER,p_NovoLider CHAR);
    PROCEDURE FUNCLIDER_CREDENCIARCOMUNIDADE(p_Userid NUMBER,p_Faccao VARCHAR2,p_Especie VARCHAR2,p_Comunidade VARCHAR2,p_Planeta VARCHAR2);
    PROCEDURE FUNCLIDER_REMOVERFACCAONACAO(p_Userid NUMBER,p_Nacao VARCHAR2);
    PROCEDURE FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO(p_Userid NUMBER,p_Federacao VARCHAR2);
    PROCEDURE FUNCCOMANDANTE_EXCLUIRNACAOFEDERACAO(p_Userid NUMBER);
    PROCEDURE FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO (p_Userid NUMBER,federacao IN federacao.nome%TYPE);
    PROCEDURE FUNCCOMANDANTE_INSERIRDOMINANCIA(p_Userid NUMBER,p_Planeta VARCHAR2);
    PROCEDURE FUNCCIENTISTA_INSEREESTRELA (p_Userid NUMBER,id_estrela IN estrela.id_estrela%TYPE,nome IN estrela.nome%TYPE,classificacao IN estrela.classificacao%TYPE,massa IN estrela.massa%TYPE,x IN estrela.x%TYPE,y IN estrela.y%TYPE,z IN estrela.z%TYPE);
    PROCEDURE FUNCCIENTISTA_ATUALIZAESTRELA (p_Userid NUMBER,id_estrela_antigo IN estrela.id_estrela%TYPE,id_estrela_novo IN estrela.id_estrela%TYPE,nome_estrela IN estrela.nome%TYPE,classificacao_estrela IN estrela.classificacao%TYPE,massa_estrela IN estrela.massa%TYPE,x_estrela IN estrela.x%TYPE,y_estrela IN estrela.y%TYPE,z_estrela IN estrela.z%TYPE);
    PROCEDURE FUNCCIENTISTA_REMOVEESTRELA (p_Userid NUMBER,id IN estrela.id_estrela%TYPE);
END PACKAGE_FUNCIONALIDADES;

/
/*
Corpo do package
*/
CREATE OR REPLACE PACKAGE BODY PACKAGE_FUNCIONALIDADES AS

    --:: FUNCIONALIDADES LIDER FACCAO) //////////////////////////////////////////////////////

    /*
    Funcionalidade do lider:
    Gerenciar aspectos da faccao: Alterar nome da faccao
    */ 
    PROCEDURE FUNCLIDER_ALTERARNOMEFACCAO(
        p_Userid NUMBER,
        p_NovoNome VARCHAR2
    ) IS
        v_CPI CHAR(14);
        v_Faccao VARCHAR2(15);
    BEGIN

        -- Verificar se o usuário é um líder de facção
        SELECT l.CPI, f.NOME
        INTO v_CPI, v_Faccao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        JOIN FACCAO f ON f.LIDER = l.CPI
        WHERE u.Userid = p_Userid;
        
        -- Alterar o nome da facção
        UPDATE FACCAO
        SET NOME = p_NovoNome
        WHERE LIDER = v_CPI;
        
        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Nome da facção alterado para: ' || p_NovoNome);

        -- Commit da operacao
        COMMIT;
        
        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Nome da facção alterado para: ' || p_NovoNome);

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Usuário não é líder de facção ou usuário inválido.');
        WHEN DUP_VAL_ON_INDEX THEN
            RAISE_APPLICATION_ERROR(-20002, 'Já existe uma facção com o nome fornecido.');
        WHEN OTHERS THEN
            IF SQLCODE = -2292 THEN
                RAISE_APPLICATION_ERROR(-20003, 'Não é possível alterar o nome porque a facção possui registros filhos.');
            ELSE
                RAISE_APPLICATION_ERROR(-20004, 'Erro ao alterar o nome da facção: ' || SQLERRM);
            END IF;
    END FUNCLIDER_ALTERARNOMEFACCAO;


    /*
    Funcionalidade do lider:
    Gerenciar aspectos da faccao: Indicar novo lider
    */ 
    PROCEDURE FUNCLIDER_INDICARNOVOLIDER(
        p_Userid NUMBER,
        p_NovoLider CHAR
    ) IS
        v_CPI CHAR(14);
        v_Faccao VARCHAR2(15);
        v_Count INTEGER;
        e_liderjalidera exception;
    BEGIN

        -- Verificar se o usuário atual é um líder de facção
        SELECT l.CPI, f.NOME
        INTO v_CPI, v_Faccao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        JOIN FACCAO f ON f.LIDER = l.CPI
        WHERE u.Userid = p_Userid;

        -- Verificar se o novo líder já lidera uma facção
        SELECT COUNT(*)
        INTO v_Count
        FROM FACCAO
        WHERE LIDER = p_NovoLider;

        IF v_Count > 0 THEN
            RAISE e_liderjalidera;
        END IF;

        -- Atualizar a facção com o novo líder
        UPDATE FACCAO
        SET LIDER = p_NovoLider
        WHERE LIDER = v_CPI;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Novo líder indicado: ' || p_NovoLider || ' para a facção: ' || v_Faccao);

        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Novo líder indicado com sucesso: ' || p_NovoLider);

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20005, 'Usuário não é líder de facção ou novo lider nao encontrado.');
        WHEN e_liderjalidera THEN
            RAISE_APPLICATION_ERROR(-20006, 'O novo lider indicado ja lidera uma faccao.');
        WHEN OTHERS THEN
            IF SQLCODE = -02291 THEN
                RAISE_APPLICATION_ERROR(-20007, 'Usuário não é líder de facção ou novo lider nao encontrado.');
            ELSE
                RAISE_APPLICATION_ERROR(-20008, 'Erro ao indicar o novo líder: ' || SQLERRM);
            END IF;

    END FUNCLIDER_INDICARNOVOLIDER;


    /*
    Funcionalidade do lider:
    Gerenciar aspectos da faccao: Credenciar comunidades
    */ 
    PROCEDURE FUNCLIDER_CREDENCIARCOMUNIDADE(
        p_Userid NUMBER,
        p_Faccao VARCHAR2,
        p_Especie VARCHAR2,
        p_Comunidade VARCHAR2,
        p_Planeta VARCHAR2
    ) IS
        v_CPI CHAR(14);
        v_Nacao VARCHAR2(15);
        v_Count INTEGER;
        e_faccaonaopresente exception;
    BEGIN

        -- Verificar se o usuário é um líder de facção
        SELECT l.CPI
        INTO v_CPI
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        JOIN FACCAO f ON f.LIDER = l.CPI
        WHERE u.Userid = p_Userid
        AND f.NOME = p_Faccao;

        -- Verificar se a facção está presente em nações que dominam o planeta
        SELECT COUNT(*)
        INTO v_Count
        FROM DOMINANCIA d
        JOIN NACAO_FACCAO nf ON d.NACAO = nf.NACAO
        WHERE d.PLANETA = p_Planeta
        AND nf.FACCAO = p_Faccao
        AND (d.DATA_FIM IS NULL OR d.DATA_FIM > SYSDATE);

        IF v_Count = 0 THEN
            RAISE e_faccaonaopresente;
        END IF;

        -- Inserir o registro na tabela PARTICIPA
        INSERT INTO PARTICIPA (FACCAO, ESPECIE, COMUNIDADE)
        VALUES (p_Faccao, p_Especie, p_Comunidade);

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Comunidade ' || p_Comunidade || ' credenciada na facção: ' || p_Faccao);

        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Comunidade credenciada com sucesso: ' || p_Comunidade);

    EXCEPTION
        WHEN DUP_VAL_ON_INDEX THEN
            RAISE_APPLICATION_ERROR(-20009, 'Esse credenciamento ja existe.');
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20010, 'Os dados passados como parametros nao foram encontrados.');
        WHEN e_faccaonaopresente THEN
            RAISE_APPLICATION_ERROR(-20011, 'A facção não está presente em nações que dominam o planeta especificado.');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20012, 'Erro ao credenciar comunidade: ' || SQLERRM);

    END FUNCLIDER_CREDENCIARCOMUNIDADE;


    /*
    Funcionalidade do lider:
    Remover faccao de nacao
    */ 
    PROCEDURE FUNCLIDER_REMOVERFACCAONACAO(
        p_Userid NUMBER,
        p_Nacao VARCHAR2
    ) IS
        v_CPI CHAR(14);
        v_faccao VARCHAR2(15);
    BEGIN
    
        -- Verificar se o usuário é um líder de facção
        SELECT l.CPI, f.NOME
        INTO v_CPI, v_Faccao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        JOIN FACCAO f ON f.LIDER = l.CPI
        WHERE u.Userid = p_Userid;
    
        -- Remover a facção da nação na tabela NACAO_FACCAO
        DELETE FROM NACAO_FACCAO
        WHERE NACAO = p_Nacao
        AND FACCAO = v_faccao;
    
        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Facção ' || v_faccao || ' removida da nação: ' || p_Nacao);
    
        -- Commit da operacao
        COMMIT;
    
        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Facção removida com sucesso da nação: ' || p_Nacao);
    
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20013, 'Os dados passados como parametros nao foram encontrados.');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20014, 'Erro ao remover a facção da nação: ' || SQLERRM);
    
    END FUNCLIDER_REMOVERFACCAONACAO;




    --:: FUNCIONALIDADES COMANDANTE) //////////////////////////////////////////////////////

    /*
    Funcionalidade do comandante:
    Alterar aspectos: Incluir propria nacao em federacao existente
    */
    PROCEDURE FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO(
        p_Userid NUMBER,
        p_Federacao VARCHAR2
    ) IS
        v_Nacao VARCHAR2(15);
        v_FedCount INTEGER;
        e_federacaonaoencontrada exception; 
    BEGIN
        -- Verificar se a federação existe
        SELECT COUNT(*)
        INTO v_FedCount
        FROM FEDERACAO
        WHERE NOME = p_Federacao;

        IF v_FedCount = 0 THEN
            RAISE e_federacaonaoencontrada;
        END IF;

        -- Verificar se o usuário é um comandante
        SELECT l.NACAO
        INTO v_Nacao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        WHERE u.Userid = p_Userid
        AND l.CARGO = 'COMANDANTE';

        -- Atualizar a nação para incluir na federação
        UPDATE NACAO
        SET FEDERACAO = p_Federacao
        WHERE NOME = v_Nacao;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Nação ' || v_Nacao || ' incluída na federação: ' || p_Federacao);

        -- Commit da operação
        COMMIT;

        -- Printa para o usuário
        DBMS_OUTPUT.PUT_LINE('Nação incluída com sucesso na federação: ' || p_Federacao);

    EXCEPTION
        WHEN e_federacaonaoencontrada THEN
            RAISE_APPLICATION_ERROR(-20025, 'Federação não encontrada.');
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20026, 'Usuário não é comandante ou nação não encontrada.');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20027, 'Erro ao incluir nação na federação: ' || SQLERRM);

    END FUNCCOMANDANTE_INCLUIRNACAOFEDERACAO;


    /*
    Funcionalidade do comandante:
    Alterar aspectos: Excluir propria nacao de federacao
    */ 
    PROCEDURE FUNCCOMANDANTE_EXCLUIRNACAOFEDERACAO(
        p_Userid NUMBER
    ) IS
        v_Nacao VARCHAR2(15);
    BEGIN

        -- Verificar se o usuário é um comandante
        SELECT l.NACAO
        INTO v_Nacao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        WHERE u.Userid = p_Userid
        AND l.CARGO = 'COMANDANTE';

        -- Atualizar a nação para remover da federação
        UPDATE NACAO
        SET FEDERACAO = NULL
        WHERE NOME = v_Nacao;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Nação ' || v_Nacao || ' removida da federação.');

        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Nação removida com sucesso da federação.');

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20028, 'A nação não possui nenhuma federação atrelada.');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20029, 'Erro ao remover nação da federação: ' || SQLERRM);

    END FUNCCOMANDANTE_EXCLUIRNACAOFEDERACAO;


    /*
    Funcionalidade do comandante:
    Alterar aspectos: Criar nova federacao com propria nacao
    */ 
    PROCEDURE FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO (
        p_Userid NUMBER,
        federacao IN federacao.nome%TYPE
    ) IS
        v_nacao VARCHAR2(15);
        e_nacao_nao_encontrada exception;
    BEGIN

        -- Seleciona qual a nacao do lider
        SELECT l.NACAO INTO v_nacao 
        FROM LIDER l
        JOIN USERS u ON u.IDLIDER = l.CPI
        WHERE u.USERID = p_userid;

        -- Insere a federacao com a propria nacao
        INSERT INTO FEDERACAO VALUES (federacao,SYSDATE);
        UPDATE NACAO SET FEDERACAO=federacao WHERE nome=v_nacao;
        IF SQL%NOTFOUND THEN
            RAISE e_nacao_nao_encontrada; 
        END IF;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Foi criada a federacao' || federacao || ' com a nacao' || v_nacao);
        
        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Nação removida com sucesso da federação.');

    EXCEPTION 
        WHEN DUP_VAL_ON_INDEX THEN RAISE_APPLICATION_ERROR(-20030, 'Federacao ja existe.');
        WHEN e_nacao_nao_encontrada THEN RAISE_APPLICATION_ERROR(-20031, 'Nacao nao encontrada.'); 

    END FUNCCOMANDANTE_CRIARFEDERACAOCOMNACAO;


    /*
    Funcionalidade do comandante:
    Inserir nova dominancia em planeta nao dominado
    */ 
    PROCEDURE FUNCCOMANDANTE_INSERIRDOMINANCIA(
        p_Userid NUMBER,
        p_Planeta VARCHAR2
    ) IS
        v_Nacao VARCHAR2(15);
        v_Count INTEGER;
        e_planetadominado exception;
    BEGIN

        -- Verificar se o usuário é um comandante
        SELECT l.NACAO
        INTO v_Nacao
        FROM USERS u
        JOIN LIDER l ON u.IdLider = l.CPI
        WHERE u.Userid = p_Userid
        AND l.CARGO = 'COMANDANTE';

        -- Verificar se o planeta não está sendo dominado por ninguém
        SELECT COUNT(*)
        INTO v_Count
        FROM DOMINANCIA
        WHERE PLANETA = p_Planeta
        AND (DATA_FIM IS NULL OR DATA_FIM > SYSDATE);

        IF v_Count > 0 THEN
            RAISE e_planetadominado;
        END IF;

        -- Inserir a nova dominância na tabela DOMINANCIA
        INSERT INTO DOMINANCIA (NACAO, PLANETA, DATA_INI, DATA_FIM)
        VALUES (v_Nacao, p_Planeta, SYSDATE, NULL);

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'Nova dominância inserida para o planeta: ' || p_Planeta || ' pela nação: ' || v_Nacao);

        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('Nova dominância inserida com sucesso para o planeta: ' || p_Planeta);

    EXCEPTION
        WHEN e_planetadominado THEN
            RAISE_APPLICATION_ERROR(-20032, 'O planeta já está sendo dominado por outra nação.');
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20033, 'Usuário não é comandante.');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20034, 'Erro ao inserir nova dominância: ' || SQLERRM);

    END FUNCCOMANDANTE_INSERIRDOMINANCIA;





    --:: FUNCIONALIDADES CIENTISTA) //////////////////////////////////////////////////////

    /*
    Funcionalidade do cientista:
    CRUD de Estrelas: Inserir uma estrela
    */ 
    PROCEDURE FUNCCIENTISTA_INSEREESTRELA (
        p_Userid NUMBER,
        id_estrela IN estrela.id_estrela%TYPE,
        nome IN estrela.nome%TYPE,
        classificacao IN estrela.classificacao%TYPE,
        massa IN estrela.massa%TYPE,
        x IN estrela.x%TYPE,
        y IN estrela.y%TYPE,
        z IN estrela.z%TYPE
    ) IS
    BEGIN

        -- Insere a estrela
        INSERT INTO ESTRELA VALUES (id_estrela,nome,classificacao,massa,x,y,z);

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'A estrela ' || nome || ' foi criada.');

        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('A estrela ' || nome || ' foi criada.');

    EXCEPTION 
        WHEN DUP_VAL_ON_INDEX THEN RAISE_APPLICATION_ERROR(-20015, 'ID ou coordenada da estrela ja existente.');
        WHEN OTHERS THEN
            IF SQLCODE = -2290 THEN
                RAISE_APPLICATION_ERROR(-20016, 'A massa deve ser maior ou igual a 0.');
            ELSE
                RAISE_APPLICATION_ERROR(-20017, 'Houve um erro.');
            END IF;

    END FUNCCIENTISTA_INSEREESTRELA;


    /*
    Funcionalidade do cientista:
    CRUD de Estrelas: Atualizar uma estrela
    */ 
    PROCEDURE FUNCCIENTISTA_ATUALIZAESTRELA (
        p_Userid NUMBER,
        id_estrela_antigo IN estrela.id_estrela%TYPE,
        id_estrela_novo IN estrela.id_estrela%TYPE,
        nome_estrela IN estrela.nome%TYPE,
        classificacao_estrela IN estrela.classificacao%TYPE,
        massa_estrela IN estrela.massa%TYPE,
        x_estrela IN estrela.x%TYPE,
        y_estrela IN estrela.y%TYPE,
        z_estrela IN estrela.z%TYPE
    ) IS
        e_estrela_nao_encontrada exception;
    BEGIN

        -- Atualiza a estrela
        UPDATE ESTRELA SET
        id_estrela = id_estrela_novo, nome = nome_estrela, classificacao = classificacao_estrela,
        massa = massa_estrela, x = x_estrela, y = y_estrela, z = z_estrela 
        WHERE id_estrela = id_estrela_antigo;
        
        IF SQL%NOTFOUND THEN
            RAISE e_estrela_nao_encontrada; 
        END IF;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'A estrela que possuia o ID ' || id_estrela_antigo || ' foi atualizada.');
        
        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('A estrela que possuia o ID ' || id_estrela_antigo || ' foi atualizada.');

    EXCEPTION 
        WHEN DUP_VAL_ON_INDEX THEN 
            RAISE_APPLICATION_ERROR(-20018, 'ID ou coordenada da estrela ja existente.');
        WHEN e_estrela_nao_encontrada THEN 
            RAISE_APPLICATION_ERROR(-20019, 'A estrela nao foi encontrada.');
        WHEN OTHERS THEN
            IF SQLCODE = -2290 THEN
                RAISE_APPLICATION_ERROR(-20020, 'A massa deve ser maior ou igual a 0.');
            ELSIF SQLCODE = -6512 THEN
                RAISE_APPLICATION_ERROR(-20021, 'Registro filho localizado, nao e possivel alterar.');
            ELSE
                RAISE_APPLICATION_ERROR(-20022, 'Existem registros filhos relacionados, nao e possivel alterar.');
            END IF;

    END FUNCCIENTISTA_ATUALIZAESTRELA;


    /*
    Funcionalidade do cientista:
    CRUD de Estrelas: Remover uma estrela
    */ 
    PROCEDURE FUNCCIENTISTA_REMOVEESTRELA (
        p_Userid NUMBER,
        id IN estrela.id_estrela%TYPE
    ) IS
        e_estrela_nao_encontrada exception;
    BEGIN

        -- Remove a estrela
        DELETE FROM ESTRELA WHERE id_estrela = id;
        IF SQL%NOTFOUND THEN
            RAISE e_estrela_nao_encontrada; 
        END IF;

        -- Registrar a operação na LOG_TABLE usando o procedimento InsertLog
        InsertLog(p_Userid, 'A estrela que possuia o ID ' || id || ' foi removida.');
        
        -- Commit da operacao
        COMMIT;

        -- Printa para o usuario
        DBMS_OUTPUT.PUT_LINE('A estrela que possuia o ID ' || id || ' foi removida.');

    EXCEPTION
        WHEN e_estrela_nao_encontrada THEN RAISE_APPLICATION_ERROR(-20023, 'A estrela nao foi encontrada.');
        WHEN OTHERS THEN RAISE_APPLICATION_ERROR(-20024, 'Um erro foi encontrado.');

    END FUNCCIENTISTA_REMOVEESTRELA;


END PACKAGE_FUNCIONALIDADES;





















