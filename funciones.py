def saludar(nombre, saludo="Hola", pais="España"):
    print(saludo,nombre,pais)
    
saludar("Andrea")
saludar("Gabriel", "Buenos días")
saludar("José Antonio", pais="Mozambique")

def calculaIVA(precio, IVA=0.21):
    importeIVA = precio*IVA
    return round(importeIVA, 2)
print("El importe del IVA es", calculaIVA(57, 0.21))

def precioFinal(precio, IVA=1.21):
    precioFinal= precio*IVA
    return round(precioFinal, 2)
print("El importe total es", precioFinal(57))