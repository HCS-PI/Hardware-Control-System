create database teste_java;
use teste_java;

create table teste (
	id int primary key auto_increment,
    email varchar(100),
    senha varchar(100)
);

insert into teste values (null, 'teste@gmail.com', '1234');