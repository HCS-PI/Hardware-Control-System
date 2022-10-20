from pickle import FALSE, TRUE
import intro, capturarDados
import os, time, platform
import keyboard as kb

intro.callIntro()
limpar = 'clear' if platform.system() == 'Linux' else 'cls'

def main():
    # login = input(str("Digite seu login:    "))
    # senha = input(str("Digite sua Senha:    "))



    # while login != "teste@gmail.com" or senha != "1234":
    #     print("Credenciais Inválidas. Digite Novamente")

    #     login = input(str("Digite seu login:    "))
    #     senha = input(str("Digite sua Senha:    "))

    # os.system(limpar)

    opcaoMenu = -1

    while opcaoMenu != 0:

        print(''' 
        \033[1m ESCOLHA UMA OPÇÃO:

          \033[92m[ 1 ] Exibir Dados do Servidor
          \033[91m[ 0 ] Sair do Programa
          \033[0m''')
        print("=-="*30)

        opcaoMenu = int(input('\033[1m>>>>>> Qual é a sua opção? \033[0m'))
       
        if opcaoMenu == 0:
                print ("Encerrando Programa ....")

        try:

                if opcaoMenu == 1:
                        isExibirDados = True;
                        while isExibirDados:
                                print('=-='*50)
                                print("\033[1mPressione \033[91mCtrl + C\033[0m \033[1mpara voltar ao Menu!\033[0m")
                                capturarDados.dadosCPU()
                                capturarDados.dadosRAM()
                                capturarDados.dadosDisco()
                                time.sleep(1)
                                os.system(limpar)
                        
                elif opcaoMenu != 0 or opcaoMenu !=1:
                        print("opção Inválida. Digite Novamente")
        except:
                time.sleep(1)
                os.system(limpar)
                main()
           
     



os.system(limpar)
main()