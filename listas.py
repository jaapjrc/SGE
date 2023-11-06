def main():
    classmates = ["Gabriel", "Pablou", "Daniel", "Andrea", "Javi"]
    classmates.insert(2, "Jean Carlos")
    classmates.sort()
    classmates.append("Antonio")
    classmates.append("Rigoberta")
    print(classmates.index("Antonio"))
    classmates.sort()
    classmates.insert(classmates.index("Rigoberta") + 1, "Merche")
    print(classmates)
    for x in classmates:
        print(x + " posicion: " + str(classmates.index(x)))

if __name__ == "__main__":
    main()

