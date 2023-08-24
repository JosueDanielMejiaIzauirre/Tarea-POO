#Ejercicio 1 de la seccion 3.11

#Pide las horas de trabajo
print("Introduzca Horas: ")
horas = int(input())

#Pide la Tarifa
print("Introduzca Tarifa: ")
tarifa = int(input())


#Cacular el salario
if horas>40:
    
    normal = 40*tarifa
    extra = (horas-40)*(tarifa*1.5)

    salario = normal + extra

    #Resultado
    print("Su salario final es ", salario)

else:
    salario = horas * tarifa
    #Resultado
    print("Su salario final es ",salario)