def divisibleDe7():
    lista = []
    numero = 2000
    for n in range (0,1200):
        if numero % 7 == 0 and numero % 5 != 0:
            lista.append(numero)
        numero += 1
    lista_modificada = str(lista).replace('[', '').replace(']','')
    return lista_modificada

print(divisibleDe7())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def factorialConPasos(n):
    lista = []
    for i in range(1,n+1):
        lista.append(factorial(i))
    lista_modificada = str(lista).replace('[', '').replace(']','')
    return lista_modificada

print(factorialConPasos(8))

def generaDiccionario(n):
    dic = {}
    for i in range(1,n+1):
        dic[i]=i*i
    return dic

print(generaDiccionario(8))

def secuenciaNumeros():
    userInput = input("Introduce una cadena de números separados por coma: ").split(',')
    tupla = tuple(userInput)
    print(userInput, tupla)

secuenciaNumeros()

def secuenciaPalabras():
    userInput = input("Introduce una cadena de palabras separadas por coma: ")
    lista = userInput.split(',')
    lista.sort()
    lista_modificada = str(lista).replace('[', '').replace(']','').replace('\'','')
    print(lista_modificada)

secuenciaPalabras()

def toUpperCase():
    texto = ""
    userInput = input("Introduce una cadena de texto (cadena vacía para detener el programa): ")
    texto += userInput + " "
    while (userInput != ""):
        userInput = input("Introduce una cadena de texto (cadena vacía para detener el programa): ")
        texto += userInput + " "
    return(texto.upper())

print(toUpperCase())