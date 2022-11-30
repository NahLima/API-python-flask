CREATE TABLE `Departments` (
  `id` int,
  `name` varchar(30),
  PRIMARY KEY (`id`, `name`)
);

CREATE TABLE `Employees` (
  `id` int,
  `department_id` int,
  `name` varchar(140) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `Dependents` (
  `id` int,
  `responsible_id` int,
  `name` varchar(140) NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `Employees` ADD FOREIGN KEY (`department_id`) REFERENCES `Departments` (`id`);

ALTER TABLE `Dependents` ADD FOREIGN KEY (`responsible_id`) REFERENCES `Employees` (`id`);


INSERT INTO Departments (id, name) VALUES (1,'Engenharia');
INSERT INTO Departments (id, name) VALUES (2, 'Comunicação');
INSERT INTO Departments (id, name) VALUES (3, 'Artes');
INSERT INTO Departments (id, name) VALUES (4, 'RH');

INSERT INTO Employees (id, department_id, name) VALUES (1, 1, 'Roberto Augusto Lins');
INSERT INTO Employees (id, department_id, name) VALUES (2, 1, 'Ana Luiza Peixoto');
INSERT INTO Employees (id, department_id, name) VALUES (3, 2, 'Carlos Silva Lima');
INSERT INTO Employees (id, department_id, name) VALUES (4, 2, 'Amanda Gonsalo Ruiz');
INSERT INTO Employees (id, department_id, name) VALUES (5, 3, 'Natalia Albuquerque Sil');
INSERT INTO Employees (id, department_id, name) VALUES (6, 3, 'Roberta Caulin Lima');
INSERT INTO Employees (id, department_id, name) VALUES (7, 4, 'Reinaldo Tijuca Rio');
INSERT INTO Employees (id, department_id, name) VALUES (8, 4, 'Ana Maria Azevedo');

INSERT INTO Dependents (id, responsible_id, name) VALUES (1, 1, 'Talita Amaral de Jesus');
INSERT INTO Dependents (id, responsible_id, name) VALUES (2, 1, 'Rafael de Freitas Sampaio');
INSERT INTO Dependents (id, responsible_id, name) VALUES (3, 2, 'Naiara Santos de Lima');
INSERT INTO Dependents (id, responsible_id, name) VALUES (4, 3, 'Jaqueline Amal de Souza');
INSERT INTO Dependents (id, responsible_id, name) VALUES (5, 3, 'Thais Sampaio Juviel');
INSERT INTO Dependents (id, responsible_id, name) VALUES (6, 3, 'Fabricio de Amaral Rezende');
INSERT INTO Dependents (id, responsible_id, name) VALUES (7, 4, 'Lucimara Antonieta');
INSERT INTO Dependents (id, responsible_id, name) VALUES (8, 5, 'Renata de Jesus');
INSERT INTO Dependents (id, responsible_id, name) VALUES (9, 6, 'Carolina Amaral de Freitas');
INSERT INTO Dependents (id, responsible_id, name) VALUES (10, 7, 'Renato Rael de Lins');
INSERT INTO Dependents (id, name) VALUES (11, 'Sonia Maria Ciavatta');
INSERT INTO Dependents (id, name) VALUES (12, 'Valdomiro Amaral de Freitas');
INSERT INTO Dependents (id, name) VALUES (13, 'Amora Lima de Além');

