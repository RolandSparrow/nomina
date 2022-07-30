from ast import If
import re


print ("MENU Registros\n\n 1)-Nuevo\n 2)-Mostrar")

opcion = input("Elije una opcion: ")

if opcion == "1":
    print ("nuevo registro\n")
    archiv = open('empleados.txt','a')

    
    print('ponga su informacion')
 

    documento = str ( input ("Numero de Documento: " ))
    nombre = re.findall ("[a-zA-Z]", input ("Nombres: " ))  
    apellidos =  re.findall ("[a-zA-Z]", input ("Apellidos: " )) 
    salario = int (input("Digite su salario minimo: " ))
    dias = int (input('¿Cuantos dias trabajo?:'))


    smlv = 1000000
    sub = 117100
    descuento_s = 4
    descuento_p = 4


    valor_dia = salario/30
    valor_total_dia = int (valor_dia * dias)
    valor_total_sub = sub * dias / 30
    valor_descuento_s = salario * 0.04
    valor_descuento_p = salario * 0.04
    valor_total = valor_total_dia + valor_total_sub - valor_descuento_s - valor_descuento_p

    print ("usuario", nombre, apellidos, " con numero de documento", documento)
    print ("Su salario es de: ", salario)
    print ("El valor del subsidio de transporte es de: ", sub)
    print ("la cantidad de dias que trabajo es de: ",dias )
    print ("El valor de los dias trabajados: ", valor_total_dia)
    print ("El valor actual del subsidio es de: ", sub)
    print ("Su valor del subsidio de transporte es de: ", valor_total_sub)
    print ("El valor de salud es de: ", valor_descuento_s)
    print ("El valor de pensión es de: ", valor_descuento_p)
    print ("Tu total es: ", valor_total)

    archiv.write(documento)
    archiv.write(",")
    archiv.write(nombre)
    archiv.write(",")
    archiv.write(apellidos)
    archiv.write(",")
    archiv.write(salario)
    archiv.write(",")
    archiv.write(dias)

    archiv.close()

elif opcion == "2":
    print ("Mostrar Registros")
    archiv = open("empleados.txt")

    print (archiv.read())

    archiv.close()
else:
    print ("dedes elegir una opcion anterior")
