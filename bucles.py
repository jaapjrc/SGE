def barSinso():
    for i in range(0,10):
        print("Hoy me voy a portar bien en clase")
        
barSinso()

def numeros1en1():
    i = 1
    for n in range(0,100):
        print(i);
        i += 1
        
numeros1en1()

def numeros5en5():
    i = 0
    for n in range(0,20):
        i += 5
        print(i);
        
numeros5en5()

def numeros10al1():
    i = 10
    for n in range(0,10):
        print(i)
        i -= 1
        
numeros10al1()

def tablaMultiplicar():
    i = int(input("Introduce un número del 1 al 10 "))
    for n in range(0,11):
        print(i * n)
        
tablaMultiplicar()

def sumaNumeros():
    userInput = int(input("Introduce un número (0 para detener el programa): "))
    suma = 0
    
    while (userInput != 0):
        suma += userInput
        userInput = int(input("Introduce un número (0 para detener el programa): "))
    
    print(suma)
    
sumaNumeros()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    

n = int(input("Introduce un número para calcular su factorial: "))    
print(factorial(n))

def numerosNegativos():
    for n in range(0,5):
        userInput = int(input("Introduce un número para comprobar si es negativo:"))
        if userInput < 0:
            print("El número es negativo")
            
numerosNegativos()

def mayor():
    userInput = int(input("Introduce un número (0 para detener el programa): "))
    mayor = 0
    
    while (userInput != 0):
        if userInput > mayor:
            mayor = userInput
        userInput = int(input("Introduce un número (0 para detener el programa): "))
    
    print(mayor)
    
mayor()

def listaNumeros():
    lista = []
    for n in range(0,4):
        userInput = int(input("Introduce un número para añadir a la lista:"))
        lista.append(userInput)
    print(lista)
            
listaNumeros()

    
