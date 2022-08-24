import dbFunctions, psutil, cpuinfo, platform, shutil, time, os, platform, getmac

limpar = 'clear' if platform.system() == 'Linux' else 'cls'

def start():
    os.system('cls')
    
    enderecoMAC = getmac.get_mac_address()
    placa = 'ABC1234'
    modelo = 'Model X'
    idCliente = 15000
    idEmpresa = 5000

    dados = dbFunctions.select(f"SELECT * FROM carro WHERE enderecoMac = '{enderecoMAC}';")

    if dados:
        print('\033[1mSugestão:\033[0m Execute o arquivo de inserção de medidas\n\n')
        time.sleep(2)
    else:
        processador = cpuinfo.get_cpu_info()['brand_raw']
        qtdNucleos = psutil.cpu_count(logical=False)
        qtdNucleosLogicos = psutil.cpu_count(logical=True)
        maxFrequencia = psutil.cpu_freq().max
        qtdMemoriaRAM = round(psutil.virtual_memory().total / 1024 ** 3, 1)
        qtdMemoriaInterna = round(shutil.disk_usage("/").total / 1024 ** 3, 1)
        sistemaOperacional = f"{platform.system()} {platform.release()}"
        enderecoIP = psutil.net_if_addrs()['Ethernet'][1][1]
        mascara = psutil.net_if_addrs()['Ethernet'][1][2]

        dbFunctions.insert(f"""INSERT INTO Carro VALUES('{enderecoMAC}', '{placa}', '{modelo}', '{processador}', '{qtdNucleos}', '{qtdNucleosLogicos}', '{maxFrequencia}',
        '{qtdMemoriaRAM}', '{qtdMemoriaInterna}', '{sistemaOperacional}', '{enderecoIP}', '{mascara}', NOW(), {idCliente}, {idEmpresa});""")