#!/bin/bash

cd /home/ubuntu;
clear;
echo "Script de instalação do projeto HCS de PI";
echo "Este Script de instalação baixará e instalará o gerenciador de pacotes 'sdk man', o java 11 e o mysql, assim como os repositórios HCS.";
sleep 2;
echo "Digite 's' para continuar ou qualquer outra tecla para cancelar as instalações"
echo ;

read inst
if [ \"$inst\" == \"s\" ]
	then
        sleep 2;
        echo ;
        echo "Instalando o gerenciador de pacotes";
        curl -s "https://get.sdkman.io" | bash;
        echo ;
        echo "Instalando java...";
        sdk install java 11.0.16-amzn;
        sleep 2;

        echo ;
        echo "Instalando banco de dados...";
        sleep 2;

        echo ;
        sudo apt install mysql-server;
        echo ;
        echo "Baixando repositórios...";
        sleep 2;

        echo ;
        git clone https://github.com/HCS-PI/projetojar.git;
        cd projetojar;
        git pull;
        echo ;
        ls;
        echo "Os arquivos em vermelho são executáveis .jar, entre com uma GUI para visualizá-los e interagir com eles.";
        echo "Ele está localizado em:";
        pwd;
        sleep 2;

        echo ;
        cd /home/ubuntu;
        git clone https://github.com/HCS-PI/Hardware-Control-System.git;
        cd Hardware-Control-System;
        git pull;
        echo ;
        ls;
        echo "Este é o repositório padrão, com toda a aplicação e o banco de dados";
        echo "Ele está localizado em";
        pwd;
        echo ;
        cd /home/ubuntu;
        echo "Script Finalizado...";

    else
        echo ;
        echo "O script será finalizado agora, nenhuma alteração foi feita"
        sleep 2;
fi