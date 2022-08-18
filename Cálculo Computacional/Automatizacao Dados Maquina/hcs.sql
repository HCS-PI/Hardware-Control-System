create database hcs;
use hcs;

create table Empresa (
idEmpresa int primary key auto_increment,
nomeEmpresa varchar (45),
cnpj varchar(14),
nomeRepresentante varchar(45),
senha varchar(12) 
)auto_increment=4523;

create table Cliente (
idCliente int primary key auto_increment,
nome varchar(45),
senha varchar(12)
);

create table Carro (
idCarro int primary key auto_increment,
modelo varchar (45),
placa varchar(15),
dataFabricacao varchar(10),
placaMae varchar(45),
placaVideo varchar (45),
processador varchar (45),
voltagem char(4),
fkCliente int,
fkEmpresa int
)auto_increment=5678;

select * from Empresa;

select * from Cliente;

SELECT * FROM Carro join Cliente where fkCliente = idCliente;

select * from Carro;

insert into Empresa values (null, 'Tesla', '123456789', 'Marise', 'urubu100');

insert into Cliente values (null, 'Maria', '123456');

insert into Carro values(null, 'Model X', 'GHT1234', '23/04/2019', 'GH10M-T', 'RTX560', 'I9 10 Geracao', '220V', 1, 4523);

SELECT * FROM Carro join Empresa on Carro.fkEmpresa = Empresa.idEmpresa;