from functools import reduce
lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista) #con el map a cada uno de ellos se le hace la transformacion

listaPares = filter(lambda x: x % 2 == 0, lista)  #enseña solo los q cumplen con dicha condicion
                                                   # tambien se podrian cambiar el labda por funcion y el filter cambiarlo por una funcion
                                                   # si en el filter se introduce una funcion esta teine q devolver true o false
                                                   
sumatorio = reduce(lambda x, y: x + y ,lista)

def esPar(x):
    x % 2 == 0
    return True
listaPares= filter(esPar, listaDobles)

print(list(listaPares))
print(sumatorio)
print(list(listaDobles))