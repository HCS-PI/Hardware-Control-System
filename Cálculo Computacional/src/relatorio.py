from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from datetime import datetime
from io import BytesIO
from svglib.svglib import svg2rlg
import cpuinfo, locale, psutil, os, matplotlib.pyplot as plt, shutil, socket, ipaddress, platform

limpar = 'clear' if platform.system() == 'Linux' else 'cls'
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def createRelatorio():
    os.system(limpar)
    print('Gerando...')
    c = canvas.Canvas(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/files/relatorio.pdf"))
    c.setTitle('Hardware Controll System - Relatório')
    c.drawImage(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/img/logo.png"), 75, 725, mask='auto')
    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 765, "Hardware Controll System")
    c.setFont('Helvetica', 18)
    c.drawString(320, 735, "Relatório")

    dt = datetime.now().strftime(f"%A, %d de %B de %Y - %H:%M:%S").capitalize()
    c.setFont('Helvetica-Bold', 18)
    c.drawString(75, 685, dt)
    c.drawString(75, 660, "Placa: ")
    c.setFont('Helvetica', 18)
    c.drawString(140, 660, "ABC-1234")

    # ------------------- Página 1 (PROCESSADOR) ------------------------------
    c.setFont('Helvetica-Bold', 20)
    c.drawString(75, 605, "Processador")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 580, "Modelo:") 
    c.setFont('Helvetica', 12)
    c.drawString(125, 580, f"{cpuinfo.get_cpu_info()['brand_raw']}")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 560, "Uso:") 
    c.setFont('Helvetica', 12)
    c.drawString(105, 560, f"{psutil.cpu_percent()}%")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 540, "Quantidade de Núcleos:")
    c.setFont('Helvetica', 12)
    c.drawString(215, 540, f"{psutil.cpu_count(logical=False)}")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 520, "Quantidade de Núcleos Lógicos:")
    c.setFont('Helvetica', 12)
    c.drawString(265, 520, f"{psutil.cpu_count(logical=True)}")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 500, "Frequência Máxima:")
    c.setFont('Helvetica', 12)
    c.drawString(195, 500, f"{psutil.cpu_freq().max}Ghz")

    j = 1
    k = 480

    cpus = psutil.cpu_percent(percpu=True)
    cpusN = []
    for i in cpus:
        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, k, f"CPUv {j}:")
        c.setFont('Helvetica', 12)
        c.drawString(125, k, f"{i}%")
        cpusN.append(f"CPUv {j}")
        j+=1
        k-=20

    plt.rcParams["figure.figsize"] = (5,3)
    plt.bar(cpusN, cpus, color="black")
    plt.ylim(1, 101)

    imgdata = BytesIO()
    plt.savefig(imgdata, format='svg', dpi=200, transparent=True)
    plt.close()
    imgdata.seek(0)
    drawing = svg2rlg(imgdata)
    renderPDF.draw(drawing, c, 75, 50)

    c.showPage()

    # ---------------------- Página 2 (MEMÓRIA RAM) ---------------------------

    c.drawImage(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/img/logo.png"), 75, 725, mask='auto')
    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 765, "Hardware Controll System")
    c.setFont('Helvetica', 18)
    c.drawString(320, 735, "Relatório")

    c.setFont('Helvetica-Bold', 20)
    c.drawString(75, 665, "Memória RAM")

    memoria = psutil.virtual_memory()
    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 635, "Quantidade de Memória:") 
    c.setFont('Helvetica', 12)
    c.drawString(220, 635, f"{round(memoria.total / 1024 ** 3, 1)} GBs")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 610, "Porcentagem de memória sendo usada:") 
    c.setFont('Helvetica', 12)
    c.drawString(310, 610, f"{memoria.percent}%")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 585, "Quantidade Usada:")
    c.setFont('Helvetica', 12)
    c.drawString(190, 585, f"{round(memoria.used / 1024 ** 3, 1)} GBs")

    plt.close()
    plt.rcParams["figure.figsize"] = (5,3)
    pct = round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)
    plt.pie([memoria.percent, 100-memoria.percent], labels=['Usado', 'Não Usado'], startangle=90,  colors=['black', 'lightgray'])
    plt.rcParams.update({'font.size': 10})

    imgdata = BytesIO()
    plt.savefig(imgdata, format='svg', dpi=200, transparent=True)
    imgdata.seek(0)
    drawing = svg2rlg(imgdata)
    renderPDF.draw(drawing, c, 75, 50)

    c.showPage()

    # ---------------------- Página 3 (MEMÓRIA INTERNA) ---------------------------

    c.drawImage(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/img/logo.png"), 75, 725, mask='auto')
    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 765, "Hardware Controll System")
    c.setFont('Helvetica', 18)
    c.drawString(320, 735, "Relatório")

    c.setFont('Helvetica-Bold', 20)
    c.drawString(75, 665, "Memória Interna")

    x = 635

    if platform.system() == 'Linux':
        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço no Disco Rígido:") 
        c.setFont('Helvetica', 12)
        c.drawString(220, x, f"{round(shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3, 1)} GB")
        x -= 25
        
        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço Usado:") 
        c.setFont('Helvetica', 12)
        c.drawString(165, x, f"{round(shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3, 1)} GB")
        x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço Livre:") 
        c.setFont('Helvetica', 12)
        c.drawString(160, x, f"{round(shutil.disk_usage('/home/hcs/Documentos').free / 1024 ** 3, 1)} GB")
        x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Porcentagem de Uso:") 
        c.setFont('Helvetica', 12)
        c.drawString(200, x, f"{round(((shutil.disk_usage('/home/hcs/Documentos').used / 1024 ** 3) * 100) / (shutil.disk_usage('/home/hcs/Documentos').total / 1024 ** 3), 1)}%")
        x -= 25        
    else:
        for i in psutil.disk_partitions():
            c.setFont('Helvetica-Bold', 12)
            c.drawString(75, x, "Dispositivo:") 
            c.setFont('Helvetica', 12)
            c.drawString(150, x, f"{i[0]}")
            x -= 25

            c.setFont('Helvetica-Bold', 12)
            c.drawString(75, x, "Tipo de Arquivo:") 
            c.setFont('Helvetica', 12)
            c.drawString(180, x, f"{i[2]}")
            x-=10
            c.drawString(75, x, "-"*100)
            x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço no Disco Rígido Principal:") 
        c.setFont('Helvetica', 12)
        c.drawString(275, x, f"""{round(shutil.disk_usage("/").total / 1024 ** 3, 1)} GBs""")
        x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço Usado no Disco Rígido Principal:") 
        c.setFont('Helvetica', 12)
        c.drawString(315, x, f"""{round(shutil.disk_usage("/").used / 1024 ** 3, 1)} GBs""")
        x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Espaço Livre no Disco Rígido Principal:") 
        c.setFont('Helvetica', 12)
        c.drawString(310, x, f"""{round(shutil.disk_usage("/").free / 1024 ** 3, 1)} GBs""")
        x -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, x, "Porcentagem de Uso do Disco Rígido Principal:") 
        c.setFont('Helvetica', 12)
        c.drawString(355, x, f"""{round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)}%""")
        x -= 25

        plt.close()
        plt.rcParams["figure.figsize"] = (5,3)
        pct = round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)
        plt.pie([pct, 100-pct], labels=['Usado', 'Não Usado'], startangle=90,  colors=['black', 'lightgray'])
        plt.rcParams.update({'font.size': 10})

    imgdata = BytesIO()
    plt.savefig(imgdata, format='svg', dpi=200, transparent=True)
    imgdata.seek(0)
    drawing = svg2rlg(imgdata)
    renderPDF.draw(drawing, c, 75, 50)

    c.showPage()

    # ---------------- Página 4 (REDE) --------------------
    c.drawImage(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/img/logo.png"), 75, 725, mask='auto')
    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 765, "Hardware Controll System")
    c.setFont('Helvetica', 18)
    c.drawString(320, 735, "Relatório")

    c.setFont('Helvetica-Bold', 20)
    c.drawString(75, 665, "Rede")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 635, "Quantidade de Dados Enviados:") 
    c.setFont('Helvetica', 12)
    c.drawString(265, 635, f"{round(psutil.net_io_counters()[0] * 10 ** -9, 3)} GBs")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 610, "Quantidade de Dados Recebidos:") 
    c.setFont('Helvetica', 12)
    c.drawString(275, 610, f"{round(psutil.net_io_counters()[1] * 10 ** -9, 3)} GBs")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 585, "Pacotes Enviados:") 
    c.setFont('Helvetica', 12)
    c.drawString(190, 585, f"{psutil.net_io_counters()[3]} pacotes")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 560, "Pacotes Recebidos:") 
    c.setFont('Helvetica', 12)
    c.drawString(195, 560, f"{psutil.net_io_counters()[4]} pacotes")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 535, "Endereço IP:") 
    c.setFont('Helvetica', 12)
    c.drawString(155, 535, f"{socket.gethostbyname(socket.gethostname())}")

    c.setFont('Helvetica-Bold', 12)
    c.drawString(75, 510, "Máscara de Rede:") 
    c.setFont('Helvetica', 12)
    c.drawString(185, 510, f"{ipaddress.IPv4Network(socket.gethostbyname(socket.gethostname()))}")

    plt.close()
    plt.rcParams["figure.figsize"] = (5,3)
    pct = round(((shutil.disk_usage("/").used / 1024 ** 3) * 100) / (shutil.disk_usage("/").total / 1024 ** 3), 1)
    plt.pie([round(psutil.net_io_counters()[0] * 10 ** -9, 3), 100-round(psutil.net_io_counters()[1] * 10 ** -9, 3)], labels=['Enviados', 'Recebidos'], startangle=90,  colors=['black', 'lightgray'])
    plt.rcParams.update({'font.size': 10})

    imgdata = BytesIO()
    plt.savefig(imgdata, format='svg', dpi=200, transparent=True)
    imgdata.seek(0)
    drawing = svg2rlg(imgdata)
    renderPDF.draw(drawing, c, 75, 50)

    c.showPage()

    # --------------- PÁGINA 5 (BATERIA) ------------------

    c.drawImage(str(os.path.abspath(os.path.join(__file__ ,"../..")) + "/assets/img/logo.png"), 75, 725, mask='auto')
    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 765, "Hardware Controll System")
    c.setFont('Helvetica', 18)
    c.drawString(320, 735, "Relatório")

    c.setFont('Helvetica-Bold', 20)
    c.drawString(75, 665, "Bateria")

    c.setFont('Helvetica-Bold', 12)

    if str(psutil.sensors_battery()) == 'None':
        c.drawString(75, 635, "Dispositivo não alimentado por bateria")
    else:
        c.drawString(75, 635, "Porcentagem de Bateria:") 
        c.setFont('Helvetica', 12)
        c.drawString(220, 635, f"{psutil.sensors_battery().percent}%")

        npo = 610
        if platform.system() != 'Linux':
            c.setFont('Helvetica-Bold', 12)
            c.drawString(75, 610, "Minutos Restantes:") 
            c.setFont('Helvetica', 12)
            c.drawString(190, 610, f"{round(psutil.sensors_battery().secsleft / 60, 0)} minutos")
            npo -= 25

        c.setFont('Helvetica-Bold', 12)
        c.drawString(75, npo, "Carregando:")
        c.setFont('Helvetica', 12)

        if psutil.sensors_battery().power_plugged:
            c.drawString(190, npo, "Sim")
        else:
            c.drawString(150, npo, "Não")
        
        plt.close()
        plt.rcParams["figure.figsize"] = (5,3)
        plt.pie([psutil.sensors_battery().percent, 100-psutil.sensors_battery().percent], labels=['Bateria Restante', ' '], startangle=90,  colors=['black', 'lightgray'])
        plt.rcParams.update({'font.size': 10})

        imgdata = BytesIO()
        plt.savefig(imgdata, format='svg', dpi=200, transparent=True)
        imgdata.seek(0)
        drawing = svg2rlg(imgdata)
        renderPDF.draw(drawing, c, 75, 50)

    c.showPage()
    c.save()
    os.system(limpar)
    return 'Relatório Gerado'