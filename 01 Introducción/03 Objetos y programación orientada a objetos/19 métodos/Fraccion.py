#atributos
#_ _numerador : int
#_ _denominador : int
class Fraccion:
    
  #__init__: int int -> Fraccion
  #crea Fraccion con numerador x  denominador y
  #devuelve referencia(dirección) a objeto
  #ej: f1=Fraccion(1,2), f2=Fraccion(1,3)
  def __init__(self,x,y):
      assert type(x)==int and type(y)==int and y!=0
      self.__numerador=x
      self.__denominador=y
      
  #aString: -> str
  #"numerador/denominador" de self
  #ej: f1.aString() -> '1/2'
  def aString(self):
      return str(self.__numerador)+ "/" + str(self.__denominador)
         
  #comparar: Fraccion -> int
  #0,<0,>0 si self ==,<,> fraccion x
  #ej: f1.comparar(f2)->n°
  def comparar(self,x):
    assert isinstance(x,Fraccion) #x es Fraccion?
    return self.__numerador * x.__denominador  \
         - self.__denominador * x.__numerador
  #sumar: Fraccion -> Fraccion
  # self + x
  #ej: f1.sumar(f2)->Fraccion(5,6)
  def sumar(self,x):
    assert isinstance(x,Fraccion) 
    num=self.__numerador * x.__denominador + \
        self.__denominador * x.__numerador
    den=self.__denominador * x.__denominador
    return Fraccion(num,den)
#test
f1=Fraccion(1,2)
assert f1.aString()=='1/2'
f2=Fraccion(1,3)
assert f1.comparar(f2)>0
assert f2.comparar(f1)<0
f3=f1.sumar(f2)
assert f3.comparar(Fraccion(5,6))==0
