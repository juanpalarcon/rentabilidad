import sys
#entradas
precio = int(sys.argv[1]) #precio del producto
usuarios_totales = int(sys.argv[2]) #numero de usuarios totales
usuarios_premiun = int(sys.argv[3]) #numero de usuarios premiun pagan x2
usuarios_gratis = int(sys.argv[4]) # numero de usuarios gratuitos no pagan
gastos = int(sys.argv[5]) #gastos del año


usuarios_normales = usuarios_totales-usuarios_premiun-usuarios_gratis # funciona
ingresos_totales = (usuarios_normales*precio)+(usuarios_premiun*precio*2)  #ingreso total
uai =(ingresos_totales-gastos) #utilidad antes de impuesto
udi = uai-(uai*0.35) #utilidad despues de impuesto

#Salidas
if uai >= 0:
    print("Las utilidades sin impuestos son :" + str(uai))
    print("Las utilidades despues de impuestos son :" + str(udi))
else:
    print("Se obtuvo perdidas de :" + str(uai))



#funciona

