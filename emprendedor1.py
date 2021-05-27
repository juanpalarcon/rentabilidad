
import sys
#entradas
precio = int(sys.argv[1]) #precio del producto
usuarios = int(sys.argv[2]) #numero de usuarios
gastos = int(sys.argv[3]) #gastos del año

utilidades =(precio*usuarios-gastos)
#Salidas
if utilidades >= 0:
    print("Las utilidades despues de impuestos son " + str(utilidades*0.65))
else:
    print("Se obtuvo perdidas de :" + str(utilidades) )

