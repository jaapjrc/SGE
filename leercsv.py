def obtenerCSV_como_diccionario(nombre_archivo):
    separador = ","
    archivo = open(nombre_archivo, encoding="utf-8")
    next(archivo)
    palabras = []
    for linea in archivo:
        linea = linea.rstrip("\n")
        columnas = linea.split(separador, 2)
        palabra = columnas[0]
        tipo = columnas[1]
        significado = columnas[2]
        palabras.append({
            "palabra" : palabra,
            "tipo" : tipo,
            "significado" : significado,
        })
    return palabras

def main():
    palabras = obtenerCSV_como_diccionario("basicdic.csv")
    for palabra in palabras:
        palabra = palabra["nombre"]
        tipo = tipo["tipo"]
        significado = significado["significado"]
        print(f"Palabra: {palabra}, Tipo: {tipo}, Significado: {significado}")
        

if __name__ == "__main__":
    main()