BEGIN;
CREATE TABLE `app_contato_professor` (
	`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	`professor` varchar(200) NOT NULL,
        `disciplina` varchar(200) NOT NULL, 
        `aviso` varchar(400) NOT NULL);
COMMIT;

BEGIN;
CREATE TABLE `app_cadastro_professor` (
	    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	    `RA` varchar(200) NOT NULL,
        `senha` varchar(200) NOT NULL, 
        `nome` varchar(200) NOT NULL),
        `endereco` varchar(200) NOT NULL, 
        `telefone` varchar(200) NOT NULL, 
        `email` varchar(200) NOT NULL
        );
COMMIT;