import psutil


tempo = psutil.sensors_battery().secsleft
minutos = round((tempo/60), 1)
horas = round((minutos/60), 1)

print(tempo)
print(minutos)
print(horas)
 
