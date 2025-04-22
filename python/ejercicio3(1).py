numero = int (input("ingresa un numero"))
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else: 
        return "inpar"

resultado = es_par_o_impar (numero)
print(f"el numero {numero} es {resultado}")

