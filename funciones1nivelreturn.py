

def maximo(*l):   
    if len(l) == 0:  
        return 0
    
    m = l[0]
    for ix in range (1, len(l)):
        if l[ix]> m:
            m = l[ix]
    return m
   # De esta forma coge los parametros separados por comas que le das y los convierte en un array

def minimo(*l):   
    if len(l) == 0:  
        return 0
    
    m = l[0]
    for ix in range (1, len(l)):
        if l[ix]< m:
            m = l[ix]
    return m
def media(*l):   
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
            
    return suma / len(l)

funciones = {
    'max': maximo,
    'min': minimo,
    'med': media }

def returnF(nombre):
    if nombre.lower() in funciones.keys():
        return funciones[nombre]  #devuelve el valor de nobre de funciones o maximo o minimo o media, devuelve una funcion
#devuelve una funcion y si metes los datos de la funcion te hace lo q diga la funcion
#funcion que devuelve funcion
    return None
