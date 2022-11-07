select * from funcionario;
select * from Dispositivo;
insert into funcionario values (null, 'Gestor Tesla', '123.456.789-85', 'teslaGES@gmail.com', 'gestorTesla123', 'GES', 1);
insert into funcionario values (null, 'Gestor Hyundai', '987.654.321-56', 'hyundaiGES@gmail.com', 'gestorHyundai123', 'GES', 2);

insert into Carro values (null, 'E2-C2-WF-BA-L9-8C', 'ULI5874', 'Model Y', 1);
select * from Carro;

insert into Dispositivo values (null, 'CPU', 'Intel i5 10500H', '%', 4);
select * from Dispositivo;

insert into Medida values (null, now(), 55.6, 7);
insert into Medida values (null, now(), 35.7, 7);

insert into Dispositivo values (null, 'RAM', 'Kingston 8GB 1600 Mhz DDR3L', '%', 4); 
select * from Dispositivo;

insert into Medida values (null, now(), 37.0, 8);
insert into Medida values (null, now(), 28.5, 8);

select * from Dispositivo;
