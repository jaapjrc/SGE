import random

def main():
    secreto = random.randint(1, 10)
    
    solucion = int(input("Introduce un número del 1 al 10 "))
    
    while (solucion != secreto):
        if (solucion > secreto):
            print("El número secreto es menor")
            solucion = int(input("Introduce un número del 1 al 10 "))
        else:
            print("El número secreto es mayor")
            solucion = int(input("Introduce un número del 1 al 10 "))
            
    print("Has adivinado el número")

if __name__ == "__main__":
    main()