from FraccionConOperadores import *
#obtener fracciones
print("suma y mayor de fracciones a/b y c/d")
def leer(x): return int(input(x))
f1=Fraccion(leer("a?"),leer("b?"))
f2=Fraccion(leer("c?"),leer("d?"))
#calcular y mostrar suma
f=f1+f2
print("suma="+str(f))
#mostrar fraccion mayor
if f1>f2:
  print("mayor="+str(f1))
else:
  print("mayor="+str(f2))
