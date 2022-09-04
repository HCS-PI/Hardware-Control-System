import psutil, os, cpuinfo, platform, time, shutil, src.intro as intro, src.relatorio as relatorio, src.mascara as mascara, threading, socket, ipaddress
from src.insertData import startInsert
from tabulate import tabulate

intro.callIntro()
isSQLActive = True

limpar = 'clear' if platform.system() == 'Linux' else 'cls'

if isSQLActive:
    import src.runData as runData
    runData.start()

def getProcessador():
    data = [
        ["Modelo", cpuinfo.get_cpu_info()['brand_raw']],
        ["Uso do Processador", f"{psutil.cpu_percent()}%"],
        ["Quantidade de Núcleos", psutil.cpu_count(logical=False)],
        ["Quantidade de Núcleos Lógicos", psutil.cpu_count(logical=True)],
        ["Frequência Máxima", f"{psutil.cpu_freq().max}Ghz"]
    ]

    j = 1
    for i in psutil.cpu_percent(percpu=True):
        data.append([f"Uso CPUv {j}", f"{i}%"])
        j+=1

    os.system(limpar)
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getProcessadorLive():
    processadores = ""
    
    j = 1
    for i in psutil.cpu_percent(percpu=True):
        processadores += f"\033[1mUso CPUv {j}:\033[0m {i}%"
        
        if j < len(psutil.cpu_percent(percpu=True)):
            processadores+="\n"
        j+=1
    
    return processadores

def getMemoriaRAM():
    data = [
        ["Espaço na Memória", f"{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB"],
        ["Uso da Memória", f"{psutil.virtual_memory().percent}% ({round(psutil.virtual_memory().used / 1024 ** 3, 1)}GB/{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB)%"]
    ]

    os.system(limpar)
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getMemoriaInterna():
    data = []

    if platform.system() == 'Linux':
        data.append(["Espaço no Disco Rígido", f"{round(shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3, 1)} GB"])
        data.append(["Espaço Usado", f"{round(shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3, 1)} GB"])
        data.append(["Espaço Livre", f"{round(shutil.disk_usage('/home/hcs/Documentos').free / 1024 ** 3, 1)} GB"])
        data.append(["Porcentagem de Uso", f"{round(((shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3) * 100) / (shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3), 1)}%"])
    else:
        for i in psutil.disk_partitions():
            print('windows')
            data.append(["Dispositivo", i[0]])
            data.append(["Tipo de Arquivo", i[2]])
            data.append(["Espaço no Disco Rígido", f"{round(shutil.disk_usage('/').total / 1024 ** 3, 1)} GB"])
            data.append(["Espaço Usado", f"{round(shutil.disk_usage('/').used / 1024 ** 3, 1)} GB"])
            data.append(["Espaço Livre", f"{round(shutil.disk_usage('/').free / 1024 ** 3, 1)} GB"])
            data.append(["Porcentagem de Uso", f"{round(((shutil.disk_usage('/').used / 1024 ** 3) * 100) / (shutil.disk_usage('/').total / 1024 ** 3), 1)}%"])
    
    os.system(limpar)
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getMemoriaInternaLive():
    memoriaInterna = ""
    if platform.system() == 'Linux':
        memoriaInterna += f"\033[1mEspaço no Disco Rígido:\033[0m {round(shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3, 1)} GB\n"
        memoriaInterna += f"\033[1mEspaço Usado:\033[0m {round(shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3, 1)} GB\n"
        memoriaInterna += f"\033[1mEspaço Livre:\033[0m {round(shutil.disk_usage('/home/hcs/Documentos').free / 1024 ** 3, 1)} GB\n"
        memoriaInterna += f"\033[1mPorcentagem de Uso:\033[0m {round(((shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3) * 100) / (shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3), 1)}%"
    else:
        for i in psutil.disk_partitions():
            memoriaInterna += f"\033[1mDispositivo:\033[0m {i[0]}\n\n"
            memoriaInterna += f"\033[1mCaminho de Arquivo:\033[0m {i[1]}\033[0m\n"
            memoriaInterna += f"\033[1mTipo de Arquivo:\033[0m {i[2]}\033[0m\n"
            memoriaInterna += f"\033[1mEspaço no Disco Rígido:\033[0m {round(shutil.disk_usage('/').total / 1024 ** 3, 1)} GB\n"
            memoriaInterna += f"\033[1mEspaço Usado:\033[0m {round(shutil.disk_usage('/').used / 1024 ** 3, 1)} GB\n"
            memoriaInterna += f"\033[1mEspaço Livre:\033[0m {round(shutil.disk_usage('/').free / 1024 ** 3, 1)} GB\n"
            memoriaInterna += f"\033[1mPorcentagem de Uso:\033[0m {round(((shutil.disk_usage('/').used / 1024 ** 3) * 100) / (shutil.disk_usage('/').total / 1024 ** 3), 1)}%\n"
    return memoriaInterna

def getOS():
    data = [
        ["\033[1mSistema\033[0m", f"{platform.system()} {platform.release()}"],
        ["\033[1mVersão\033[0m", platform.version()]
    ]

    os.system(limpar)
    return tabulate(data)

def getRede():
    data = [
        ["GB Enviados",
            f"{str(round(psutil.net_io_counters()[0] * 10 ** -9, 3))} GB"],
        ["GB Recebidos",
            f"{str(round(psutil.net_io_counters()[1] * 10 ** -9, 3))} GB"],
        ["Pacotes Enviados", f"{mascara.getNumero(psutil.net_io_counters()[3])}"],
        ["Pacotes Recebidos", f"{mascara.getNumero(psutil.net_io_counters()[4])}"],
        ["Endereço IP", f"{socket.gethostbyname(socket.gethostname())}"],
        ["Máscara da Rede", f"{ipaddress.IPv4Network(socket.gethostbyname(socket.gethostname()))}"]
    ]

    os.system(limpar)
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getBateria():
    os.system(limpar)

    if str(psutil.sensors_battery()) == 'None':
        return "Dispositivo não alimentado por bateria"
    else:
        data = [
        ["Porcentagem de Bateria", f"{psutil.sensors_battery().percent}%"]
        ]
        
        if platform.system() != 'Linux':
            data.append(["Minutos Restantes", f"{round(psutil.sensors_battery().secsleft / 60, 0)} minutos"])

        if psutil.sensors_battery().power_plugged:
            data.append(["Está Carregando?", "Sim"])
        else:
            data.append(["Está Carregando?", "Não"])

        return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getBateriaLive():
    if str(psutil.sensors_battery()) == 'None':
        return "Dispositivo não alimentado por bateria"
    else:
        bateria = ""
        
        bateria += f"\033[1mPorcentagem de Bateria:\033[0m {psutil.sensors_battery().percent}%\n"

        if platform.system() != 'Linux':
            bateria += f"\033[1mMinutos Restantes:\033[0m {round(psutil.sensors_battery().secsleft / 60, 0)} minutos\n"
        
        if psutil.sensors_battery().power_plugged:
            bateria += "\033[1mEstá Carregando?\033[0m Sim\n"
        else:
            bateria += "\033[1mEstá Carregando?\033[0m Não"

        return bateria

def getTemperatura():
    return psutil.sensors_temperatures()

def main():
    threading.Thread(target=startInsert).start()

    dictFunctions = {'2': getProcessador, '3': getMemoriaRAM, '4': getMemoriaInterna, '5': getOS, '6': getRede, '7': getBateria, '8': getTemperatura, '9': relatorio.createRelatorio}
    index = 0

    while index != '10':
        os.system(limpar)
        index = input("\033[1mHardware Data\033[0m\n\n[1] - Estatísticas em tempo real\n[2] - Processador\n[3] - Memória RAM\n[4] - Memória Interna\n[5] - Sistema Operacional\n[6] - Rede\n[7] - Bateria\n[8] - Temperatura\n[9] - Relatório\n[10] - Sair\n\n\033[1m>>>\033[0m ")
        os.system(limpar)
        if int(index) > 0 and int(index) < 10:
            print('Buscando dados...')
        try:
            if index == '10':
                os.system(limpar)
                print('\033[1mHardware Controll System\033[0m - Volte Sempre!\n\n')
                time.sleep(4)
                exit()
            elif index != '1':
                print(dictFunctions[index]())
            else:
                tracos = '----------------'
                while True:
                    a = "\033[1m"
                    b = "\033[0m"
                    print(f"""{a}HCS - Análise de Hardware Nativo{b}

{a}{tracos} PROCESSADOR {tracos}
{a}Uso do Processador:{b} {psutil.cpu_percent()}% 
{str(getProcessadorLive())}
{a}{tracos}              {tracos}{b}\n
{a}{tracos} MEMÓRIA RAM {tracos}
{a}Uso da Memória RAM:{b} {psutil.virtual_memory().percent}% ({round(psutil.virtual_memory().used / 1024 ** 3, 1)}GB/{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB)
{a}{tracos}             {tracos}{b}\n
{a}{tracos} MEMÓRIA INTERNA {tracos}
{str(getMemoriaInternaLive())}
{a}{tracos}                 {tracos}{b}\n
{a}{tracos} REDE {tracos}{b}
{a}Qtd. Dados Enviados:{b} {round(psutil.net_io_counters()[0] * 10 ** -9, 3)} GB
{a}Qtd. Dados Recebidos:{b} {round(psutil.net_io_counters()[1] * 10 ** -9, 3)} GB
{a}Pacotes Enviados:{b} {psutil.net_io_counters()[3]}
{a}Pacotes Recebidos{b} {psutil.net_io_counters()[4]}
{a}Endereço IP{b} {socket.gethostbyname(socket.gethostname())}
{a}Máscara da Rede{b} {ipaddress.IPv4Network(socket.gethostbyname(socket.gethostname()))}
{a}{tracos} {tracos}{b}\n
{a}{tracos} BATERIA {tracos}
{str(getBateriaLive())}
{a}{tracos}         {tracos}{b}\n
""")
                    time.sleep(1)
                    os.system(limpar)
        except:
            main()
        input('\nPressione enter para voltar ao menu...\n\n')

os.system(limpar)
main()