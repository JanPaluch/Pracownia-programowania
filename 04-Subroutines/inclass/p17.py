def diffrent():
    n1=int(input("Podaj liczbę: "))
    n2=int(input("Podaj liczbę drugą: "))
    n3=int(input("Podaj liczbę trzecią: "))
    if n1==n2==n3:
        return (f"Numbers {n1}, {n2} and {n3} are the same")
    else:
        return (f"Numbers {n1}, {n2} and {n3} are diffrent")



print(diffrent())
