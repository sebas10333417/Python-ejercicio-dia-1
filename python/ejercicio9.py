año1 = int(input("Ingresa un año: "))
def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if es_bisiesto(año1):
    print(f"{año1} es un año bisiesto.")
else:
    print(f"{año1} no es un año bisiesto.")
