import src.dbFunctions as dbFunctions, psutil, cpuinfo, platform, shutil, os, platform, getmac, socket, ipaddress
limpar = 'clear' if platform.system() == 'Linux' else 'cls'

def start():
    os.system(limpar)
    
    enderecoMAC = getmac.get_mac_address()
    placa = 'ABC1234'
    modelo = 'Model X'
    idCliente = 15000
    idEmpresa = 5000

    dados = dbFunctions.select(f"SELECT * FROM Carro WHERE enderecoMac = '{enderecoMAC}';")

    if not dados:
        processador = cpuinfo.get_cpu_info()['brand_raw']
        qtdNucleos = psutil.cpu_count(logical=False)
        qtdNucleosLogicos = psutil.cpu_count(logical=True)
        maxFrequencia = psutil.cpu_freq().max
        qtdMemoriaRAM = round(psutil.virtual_memory().total / 1024 ** 3, 1)
        qtdMemoriaInterna = round(shutil.disk_usage("/").total / 1024 ** 3, 1)
        sistemaOperacional = f"{platform.system()} {platform.release()}"
        enderecoIP = socket.gethostbyname(socket.gethostname())
        mascara = ipaddress.IPv4Network(enderecoIP)

        dbFunctions.insert(f"""INSERT INTO Carro VALUES('{enderecoMAC}', '{placa}', '{modelo}', '{processador}', '{qtdNucleos}', '{qtdNucleosLogicos}', '{maxFrequencia}',
        '{qtdMemoriaRAM}', '{qtdMemoriaInterna}', '{sistemaOperacional}', '{enderecoIP}', '{mascara}', NOW(), {idCliente}, {idEmpresa});""")