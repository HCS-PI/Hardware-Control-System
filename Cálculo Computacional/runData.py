import dbFunctions, psutil, cpuinfo, platform, shutil, time, os,platform


if platform.system() == 'Linux':
  limpar = 'clear';
else:
  limpar  = 'cls';

def start():
    os.system(limpar)
    
    placa = 'ABC1234'
    modelo = 'Model X'
    idCliente = 15000
    idEmpresa = 5000

    dados = dbFunctions.select(f"SELECT * FROM carro WHERE placaCarro = '{placa}';")

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

        dbFunctions.insert(f"""INSERT INTO Carro VALUES('{placa}', '{modelo}', '{processador}', '{qtdNucleos}', '{qtdNucleosLogicos}', '{maxFrequencia}',
        '{qtdMemoriaRAM}', '{qtdMemoriaInterna}', '{sistemaOperacional}', '{enderecoIP}', '{mascara}', '{idCliente}', '{idEmpresa}');""")
