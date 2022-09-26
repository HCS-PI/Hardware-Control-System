CREATE DATABASE HardwareControllSystem;

USE  HardwareControllSystem;

CREATE TABLE Empresa(
idEmpresa INT PRIMARY KEY AUTO_INCREMENT
,nomeEmpresa VARCHAR(40)
,cnpj VARCHAR(18)
);

CREATE TABLE Funcionario(
idFuncionario INT PRIMARY KEY AUTO_INCREMENT
,nomeFuncionario VARCHAR(64)
,cpf CHAR(14)
,email VARCHAR(100)
,senha VARCHAR(256)
,cargo CHAR(3)
,fkEmpresa INT, FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
);

CREATE TABLE Carro(
idCarro INT PRIMARY KEY AUTO_INCREMENT
,enderecoMAC VARCHAR(17)
,placaCarro CHAR(7)
,modelo VARCHAR(64)
,fkEmpresa INT, FOREIGN KEY (fkEmpresa) REFERENCES Empresa(idEmpresa)
);

CREATE TABLE Dispositivo(
idDispositivo INT PRIMARY KEY AUTO_INCREMENT
,tipo VARCHAR(45)
,modelo VARCHAR(45)
,unidMedida VARCHAR(10)
,fkCarro INT, FOREIGN KEY (fkCarro) REFERENCES Carro(idCarro)
);

CREATE TABLE Medida(
idMedida INT PRIMARY KEY AUTO_INCREMENT
,horarioRegistro DATETIME
,valor DECIMAL
,fkDispositivo INT, FOREIGN KEY (fkDispositivo) REFERENCES Dispositivo(idDispositivo)
);










