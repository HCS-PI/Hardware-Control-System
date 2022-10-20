import psutil

def dadosCPU():
    consumoCPU = psutil.cpu_percent(interval=None)
    nucleos = psutil.cpu_count(logical=False)
    processadoresLogicos = psutil.cpu_count() - psutil.cpu_count(logical=False);
    threads = psutil.cpu_count()

    print('=-='*50)
    print('=-='*50) 
    print('\033[1mDADOS DE CPU (PROCESSADOR)\033[0m\n')
    print(f'\033[1mConsumo(%): \033[94m{consumoCPU}%\033[0m     \033[1mNúcleos: \033[94m{nucleos}\033[0m      \033[1mProcessadores Lógicos: \033[94m{processadoresLogicos}\033[0m      \033[1mThreads: \033[94m{threads}\033[0m')
    print('=-='*50) 

def dadosRAM(): 
    consumoRam = psutil.virtual_memory()[2];
    memoriaRamTotal = round(psutil.virtual_memory()[0] / (10**9),2);
    memoriaRamEmUso = round(psutil.virtual_memory()[3] / (10**9),2);
    memoriaRamDisp = round(psutil.virtual_memory()[1] / (10**9),2);

    print('=-='*50) 
    print('\033[1mDADOS DE RAM (MEMÓRIA(S) RAM)\033[0m\n')
    print(f'\033[1mConsumo(%): \033[93m{consumoRam}%\033[0m     \033[1mCapacidade Total: \033[93m{memoriaRamTotal} Gb\033[0m      \033[1mEm Uso: \033[93m{memoriaRamEmUso} Gb\033[0m      \033[1mDisponível: \033[93m{memoriaRamDisp} Gb\033[0m')
    print('=-='*50)  

dispositivos = psutil.disk_partitions();
def dadosDisco(): 
    print('=-='*50)
    print('\033[1mDADOS DE UNIDADES DE ARMAZENAMENTO (DISCOS)\033[0m\n')
    for dispositivo in dispositivos:
        armzTotalDisco = round((psutil.disk_usage(f'{dispositivo.device}')[0]) / (10**9),2);
        espacoUsadoDisco = round((psutil.disk_usage(f'{dispositivo.device}')[1]) / (10**9),2);
        espacoLivreDisco = round((psutil.disk_usage(f'{dispositivo.device}')[2]) / (10**9),2);
        consumoDisco = round((psutil.disk_usage(f'{dispositivo.device}')[3]),2);

        print(f'\033[1mUnidade de Armazenamento: \033[95m{dispositivo.device}\033[0m   \033[1mEspaço Total: \033[95m{armzTotalDisco} Gb\033[0m   \033[1mEspaço Usado: \033[95m{espacoUsadoDisco} Gb\033[0m   \033[1mEspaço Livre: \033[95m{espacoLivreDisco} Gb\033[0m   \033[1mConsumo(%): \033[95m{consumoDisco}%\033[0m')
    print('=-='*50) 
    print('=-='*50)    