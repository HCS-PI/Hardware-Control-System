import mysql.connector
from mysql.connector import Error
import os  
import getpass 
import psutil


conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='@Pedrinho1')

if conexao.is_connected():
        hcs = conexao.get_server_info()
        print("conectado ao servidor MySQL")

def menu():
 menu()
 os.system('cls')
print('''
/***
 *     __    __       ___      .______       _______  ____    __    ____      ___      .______       _______ 
 *    |  |  |  |     /   \     |   _  \     |       \ \   \  /  \  /   /     /   \     |   _  \     |   ____|
 *    |  |__|  |    /  ^  \    |  |_)  |    |  .--.  | \   \/    \/   /     /  ^  \    |  |_)  |    |  |__   
 *    |   __   |   /  /_\  \   |      /     |  |  |  |  \            /     /  /_\  \   |      /     |   __|  
 *    |  |  |  |  /  _____  \  |  |\  \----.|  '--'  |   \    /\    /     /  _____  \  |  |\  \----.|  |____ 
 *    |__|  |__| /__/     \__\ | _| `._____||_______/     \__/  \__/     /__/     \__\ | _| `._____||_______|
 *                                                                                                           
 *      ______   ______   .__   __. .___________..______        ______    __       __                        
 *     /      | /  __  \  |  \ |  | |           ||   _  \      /  __  \  |  |     |  |                       
 *    |  ,----'|  |  |  | |   \|  | `---|  |----`|  |_)  |    |  |  |  | |  |     |  |                       
 *    |  |     |  |  |  | |  . `  |     |  |     |      /     |  |  |  | |  |     |  |                       
 *    |  `----.|  `--'  | |  |\   |     |  |     |  |\  \----.|  `--'  | |  `----.|  `----.                  
 *     \______| \______/  |__| \__|     |__|     | _| `._____| \______/  |_______||_______|                  
 *                                                                                                           
 *         _______.____    ____      _______..___________. _______ .___  ___.                                
 *        /       |\   \  /   /     /       ||           ||   ____||   \/   |                                
 *       |   (----` \   \/   /     |   (----``---|  |----`|  |__   |  \  /  |                                
 *        \   \      \_    _/       \   \        |  |     |   __|  |  |\/|  |                                
 *    .----)   |       |  |     .----)   |       |  |     |  |____ |  |  |  |                                
 *    |_______/        |__|     |_______/        |__|     |_______||__|  |__|                                
 *                                                                                                           
 */
''')

nome = input('Para iniciar por favor insira seu nome:')

while (nome == ''): 
     print('Insira um nome válido.')
     break   



else:
    os.system('cls')

    while True:
        print('Olá! ', nome,'. Seja bem vindo ao nosso sistema de controle de hardware.')
        print('''
                    
                    
                            [CE] -  Cadastrar Empresa
                            [CM] -  Cadastrar Carro
                            [CC]  - Cadastrar Cliente
                            [LE] - Login Empresa
                            [LC]  - Login Cliente
                            [CD] - Consultar dados 
                            [S]  -  Sair
        ''')
                
        opcao = input('Escolha uma opção:')

        if(opcao == 'CE' or opcao == 'ce'):
                
                    # conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='sptech')
                
                    cursor = conexao.cursor()
                    
                    nomeEmpresa = input('Qual o nome da empresa?')
                    cnpj = input('Qual o CNPJ?')
                    nomeRepresentante = input('Qual o do representante?')
                    senha = getpass.getpass(prompt='Escolha uma senha:', stream=None);

                    cursor.execute("INSERT INTO Empresa (nomeEmpresa, cnpj, nomeRepresentante, senha) VALUES('{}','{}','{}','{}');".format(nomeEmpresa,cnpj,nomeRepresentante,senha))
                
                    conexao.commit()
                    print('Empresa cadastrada com sucesso!')

        if(opcao == 'CM' or opcao == 'cm'):

                    # conexao = mysql.connector.connect(host='localhost', database='hcs', user='root', password='sptech')

                    cursor = conexao.cursor()

                    placa = input('Qual a placa?')
                    dataFabricacao = input('Qual a data de fabricação?')
                    placaMae = input('Qual o modelo da placa mãe?')
                    placaVideo = input('Qual o modelo da placa de video?')
                    processador = input('Qual o modelo do processador?')
                    voltagem = input('Qual a voltagem do carregador?')
                    fkCliente = input('Qual o código do proprietário?')
                    fkEmpresa = input('Qual o código da marca?')

                    cursor.execute("INSERT INTO Carro (placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa) VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa))
                    print('Carro cadastrado com sucesso!')
        if(opcao == 'CC' or opcao == 'cc'):

                    cursor = conexao.cursor()

                    nome = input('Insira o nome do cliente:')
                    senha = getpass.getpass(prompt='Escolha uma senha para o cliente:', stream=None)

                    cursor.execute("INSERT INTO Cliente (nome, senha) VALUES('{}','{}')".format(nome, senha))
                    print('Cliente cadastrada com sucesso!')
        if (opcao == 'LE' or opcao == 'le'):

            cnpj = input('Informe o código de sua empresa:')
            senha = input('Informe sua senha:')
            query = ("SELECT * FROM Empresa")
            cursor = conexao.cursor()
            cursor.execute(query)
            dados = cursor.fetchall()
            
            
            for dado in dados:
                        if(cnpj != dado[2] or senha !=dado[4]):
                            print('Código incorreto')
                        else:
                            query2 = ("SELECT modelo, placa, dataFabricacao, placaMae,placaVideo, processador, voltagem, fkCliente, fkEmpresa FROM Carro;")
                            cursor = conexao.cursor()
                            cursor.execute(query2)
                            dadosC = cursor.fetchall()

                            print('Olá ', dado[1], '!')
                            print('Listando dados de todos os automóveis disponíveis:')
                            
                        for dadosCarro in dadosC:
                            print('|Modelo: ',dadosCarro[1])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa:',dadosCarro[2])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Data de fabricação:',dadosCarro[3])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa Mãe:',dadosCarro[4])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa de Vídeo:',dadosCarro[5])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Processador/CPU: ',dadosCarro[6], end="")
                            print(psutil.cpu_percent(interval=None))
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print ('|Carga média dos processos sendo executados: ', end="")
                            print(psutil.getloadavg())
                            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
                            print('|Uso da memória do sistema:', end="")
                            print(psutil.virtual_memory())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Voltagem:', dadosCarro[7])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
                            print('|Id do proprietário:', dadosCarro[8])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Carga restante da bateria:', end="")
                            print(psutil.sensors_battery())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')




        if (opcao == 'LC' or opcao == 'lc'):

            login = input('Informe o seu código:')
            senha = getpass.getpass(prompt='Insira sua senha:', stream=None)
            query = ("SELECT * FROM Cliente;")
            cursor = conexao.cursor()
            cursor.execute(query)
            dados = cursor.fetchall()

            for dado in dados:
                    if(login != dado[0] or senha != dado[2]):
                        print('Código/senha incorreto!')
            else:
                        os.system('cls')
                        print('Olá ', dado[1], '!')
                        print('Listando dados de todos os automóveis disponíveis:')
                        query2 = ("SELECT * FROM Carro join Cliente where Carro.fkCliente = Cliente.idCliente;")
                        cursor = conexao.cursor()
                        cursor.execute(query2)
                        dadosC = cursor.fetchall()

                       
                        
                        for dadosCarro in dadosC:
                            print('|Modelo: ',dadosCarro[1])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa:',dadosCarro[2])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Data de fabricação:',dadosCarro[3])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa Mãe:',dadosCarro[4])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Placa de Vídeo:',dadosCarro[5])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Processador/CPU: ',dadosCarro[6], end="")
                            print(psutil.cpu_percent(interval=None))
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print ('|Carga média dos processos sendo executados: ', end="")
                            print(psutil.getloadavg())
                            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
                            print('|Uso da memória do sistema:', end="")
                            print(psutil.virtual_memory())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Voltagem:', dadosCarro[7])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
                            print('|Id do proprietário:', dadosCarro[8])
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')
                            print('|Carga restante da bateria:', end="")
                            print(psutil.sensors_battery())
                            print ('|------------------------------------------------------------------------------------------------------------------------------------')


        if(opcao == 'CD' or opcao == 'cd'):
            os.system('cls')

            print('''   
                     ___¦¦¦¦¦¦¦¦¦¦¦_____
                    |¦¦¦¦¦¦¦¦____¦¦¦¦¦¦¦¦|
                    |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦|
                    ¯(@)(@)¯¯¯¯¯¯¯(@)(@)¯
            ''')
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print('|Listando dados de seu automóvel Tesla Model X:')
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print('|Processador/CPU: ', end="")
            print(psutil.cpu_percent(interval=None))
            print ('|------------------------------------------------------------------------------------------------------------------------------------')
            print ('|Carga média dos processos sendo executados: ', end="")
            print(psutil.getloadavg())
            print ('|-----------------------------------------------------------------------------------------------------------------------------------')
            print('|Uso da memória do sistema:', end="")
            print(psutil.virtual_memory())
            print ('|------------------------------------------------------------------------------------------------------------------------------------')            
            print('|Carga restante da bateria:', end="")
            print(psutil.sensors_battery())
            print ('|------------------------------------------------------------------------------------------------------------------------------------')


        if(opcao == 's' or opcao == 'S'):
            os.system('cls')               
            conexao.close()
            print('Obrigada por utilizar nosso programa!')
        break

