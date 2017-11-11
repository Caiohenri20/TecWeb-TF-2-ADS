BEGIN;
CREATE TABLE `app_contato_professor` (
	`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	`professor` varchar(200) NOT NULL,
        `disciplina` varchar(200) NOT NULL, 
        `aviso` varchar(400) NOT NULL);
COMMIT;