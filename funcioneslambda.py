from funciones1nivel import sumaTodos 

 #cubo = lambda x: x**3 se podria poner asi y solo poner cubo en la funcion
doble = lambda x : x*2
print (sumaTodos(3,lambda x: x**3)) #(**) es igual a elevado a
print (sumaTodos(3, doble))
# lambda es como se llama a una funcion anonima donte tu pones lo que quieras
#se usa poniendo lambda, espacio, parametros, separados por comas, dos puntos, bloque de codigo definido (sin return)