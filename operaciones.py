def main():
    nums = []
    for n in range(4):
        nums.append(int(input("Dime un número ")))
        
    operacion = input("Dime si quieres sumar (+) o multiplicar(*) ")
    
    if operacion == "+":
        total = 0
        for n in nums:
            total += n
        print("El total es", total)
    elif operacion == '*':
        total = 1
        for n in nums:
            total *= n
        print("El total es",total)
    else:
        print("Operación no contemplada")

if __name__ == "__main__":
    main()