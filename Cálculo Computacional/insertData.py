import dbFunctions, psutil, shutil, time, os

os.system('cls')
    
placa = 'ABC1234'
modelo = 'Model X'
idCliente = 15000
idEmpresa = 5000

dados = dbFunctions.select(f"SELECT * FROM carro WHERE placaCarro = '{placa}';",True)

if dados:
    while True:
        os.system('cls')
        print('Inserindo dados...')
        usoProcessador = psutil.cpu_percent()
        usoMemoriaRAM = psutil.virtual_memory().percent
        usoMemoriaInt = round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)
        qtdDadosRec = round(psutil.net_io_counters()[0] * 10 ** -9, 3)
        qtdDadosEnv = round(psutil.net_io_counters()[1] * 10 ** -9, 3)
        qtdPacotesEnv = psutil.net_io_counters()[3]
        qtdPacotesRec = psutil.net_io_counters()[4]

        if not (str(psutil.sensors_battery()) == 'None'):
            qtdBateria = psutil.sensors_battery().percent
            estaConectada = psutil.sensors_battery().power_plugged

            dbFunctions.insert(f"""INSERT INTO medidas VALUES(NULL, {usoProcessador}, {usoMemoriaRAM}, {usoMemoriaInt}, {qtdDadosRec}, {qtdDadosEnv}, 
            {qtdPacotesEnv}, {qtdPacotesRec}, {qtdBateria}, {estaConectada}, '{placa}');""")
        else:
            dbFunctions.insert(f"""INSERT INTO medidas VALUES(NULL, {usoProcessador}, {usoMemoriaRAM}, {usoMemoriaInt}, {qtdDadosRec}, {qtdDadosEnv}, 
            {qtdPacotesEnv}, {qtdPacotesRec}, NULL, NULL, '{placa}');""")
        
        print('Dados Inseridos')
        time.sleep(4)
        os.system('cls')
        print('Inserção Pausada')
        time.sleep(26)
else:
    print('O carro não está registrado!')
    