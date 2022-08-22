import psutil, os, cpuinfo, platform, time, shutil, intro, relatorio, mascara

from tabulate import tabulate

intro.callIntro()
isSQLActive = True

if isSQLActive:
    import runData
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
        data.append([f"Uso CPU {j}", f"{i}%"])
        j+=1

    os.system('cls')
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getProcessadorLive():
    processadores = ""
    
    j = 1
    for i in psutil.cpu_percent(percpu=True):
        processadores += f"\033[1mUso CPU {j}:\033[0m {i}%\n"
        j+=1
    
    return processadores

def getMemoriaRAM():
    data = [
        ["Espaço na Memória", f"{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB"],
        ["Uso da Memória", f"{psutil.virtual_memory().percent}% ({round(psutil.virtual_memory().used / 1024 ** 3, 1)}GB/{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB)%"]
    ]

    os.system('cls')
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getMemoriaInterna():
    data = []

    for i in psutil.disk_partitions():
        data.append(["Dispositivo", i[0]])
        data.append(["Tipo de Arquivo", i[2]])
        data.append(["Espaço no Disco Rígido", round(shutil.disk_usage("/").total / 1024 ** 3, 1)])
        data.append(["Espaço Usado", round(shutil.disk_usage("/").used / 1024 ** 3, 1)])
        data.append(["Espaço Livre", round(shutil.disk_usage("/").free / 1024 ** 3, 1)])
        data.append(["Porcentagem de Uso", round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)])

    os.system('cls')
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getMemoriaInternaLive():
    memoriaInterna = ""
    for i in psutil.disk_partitions():
        memoriaInterna += f"\033[1mDispositivo: {i[0]}\033[0m\n"
        memoriaInterna += f"\033[1mCaminho de Arquivo: {i[1]}\033[0m\n"
        memoriaInterna += f"\033[1mTipo de Arquivo: {i[2]}\033[0m\n"
    return memoriaInterna

def getOS():
    data = [
        ["\033[1mSistema\033[0m", f"{platform.system()} {platform.release()}"],
        ["\033[1mVersão\033[0m", platform.version()]
    ]

    os.system('cls')
    return tabulate(data)

def getRede():
    data = [
        ["GBs Enviados",
            f"{str(round(psutil.net_io_counters()[0] * 10 ** -9, 3))} GB"],
        ["GBs Recebidos",
            f"{str(round(psutil.net_io_counters()[1] * 10 ** -9, 3))} GB"],
        ["Pacotes Enviados", f"{mascara.getNumero(psutil.net_io_counters()[3])}"],
        ["Pacotes Recebidos", f"{mascara.getNumero(psutil.net_io_counters()[4])}"],
        ["Endereço IP", f"{psutil.net_if_addrs()['Ethernet'][1][1]}"],
        ["Máscara da Rede", f"{psutil.net_if_addrs()['Ethernet'][1][2]}"]
    ]

    os.system('cls')
    return tabulate(data, headers=['\033[1mFunção\033[0m', '\033[1mValor\033[0m'])

def getBateria():
    os.system('cls')

    if str(psutil.sensors_battery()) == 'None':
        return "Dispositivo não alimentado por bateria"
    else:
        data = [
        ["Porcentagem de Bateria", f"{psutil.sensors_battery().percent}%"],
        ["Minutos Restantes", f"{round(psutil.sensors_battery().secsleft / 60, 0)} minutos"]
        ]

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
        bateria += f"\033[1mMinutos Restantes:\033[0m {round(psutil.sensors_battery().secsleft / 60, 0)} minutos\n"
        
        if psutil.sensors_battery().power_plugged:
            bateria += "\033[1mEstá Carregando?\033[0m Sim\n"
        else:
            bateria += "\033[1mEstá Carregando?\033[0m Não"

        return bateria

def getTemperatura():
    return psutil.sensors_temperatures()

def main():
    dictFunctions = {'2': getProcessador, '3': getMemoriaRAM, '4': getMemoriaInterna, '5': getOS, '6': getRede, '7': getBateria, '8': getTemperatura, '9': relatorio.createRelatorio}
    index = 0

    while index != '8':
        os.system('cls')
        index = input("\033[1mHardware Data\033[0m\n\n[1] - Estatísticas em tempo real\n[2] - Processador\n[3] - Memória RAM\n[4] - Memória Interna\n[5] - Sistema Operacional\n[6] - Rede\n[7] - Bateria\n[8] - Temperatura\n[9] - Relatório\n[10] - Sair\n\n\033[1mUsuário:\033[0m ")
        os.system('cls')
        if int(index) > 0 and int(index) < 10:
            print('Buscando dados...')
        try:
            if index == '10':
                os.system('cls')
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
{a}{tracos}              {tracos}{b}
\n
{a}{tracos} MEMÓRIA RAM {tracos}
{a}Uso da Memória RAM:{b} {psutil.virtual_memory().percent}% ({round(psutil.virtual_memory().used / 1024 ** 3, 1)}GB/{round(psutil.virtual_memory().total / 1024 ** 3, 1)}GB)
{a}{tracos}             {tracos}{b}
\n
{a}{tracos} MEMÓRIA INTERNA {tracos}
{str(getMemoriaInternaLive())}
{a}Espaço no Disco Rígido:{b} {round(shutil.disk_usage("/").total / 1024 ** 3, 1)} GB
{a}Espaço Usado:{b} {round(shutil.disk_usage("/").used / 1024 ** 3, 1)} GB
{a}Espaço Livre:{b} {round(shutil.disk_usage("/").free / 1024 ** 3, 1)} GB
{a}Porcentagem de Uso:{b} {round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)}%
{a}{tracos}                 {tracos}{b}
\n
{a}{tracos} REDE {tracos}{b}
{a}Qtd. Dados Enviados:{b} {round(psutil.net_io_counters()[0] * 10 ** -9, 3)} GB
{a}Qtd. Dados Recebidos:{b} {round(psutil.net_io_counters()[1] * 10 ** -9, 3)} GB
{a}Pacotes Enviados:{b} {psutil.net_io_counters()[3]}
{a}Pacotes Recebidos{b} {psutil.net_io_counters()[4]}
{a}Endereço IP{b} {psutil.net_if_addrs()['Ethernet'][1][1]}
{a}Máscara da Rede{b} {psutil.net_if_addrs()['Ethernet'][1][2]}
{a}{tracos} {tracos}{b}
\n
{a}{tracos} BATERIA {tracos}
{str(getBateriaLive())}
{a}{tracos}         {tracos}{b}
\n
""")
                    time.sleep(1)
                    os.system('cls')
        except:
            main()
        input('\nPressione enter para voltar ao menu...\n\n')

os.system('cls')
main()