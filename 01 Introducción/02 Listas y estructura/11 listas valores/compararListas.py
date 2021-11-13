#compararListas: list list -> int
#-1 si X<Y, 0 si X=Y, 1 si X>Y
#ej: compararListas([1,2,3],[2,3]) -> -1
#    compararListas([2,3],[1,2,3]) -> 1
#    compararListas([2,3],[2,3]) -> 0
def compararListas(X,Y):
    assert type(X)==list and type(Y)==list
    for i in range(min(len(X),len(Y))):
        if X[i] < Y[i]: return -1
        if X[i] > Y[i]: return 1
    if len(X)<len(Y): return -1
    if len(X)>len(Y): return 1
    return 0
    return len(X)-len(Y)
assert compararListas([1,2,3],[2,3]) == -1
assert compararListas([2,3],[1,2,3]) == 1
assert compararListas([2,3],[2,3]) == 0
