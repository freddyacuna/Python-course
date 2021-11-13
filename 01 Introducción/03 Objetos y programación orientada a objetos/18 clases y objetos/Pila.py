#_L: list
class Pila:
    def __init__(self): self._L=[]
    def vaciar(self): self._L=[]
    def vacio(self): return self.__L==[]
    def poner(self,x): self._L.append(x)
    def sacar(self): return self._L.pop()
P=Pila(); P.poner(1); P.poner(2)
assert P.sacar()==2
class Cola(Pila):
    def sacar(self): return self._L.pop(0)
C=Cola(); C.poner(1); C.poner(2)
assert C.sacar()==1
