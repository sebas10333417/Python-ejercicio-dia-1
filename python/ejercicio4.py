Pass="python123"

cont=1

nombre=input("ingresar contraseña")

while Pass!=nombre and cont<=3:

          nombre=input("ingresar contraseña") 

          cont=cont+1

if cont<=3:

          print("acceso permitido")

else:

          print("acceso denegado")

print("llegaste a la vez",cont)