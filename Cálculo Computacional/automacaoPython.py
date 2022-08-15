import psutil as ps;
import time;
import math;
import os
import mysql.connector as bd;
''' para sql server:

import pyodbc;
'''

def maquina():
  # variaveis
  qntd_execucao = 0;
  usuario = ps.users();
  cores = ps.cpu_count(logical=True);
  threads = ps.cpu_count(logical=False);
  
  # conexão com o banco
  conexao = bd.connect(
  host = 'localhost',
  user = 'aluno',
  password = 'sptech'
  );  

  #relatorio
  while True:
   os.system('clear')
   x = ps.cpu_percent();
   y = ps.disk_usage('/');
   mem = ps.virtual_memory();
   ram = mem.available / (1024)**2;
   qntd_execucao+=1;
   
   print('======================================================\n')
   print(f'Quantidade de execução: {qntd_execucao}\n')
   print(f'cpu porcentagem: {x}%');
   print(f'disco porcentagem: {y.percent}%')
   print(f'memória RAM :{math.floor(ram)}MB')
   print(f'Quantidade de núcleos: {cores} e threads: {threads}\n')
   print('======================================================')
   time.sleep(1);
   
  
maquina();
