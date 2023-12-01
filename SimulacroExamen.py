#Ejercicio 1
def multiplosDe3y4(lista):
    resultado = []
    for n in lista:
        if n % 3 == 0 and n % 4 == 0:
            resultado.append(n)
    return resultado
            
lista = [36,25,32,48,127]
print(multiplosDe3y4(lista))

#Ejercicio 2
def mundialFutebol():
    rivales = ["Costa Rica", "Alemania", "Japón"]
    golesAFavor = [7,1,2]
    golesEnContra = [0,1,0]
    resultado = f"Partidos jugados: {len(rivales)}"
    
#Ejercicio 3
def addDiccionario():
    capitales={"España":"Madrid","Italia":"Roma","Francia":"París"}
    pais = input("Introduce el nombre de un país: ")
    capital = input("Introduce la capital del país: ")
    capitales[pais]=capital
    resultado = ""
    for key,value in capitales.items():
        resultado = resultado + f"{value} capital de {key}" + "\n"
    return resultado


print(addDiccionario())

#Ejercicio 4
def addDiccionarioBucle():
    capitales={"España":"Madrid","Italia":"Roma","Francia":"París"}
    pais = input("Introduce el nombre de un país (0 para parar la ejecucción del programa): ")
    capital = input("Introduce la capital del país (0 para parar la ejecucción del programa): ")
    resultado = ""
    while pais != "0" and capital != "0":
        capitales[pais]=capital
        pais = input("Introduce el nombre de un país (0 para parar la ejecucción del programa): ")
        capital = input("Introduce la capital del país (0 para parar la ejecucción del programa): ")
    for key,value in capitales.items():
        resultado = resultado + f"{value} capital de {key}" + "\n"
    return resultado


print(addDiccionarioBucle())