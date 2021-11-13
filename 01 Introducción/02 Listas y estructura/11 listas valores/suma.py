
#suma: list(num) -> num
#suma de numeros de lista L
#ej: suma([20,30,10])->60
def suma(L):
    assert type(L)==list
    s=0
    for numero in L:
        s += numero #s=s+numero
    return s
assert suma([20,30,10])==60
