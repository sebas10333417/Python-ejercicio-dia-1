TotalCuenta = float(input("El total de la cuenta es: "))
TotalUsuario1 = int(input("Que porcentaje deseas incluir en el servicio - 10, 15 , 20? "))
propina = TotalCuenta * (TotalUsuario1 / 100 )
print(f"la propina es: ${propina: .2f}")


