def probabilidad_simple():
    p=int(input("Sucesos favorables: "))
    q=int(input("Sucesos posibles: "))
    print(f"La probabilidad de que ocurra es {round(p/q*100,3)} %")