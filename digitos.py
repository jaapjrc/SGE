def menorDigitoString(numero):
    nums=str(numero)
    lista=[]
    for n in nums:
        lista.append(n)
        lista.sort(reverse=False)
    return lista[0]
    
print(menorDigitoString(239))

def ordenInverso(numero):
    numeroEnTexto=str(numero)
    numeroEnLista=[]
    for n in numeroEnTexto:
        numeroEnLista.append(n) 
    numeroEnLista.sort(reverse=True)
    return numeroEnLista
    
x=3825
print(ordenInverso(x))

def esCapicua(x):
    numero=str(x)
    longitud=len(numero)
    for n in range(0, longitud // 2):
        if numero[n] != numero[-(n+1)]:
            return False
        return True
    
print(esCapicua(1234321))
print(esCapicua(1234))

def suma(*numeros):
    valor = 0
    for n in numeros:
        valor += n
    return valor

print(suma(1,3,5))

def boletin(**asignaturas):
    for asignatura, nota in asignaturas.items():
        print(asignatura, nota)
        
boletin(mates=9, lengua=8)

def pares(*numeros):
    for n in numeros:
        if n % 2 != 0:
            return False
    return True

print(pares(1,2,3))
print(pares(2,4,6))

def menorDigito(*numeros):
    menor = numeros[0]
    for n in numeros:
        if n < menor:
            menor = n
    return menor

print(menorDigito(5,6,8,2))

def mejorNota(**notas):
    mejorNota = -1
    for alumno, nota in notas.items():
        if nota > mejorNota:
            mejorNota = nota
            mejorAlumno = alumno
    return mejorAlumno, mejorNota

print(mejorNota(Gabriel=9,Jose_Antonio=10,Andrea=6))

def creaSQL(**datos):
    texto="SELECT * FROM personas WHERE "
    for clave, valor in datos.items():
       if type(valor) != "str":
           texto += clave + "=" + str(valor) + " AND "
       else:
           texto += clave + "='" + valor +"' AND "
    texto=texto[0:-5] + ";"
    return texto

print(creaSQL(nombre="Gabriel",poblacion="Murcia",mote="Gaybriel"))