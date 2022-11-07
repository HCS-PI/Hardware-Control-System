
CREATE DATABASE hardware_control_system;

USE  hardware_control_system;

CREATE TABLE Empresa(
id_empresa INT PRIMARY KEY IDENTITY(1,1)
,nome_empresa VARCHAR(40)
,cnpj VARCHAR(18)
);

CREATE TABLE Funcionario(
id_funcionario INT PRIMARY KEY IDENTITY(1,1)
,nome_funcionario VARCHAR(64)
,cpf CHAR(14)
,email VARCHAR(100)
,senha VARCHAR(256)
,cargo CHAR(3)
,fk_empresa INT FOREIGN KEY REFERENCES Empresa(id_empresa)
);

CREATE TABLE Carro(
id_carro INT PRIMARY KEY IDENTITY(1,1)
,endereco_mac VARCHAR(17)
,placa_carro CHAR(7)
,modelo VARCHAR(64)
,fk_empresa INT FOREIGN KEY REFERENCES Empresa(id_empresa)
);

CREATE TABLE Dispositivo(
id_dispositivo INT PRIMARY KEY IDENTITY(1,1)
,tipo VARCHAR(45)
,modelo VARCHAR(45)
,unid_medida VARCHAR(10)
,fk_carro INT FOREIGN KEY REFERENCES Carro(id_carro)
);

CREATE TABLE Medida(
id_medida INT PRIMARY KEY  IDENTITY(1,1)
,horario_registro DATETIME
,valor DECIMAL(5,1)
,fk_dispositivo INT FOREIGN KEY REFERENCES Dispositivo(id_dispositivo)
);

SELECT * FROM Empresa

insert into Empresa(nome_empresa ,cnpj ) 
values ('Tesla Corporation', '35.008.715/0001-75')
		,('Hyundai', '05.127.365/0001-03');

insert into Funcionario (nome_funcionario ,cpf ,email ,senha ,cargo,fk_empresa)
values ('Carlos Alberto', '996.912.830-26','teslaADM@gmail.com', 'senhascreta123', 'ADM', 1)
	,('Leonardo Vasconcelos', '802.916.120-40','hyundaiADM@gmail.com', 'senhascreta456', 'ADM', 2);

INSERT INTO Carro(endereco_mac ,placa_carro ,modelo, fk_empresa)
values ('C2-F2-9F-2A-F9-7C', 'ABC1256', 'Model S', 1)
		,('87-93-87-EF-B1-0B', 'CDE1234', 'Model X', 1)
		,('87-93-22-EF-B1-0B', 'CDE1234', 'Model G', 2)
		,( '10-B1-A8-76-99-DD', 'EFG7891', 'Ioniq 5', 2);


insert into Dispositivo (tipo ,modelo ,unid_medida ,fk_carro )
	values	('CPU', 'Intel i5 7400', '%', 1)
			,('CPU', 'Intel i5 10500H', '%', 2)
			,('RAM', 'Kingston 8GB 1600 Mhz DDR3L', '%', 1)
			,('RAM', 'Corsair Value Select 16GB, 2133Mhz, DDR4', '%', 2)
			,('CPU', 'Intel i5 7400', '%', 3)
			,('CPU', 'Intel i5 7400', '%', 4)
			,('RAM', 'Kingston 8GB 1600 Mhz DDR3L', '%', 3);


insert into Medida (horario_registro ,valor ,fk_dispositivo )
	values (CURRENT_TIMESTAMP, 50.0, 1)
			,(CURRENT_TIMESTAMP, 50.0, 1)
			,(CURRENT_TIMESTAMP, 50.0, 1)
			,(CURRENT_TIMESTAMP, 80.0, 2)
			,(CURRENT_TIMESTAMP, 40.0, 2)
			,(CURRENT_TIMESTAMP, 77.0, 3)
			,(CURRENT_TIMESTAMP, 44.0, 3)
			,(CURRENT_TIMESTAMP, 37.0, 4)
			,(CURRENT_TIMESTAMP, 28.5, 4)
			,(CURRENT_TIMESTAMP, 50.0, 5)
			,(CURRENT_TIMESTAMP, 50.0, 5)
			,(CURRENT_TIMESTAMP, 77.0, 6)
			,(CURRENT_TIMESTAMP, 44.0, 7);


SELECT * FROM Empresa;
SELECT * FROM Funcionario;

SELECT * FROM Dispositivo;
Select * from Carro;
SELECT * FROM Medida;


CREATE VIEW vwDashGesCPU AS 
SELECT TOP 5 id_empresa as 'CodEmpresa',
		Carro.modelo AS 'ModeloCarro',
		tipo AS 'Componente',
		unid_medida AS 'UnidadeMedida',
		round(avg(valor),1) AS 'MediaConsumo' FROM Empresa, Carro, Dispositivo, Medida
WHERE id_empresa = fk_empresa AND fk_carro = id_carro 
AND fk_dispositivo = id_dispositivo AND tipo = 'CPU'
group by Carro.modelo, id_empresa,tipo,unid_medida ;


CREATE VIEW vwDashGesRAM AS 
SELECT TOP 5 id_empresa as 'CodEmpresa',
		Carro.modelo as 'ModeloCarro',
		tipo as 'Componente',
		unid_medida as 'Unidade de Medida',
		round(avg(valor),1) as 'MediaConsumo'
		FROM Empresa, Carro, Dispositivo, Medida
		WHERE fk_empresa = id_empresa AND fk_carro = id_carro AND fk_dispositivo = id_dispositivo AND tipo = 'RAM' 
		group by Carro.modelo,id_empresa,tipo,unid_medida

select * from vwDashGesCPU where CodEmpresa = 1 order by MediaConsumo DESC;
select * from vwDashGesRAM where CodEmpresa = 1 order by MediaConsumo DESC;
GO


CREATE VIEW vwDashTec AS
Select TOP 5 id_empresa as CodEmpresa,
Carro.id_carro AS 'IdCarro',
Carro.modelo AS 'Modelo',
Carro.placa_carro AS 'Placa',
Medida.valor as 'Valor',
tipo as 'Componente',
unid_medida as 'UnidadeMedida' 
FROM Empresa, Carro, Dispositivo, Medida
WHERE fk_empresa = id_empresa AND fk_carro = id_carro AND fk_dispositivo = id_dispositivo
GROUP BY id_empresa,Medida.valor,unid_medida, Carro.id_carro,Carro.modelo,Carro.placa_carro,tipo  ;



Select * from vwDashTec ORDER BY Valor desc;
SELECT * from vwDashTec WHERE CodEmpresa = 1;

