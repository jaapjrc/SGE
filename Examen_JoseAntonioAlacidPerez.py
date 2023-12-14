#Ejercicio 13
def sumaMediaEdades(lista):
    suma = 0
    var = 0
    for i in lista:
        if i > 10 and i < 60:
            suma += i
            var += 1
    media = suma / var
    resultado = f"Suma: {suma} Media: {media}"
    return resultado
    
lista = [6,14,21,44,50,80]
print(sumaMediaEdades(lista))

#Ejercicio 14
def separarPalabra():
    palabra = input("Introduce una palabra: ")
    palabraSeparada = ""
    for i in palabra:
        palabraSeparada = palabraSeparada + i + " "
    return palabraSeparada

print(separarPalabra())

#Ejercicio 15
def mayorMenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
    resultado = f"Mayor: {mayor} Menor: {menor}"
    return resultado

print(mayorMenor(lista))

#Ejercicio 16
def addDiccionario():
    edades={"Antonio":"29","María":"19","Roberto":"21"}
    nombre = input("Introduce un nombre: ")
    edad = input("Introduce una edad: ")
    edades[nombre]=edad
    return edades


print(addDiccionario())

#Como no está explicado si tiene que ser ese diccionario o cualquiera aquí hay otro método con cualquiera

def addDiccionario(edades):
    nombre = input("Introduce un nombre: ")
    edad = input("Introduce una edad: ")
    edades[nombre]=edad
    return edades

edades={"Antonio":"29","María":"19","Roberto":"21"}
print(addDiccionario(edades))