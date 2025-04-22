NumeroSecreto = 7
Adivinanza = int(input("por favor ingresa el numero secreto del 1 al 10: "))
if Adivinanza == 7 :
    print("tu numero es correcto")
elif Adivinanza < NumeroSecreto:
    print("tu numero es inferior")
else:
    print(" tu numero es mayor")

