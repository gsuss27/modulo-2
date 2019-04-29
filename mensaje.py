def esdecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
def validacion(mensaje):
    num = input(mensaje)
    while not esdecimal(num):
        print(num," Debe ser un numero")
        num = input(mensaje)
    return num
  
  
numh = validacion("Introduzca la altura: ")
numb = validacion("Introduzca la base: ")


altura = float(numh)
base = float(numb)


area=(base*altura)/2
print("El area es:", round(area,2))