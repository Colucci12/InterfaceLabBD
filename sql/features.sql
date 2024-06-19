--:: CRIACAO DOS INDICES) //////////////////////////////////////////////////////////////////////////////////

/*
A fim de melhorar as consultas do projeto, principalmente as contidas nos relatorios,
visto que sao querys complexas e demoradas, segue abaixo a criacao de alguns indices:
*/

CREATE INDEX idx_participa_faccao ON PARTICIPA(FACCAO);
CREATE INDEX idx_habitacao_planeta_especie_comunidade ON HABITACAO(PLANETA, ESPECIE, COMUNIDADE);
CREATE INDEX idx_dominancia_planeta_nacao ON DOMINANCIA(PLANETA, NACAO);
CREATE INDEX idx_orbita_planeta ON ORBITA_PLANETA(PLANETA);