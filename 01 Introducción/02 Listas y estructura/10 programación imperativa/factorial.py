#factorial: int -> int
#factorial de n>=0 como n*(n-1)*...*1
#ej: factorial(4)->24, factorial(0)->1
def factorial(n):
    assert type(n)==int and n>=0
    producto=1                
    while n>0:         
        producto = producto * n
        n = n - 1
    return producto
assert factorial(4)==24
assert factorial(0)==1
