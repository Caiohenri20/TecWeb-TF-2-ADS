use db_faculdade;

CREATE TABLE App_Professor (
  id INT NOT NULL AUTO_INCREMENT,
  ra_professor VARCHAR(10) NOT NULL UNIQUE,
  apelido_professor VARCHAR(30) NOT NULL,
  nome_professor VARCHAR(120) NOT NULL,
  email_professor VARCHAR(80) NOT NULL,
  celular_professor VARCHAR(11) NOT NULL,
  PRIMARY KEY(id)
)

CREATE TABLE App_Curso (
  id INT NOT NULL AUTO_INCREMENT,
  nome_curso VARCHAR(50) NOT NULL UNIQUE,
  sigla_curso VARCHAR(5) NOT NULL UNIQUE,
  PRIMARY KEY(id)
)

CREATE TABLE App_Grade (
  id INT NOT NULL AUTO_INCREMENT,
  sigla_curso VARCHAR(5) NOT NULL UNIQUE,
  ano_grade VARCHAR(4) NOT NULL,
  semestre_grade VARCHAR(1) NOT NULL UNIQUE,
  PRIMARY KEY(id),
  FOREIGN KEY(sigla_curso)
    REFERENCES App_Curso(sigla_curso)
)

CREATE TABLE App_Aluno (
  id INT NOT NULL AUTO_INCREMENT,
  ra_aluno VARCHAR(10) NOT NULL UNIQUE,
  nome_aluno VARCHAR(100) NOT NULL,
  email_aluno VARCHAR(50) NOT NULL,
  celular_aluno VARCHAR(15) NOT NULL,
  sigla_curso VARCHAR(5) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(sigla_curso)
    REFERENCES App_Curso(sigla_curso)
)

CREATE TABLE App_Cursturma (
  id INT NOT NULL AUTO_INCREMENT,
  sigla_curso VARCHAR(5) NOT NULL UNIQUE,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(sigla_curso)
    REFERENCES App_Curso(sigla_curso)
)

CREATE TABLE App_Turma (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  turno_turma VARCHAR(15) NOT NULL,
  ra_professor VARCHAR(10) NOT NULL UNIQUE,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Cursturma(nome_disciplina),
  FOREIGN KEY(ra_professor)
    REFERENCES App_Professor(ra_professor)
)

CREATE TABLE App_Matricula (
  id INT NOT NULL AUTO_INCREMENT,
  ra_aluno VARCHAR(5) NOT NULL,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Cursturma(nome_disciplina)
)

CREATE TABLE App_Periodo (
  id INT NOT NULL AUTO_INCREMENT,
  sigla_curso VARCHAR(5) NOT NULL,
  ano_grade VARCHAR(5) NOT NULL,
  semestre_grade VARCHAR(5) NOT NULL UNIQUE,
  numero_periodo VARCHAR(5) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(semestre_grade)
    REFERENCES App_Grade(semestre_grade)
)

CREATE TABLE App_Disciplina (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  carga_horaria_disciplina VARCHAR(100) NOT NULL,
  teoria_disciplina VARCHAR(100) NOT NULL,
  pratica_disciplina VARCHAR(100) NOT NULL,
  ementa_disciplina VARCHAR(50) NOT NULL,
  competencias_disciplina VARCHAR(50) NULL,
  habilidades_disciplina VARCHAR(50) NULL,
  conteudo_disciplina VARCHAR(50) NULL,
  bibliografia_disciplina VARCHAR(50) NULL,
  bibliografia_complementar_disciplina VARCHAR(50) NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Turma(nome_disciplina)
)

CREATE TABLE App_Disciplinofertada (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(240) NOT NULL,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Turma(nome_disciplina)
)

CREATE TABLE App_Perioddisciplina (
  id INT NOT NULL AUTO_INCREMENT,
  sigla_curso VARCHAR(5) NOT NULL,
  ano_grade VARCHAR(5) NOT NULL,
  semestre_grade VARCHAR(5) NOT NULL,
  numero_periodo VARCHAR(5) NOT NULL UNIQUE,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Disciplina(nome_disciplina)
)

CREATE TABLE App_Questao (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(10) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  numero_questao VARCHAR(5) NOT NULL,
  datalimiteentrega_questao VARCHAR(15) NOT NULL,
  descricao_questao INTEGER UNSIGNED NOT NULL,
  data_questao DATE NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Disciplina(nome_disciplina)
)

CREATE TABLE App_Resposta (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  numero_questao VARCHAR(5) NOT NULL,
  ra_aluno VARCHAR(5) NOT NULL,
  dataavaliacao_resposta VARCHAR(15) NOT NULL,
  nota_resposta VARCHAR(5) NOT NULL,
  avaliacao_resposta VARCHAR(100) NOT NULL,
  descricao_resposta VARCHAR(100) NOT NULL,
  datadeenvio_resposta VARCHAR(15) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Disciplina(nome_disciplina)
)

CREATE TABLE App_Arquivresposta (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(5) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  numero_questao VARCHAR(5) NOT NULL,
  ra_aluno VARCHAR(5) NOT NULL,
  aquivo_resposta VARCHAR(500) NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Resposta(nome_disciplina)
)
*/

CREATE TABLE App_Arquivquestao (
  id INT NOT NULL AUTO_INCREMENT,
  nome_disciplina VARCHAR(240) NOT NULL UNIQUE,
  ano_disciplina VARCHAR(5) NOT NULL,
  semestre_disciplina VARCHAR(5) NOT NULL,
  id_turma VARCHAR(5) NOT NULL,
  numero_questao VARCHAR(5) NOT NULL,
  arquivo_questao VARCHAR(5) NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(nome_disciplina)
    REFERENCES App_Questao(nome_disciplina)
)





