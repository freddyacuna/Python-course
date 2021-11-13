#esPrimo: int -> bool
#True si n>1 es primo
#ej: esPrimo(2)->True  (par primo)
#ej: esPrimo(6)->False (par no primo)
#ej: esPrimo(13)->True (impar primo)
#ej: esPrimo(9)->False (impar no primo)
def esPrimo(n):
  assert type(n)==int and n>1
  #primo par?
  if n==2: return True
  if n%2==0: return False
  #primo impar?
  divisor=3
  while divisor*divisor<=n :
      if n%divisor==0: return False
      divisor += 2
  return True
assert esPrimo(2)
assert not esPrimo(6)
assert esPrimo(13)
assert not esPrimo(9)
#siguientePrimo: int -> int
#primo siguiente a n
#ej: siguientePrimo(7)->11
def siguientePrimo(n):
    assert type(n)==int and n>=1
    if n%2==0:
        imparSgte=n+1
    else:
        imparSgte=n+2
    while not esPrimo(imparSgte):
        imparSgte += 2
    return imparSgte
assert siguientePrimo(7)==11
assert siguientePrimo(2)==3
#factoresPrimos: int ->
#escribe factores primos de n>=1
#ej: factoresPrimos(24) escribe 2**3 y 3**1
def factoresPrimos(n):
    assert type(n)==int and n>=1
    factor=2
    while n!=1:
        #calculo y escritura de potencia de factor primo
        p=0
        while n%factor==0:
            p +=1   
            n /= factor
        if p>0: print('factor:',factor,'potencia:',p)
        factor=siguientePrimo(factor)
#factoresPrimosRango: int int ->
#escribe factores primos de números entre x e y
#ej: factoresPrimosRango(25,30) escribe factores de 25,...,30
def factoresPrimosRango(x,y):
    assert type(x)==int and x>=2 and type(y)==int
    while x<=y:
        print('factores primos de',x)
        factoresPrimos(x)
        print()
        x += 1
#sonCoprimos: int int -> bool
#True si x e y no tienen divisores comunes
#ej: sonCoprimos(4,9)->True
#ej: sonCoprimos(18,24)->False
def sonCoprimos(x,y):
  assert type(x)==int and x>1
  assert type(y)==int and y>1
  assert x != y
  #maximo común divisor entre x e y
  while x != y:                   
     if x > y:                    
        x -= y                  
     else:                      
        y -= x 
  #son coprimos si máximo común divisor es 1                 
  return x == 1
assert sonCoprimos(4,9)
assert not sonCoprimos(18,24)
#coprimosEnRango: int int -> 
#escribe coprimos entre números x e y
#ej: coprimosEnRango(2,5) escribe 2 3,2 5,3 4,3 5,4 5
def coprimosEnRango(x,y):
    assert type(x)==int and x>1
    assert type(y)==int and y>1
    while x<y:
        #coprimos de x entre x+1 e y
        n=x+1
        while n<=y:
            if sonCoprimos(x,n): print(x,n)
            n += 1
        x += 1
          print('factores primos de',x)
        factoresPrimos(x)
        print()
        x += 1
#sonCoprimos: int int -> bool
#True si x e y no tienen divisores comunes
#ej: sonCoprimos(4,9)->True
#ej: sonCoprimos(18,24)->False
def sonCoprimos(x,y):
  assert type(x)==int and x>1
  assert type(y)==int and y>1
