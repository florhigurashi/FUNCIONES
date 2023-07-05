#Ejercicio 1: Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensaje a su elección

def saludo(aula1, aula2, aula3):
    
    print(f"Hola aula {aula1}, ¿Qué tal?, bienvenidos a nuestro instituto")
    print(f"Hola aula {aula2}, ¿Que tal?, queremos que se sientan parte")
    print(f"Hola aula {aula3}, ¿Qué tal?, los esperamos en despacho de alumnos para lo que necesiten")

saludo(1,2,3)
"""

#Ejercicio 2: A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.
"""
def saludo(nombre1, nombre2, nombre3):
    
    print(f"Hola {nombre1}, ¿Que tal?, buen comienzo de semana")
    print(f"Hola {nombre2}, ¿Qué tal?, no olvides revisar el clima antes de salir")
    print(f"Hola {nombre3}, ¿Qué tal?, disfruta tu dia como siempre")

saludo("Abi","Lau","Tami")
"""

#Ejercicio 3: Realice un programa de funciones que contengan 3 parámetros, el cual deriva en una suma. Mostrar el resultado dos veces.
"""
def sumar(num1, num2, num3):
    
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
    print(f"La suma de {num3} y {num2} es {num3 + num2}")

suma(21,10,84)
""" 


#Ejercicio 4 Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, muestre un mensaje que muestre TRUE.

"""
def comparar_numeros(num1, num2):
    
    if num1 == num2:
        return True
    else:
        return False

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = comparar_numeros(numero1, numero2)

print(resultado)

"""

#Ejercicio 5: Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resto, respectivamente. Recuerda: en estos ejercicios trabajaron argumentos para este ejercicio serían dos.
"""
def sumayresta (num1,num2):
    
    suma= num1+num2
    resta= num1-num2
    
    print (f"La suma de los numeros {num1} y {num2} es: {suma} ")
    print ( f"La resta de los numeros {num1} y {num2} es: {resta} ")

sumayresta (7,5)