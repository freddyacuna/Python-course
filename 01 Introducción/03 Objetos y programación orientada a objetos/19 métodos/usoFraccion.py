from Fraccion import *
#obtener fracciones
print("suma y mayor de fracciones a/b y c/d")
def leer(x): return int(input(x))
f1=Fraccion(leer("a?"),leer("b?"))
f2=Fraccion(leer("c?"),leer("d?"))
#calcular y mostrar suma
f=f1.sumar(f2) 
print("suma="+f.aString())
#mostrar fraccion mayor
if f1.comparar(f2)>0:
  print("mayor="+f1.aString())
else:
  print("mayor="+f2.aString())
