CREATE USER 'hcsUser'@'localhost' IDENTIFIED BY 'urubu100';
GRANT ALL PRIVILEGES ON hcs.* TO 'hcsUser'@'localhost';

CREATE DATABASE hcs;
USE hcs;

CREATE TABLE Empresa (
	idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
	nomeEmpresa VARCHAR (64) NOT NULL,
	cnpj varchar(14) NOT NULL UNIQUE,
	nomeRepresentante VARCHAR(45) NOT NULL,
	senha VARCHAR(256) NOT NULL
) AUTO_INCREMENT = 5000;

CREATE TABLE Funcionario (
	idFuncionario INT PRIMARY KEY AUTO_INCREMENT,
    nomeFuncionario VARCHAR(64) NOT NULL,
    senha VARCHAR(256) NOT NULL,
    fkEmpresa INT,
    FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
);

CREATE TABLE Cliente (
	idCliente INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(64) NOT NULL,
	senha VARCHAR(12) NOT NULL
) AUTO_INCREMENT=15000;

CREATE TABLE Carro (
	enderecoMac VARCHAR(23) PRIMARY KEY,
	placaCarro CHAR(7) NOT NULL UNIQUE,
	modelo VARCHAR(64) NOT NULL,
	
    processador VARCHAR(45) NOT NULL,
    qtdNucleos INT NOT NULL,
    qtdNucleosLogicos INT NOT NULL,
    maxFrequencia INT NOT NULL,
    qtdMemoriaRAM INT NOT NULL,
    qtdMemoriaInterna INT NOT NULL,
    sistemaOperacional VARCHAR(45) NOT NULL,
    enderecoIP VARCHAR(32) NOT NULL,
    mascara VARCHAR(32) NOT NULL,
    horarioReg DATETIME NOT NULL,
    
	fkCliente INT,
	FOREIGN KEY (fkCliente) REFERENCES Cliente(idCliente),
    
	fkEmpresa INT,
    FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
) AUTO_INCREMENT=10000;

CREATE TABLE medidas (
	idMedida INT PRIMARY KEY AUTO_INCREMENT,
    usoProcessador INT NOT NULL,
    usoMemoriaRAM INT NOT NULL,
    usoMemoriaInt INT NOT NULL,
    qtdDadosRec INT NOT NULL,
    qtdDadosEnv INT NOT NULL,
    qtdPacotesEnv INT NOT NULL,
    qtdPacotesRec INT NOT NULL,
    qtdBateria INT,
    estaConectado BOOL,
    horario DATETIME,
    
    fkCarro VARCHAR(23),
    FOREIGN KEY (fkCarro) REFERENCES Carro (enderecoMac)
) AUTO_INCREMENT = 100000;

INSERT INTO Empresa VALUES (NULL, 'Tesla', '123456789', 'Marise', 'urubu100');
INSERT INTO Cliente VALUES (NULL, 'Maria', '123456');

SELECT * FROM Empresa;
SELECT * FROM Cliente;

SELECT * FROM Carro JOIN Cliente WHERE fkCliente = idCliente;

SELECT * FROM Carro;

SELECT * FROM medidas;

SELECT * FROM Carro join Empresa on Carro.fkEmpresa = Empresa.idEmpresa;

DROP TABLE medidas;
DROP DATABASE hcs;