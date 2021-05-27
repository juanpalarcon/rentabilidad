import sys

# entradas
precio = int(sys.argv[1])
num_usuarios = int(sys.argv[2])
gastos = int(sys.argv[3])
utilidades_anterior = ""
try:
    utilidades_anterior = int(sys.argv[4])
except IndexError:
    utilidades_anterior = 1000


utilidad_actuales= precio*num_usuarios-gastos
utilidades_tax = utilidad_actuales-utilidad_actuales*0.35
razon_utilidades = float(utilidades_tax/utilidades_anterior)
porcentajes_razon_utilidades= razon_utilidades*100


# salidas  
if porcentajes_razon_utilidades > 0.1:
    print("La razon de utilidad es este año es de :" + str(round(porcentajes_razon_utilidades,3)) + "%")
else:
    print("La razon de utlidad muestra una reduccion de :" + str(round(porcentajes_razon_utilidades,3)) + "%")









