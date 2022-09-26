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
,valor DECIMAL(5,1)
,fkDispositivo INT, FOREIGN KEY (fkDispositivo) REFERENCES Dispositivo(idDispositivo)
);


insert into Empresa values (null, 'Tesla Corporation', '35.008.715/0001-75');
insert into Funcionario values (null, 'Carlos Alberto', '996.912.830-26','teslaADM@gmail.com', 'senhascreta123', 'ADM', 1);
insert into Carro values (null, 'C2-F2-9F-2A-F9-7C', 'ABC1256', 'Model S', 1);
insert into Carro values (null, '87-93-87-EF-B1-0B', 'CDE1234', 'Model X', 1);

insert into Dispositivo values (null, 'CPU', 'Intel i5 7400', '%', 1); 
insert into Dispositivo values (null, 'CPU', 'Intel i5 10500H', '%', 2);

insert into Medida values (null, now(), 50.0, 1);
insert into Medida values (null, now(), 50.0, 1);
insert into Medida values (null, now(), 80.0, 2);
insert into Medida values (null, now(), 40.0, 2);

insert into Dispositivo values (null, 'RAM', 'Kingston 8GB 1600 Mhz DDR3L', '%', 1); 
insert into Dispositivo values (null, 'RAM', 'Corsair Value Select 16GB, 2133Mhz, DDR4', '%', 2);

insert into Medida values (null, now(), 77.0, 3);
insert into Medida values (null, now(), 44.0, 3);
insert into Medida values (null, now(), 37.0, 4);
insert into Medida values (null, now(), 28.5, 4);

insert into Empresa values (null, 'Hyundai', '05.127.365/0001-03');
insert into Funcionario values (null, 'Leonardo Vasconcelos', '802.916.120-40','hyundaiADM@gmail.com', 'senhascreta456', 'ADM', 2);
insert into Carro values (null, '10-B1-A8-76-99-DD', 'EFG7891', 'Ioniq 5', 2);

insert into Dispositivo values (null, 'CPU', 'Intel i5 7400', '%', 3); 

insert into Medida values (null, now(), 50.0, 5);
insert into Medida values (null, now(), 50.0, 5);

insert into Dispositivo values (null, 'RAM', 'Kingston 8GB 1600 Mhz DDR3L', '%', 1); 

insert into Medida values (null, now(), 77.0, 6);
insert into Medida values (null, now(), 44.0, 6);


CREATE VIEW `vw_dashGES_CPU` AS
SELECT idEmpresa,
Carro.modelo as ModeloCarro,
tipo as Componente,
unidMedida as 'Unidade de Medida',
round(avg(valor),1) as MediaConsumo
FROM Empresa, Carro, Dispositivo, Medida
WHERE fkEmpresa = idEmpresa AND fkCarro = idCarro AND fkDispositivo = idDispositivo AND tipo ="CPU" group by Carro.modelo;

CREATE VIEW `vw_dashGES_RAM` AS
SELECT idEmpresa,
Carro.modelo as ModeloCarro,
tipo as Componente,
unidMedida as 'Unidade de Medida',
round(avg(valor),1) as MediaConsumo
FROM Empresa, Carro, Dispositivo, Medida
WHERE fkEmpresa = idEmpresa AND fkCarro = idCarro AND fkDispositivo = idDispositivo AND tipo ="RAM" group by Carro.modelo;

select * from vw_dashGES_CPU;

/*Selecionando as tabelas dinâmicas referentes a empresa TESLA*/
select * from vw_dashGES_CPU where idEmpresa = 1;
select * from vw_dashGES_RAM where idEmpresa = 1;

/*Selecionando as tabelas dinâmicas referentes a empresa HYUNDAI*/
select * from vw_dashGES_CPU where idEmpresa = 2;
select * from vw_dashGES_RAM where idEmpresa = 2;




