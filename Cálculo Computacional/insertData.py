import dbFunctions, psutil, shutil, time, os, getmac, platform

def startInsert():
    enderecoMAC = getmac.get_mac_address()
    placa = 'ABC1234'
    modelo = 'Model X'
    idCliente = 15000
    idEmpresa = 5000

    dados = dbFunctions.select(f"SELECT * FROM carro WHERE enderecoMac = '{enderecoMAC}';", True)

    if dados:
        while True:
            usoProcessador = psutil.cpu_percent()
            usoMemoriaRAM = psutil.virtual_memory().percent
            usoMemoriaInt = round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)
            qtdDadosRec = round(psutil.net_io_counters()[0] * 10 ** -9, 3)
            qtdDadosEnv = round(psutil.net_io_counters()[1] * 10 ** -9, 3)
            qtdPacotesEnv = psutil.net_io_counters()[3]
            qtdPacotesRec = psutil.net_io_counters()[4]

            if str(psutil.sensors_battery()) == 'None':
                dbFunctions.insert(f"""INSERT INTO medidas VALUES(NULL, {usoProcessador}, {usoMemoriaRAM}, {usoMemoriaInt}, {qtdDadosRec}, {qtdDadosEnv}, 
                {qtdPacotesEnv}, {qtdPacotesRec}, NULL, NULL, NOW(), '{enderecoMAC}');""")
            else:
                qtdBateria = psutil.sensors_battery().percent
                estaConectada = psutil.sensors_battery().power_plugged

                dbFunctions.insert(f"""INSERT INTO medidas VALUES(NULL, {usoProcessador}, {usoMemoriaRAM}, {usoMemoriaInt}, {qtdDadosRec}, {qtdDadosEnv}, 
                {qtdPacotesEnv}, {qtdPacotesRec}, {qtdBateria}, {estaConectada}, NOW(), '{enderecoMAC}');""")

            time.sleep(4)
            time.sleep(26)
    else:
        print('O carro não está registrado!')