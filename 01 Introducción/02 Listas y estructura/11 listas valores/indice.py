L=[8,9,7,9] 
#indice: any list -> int 
#indice de primer x en L (-1 si no está) 
#ej: indice(9,L)->1, indice(6,L)->-1 
def indice(x,L): 
    assert type(L)==list
    if x in L:     
        return L.index(x)   
    else:     
        return -1 
assert indice(9,L) == 1 
assert indice(6,L) == -1 
