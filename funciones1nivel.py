def normal(x):
    return x
def cuadrado(x):
    return x*x

def sumaTodos(limitTo, f):
    resultado=0
    for i in range (0, limitTo+1):  #llega solo hasta limitto x eso se pone mas 1 (el ultimo no lo cuenta)
        resultado+=f(i)   #busca el primer i y lo mete en la funcion y el valor que le da le suma
    return resultado

if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))



# subir archivos 1 git status 2 git add. 3 git -m "nombre archivo" 4 git push origin master