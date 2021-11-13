#factorial: int -> int
#factorial de n>=0 como 1*2*...*n
#ej: factorial(4)->24, factorial(0)->1
def factorial(n):
    assert type(n)==int and n>=0
    f=1
    i=1
    while i<=n:
        f = f * i
        i=i+1
    return f
assert factorial(4)==24
assert factorial(0)==1
