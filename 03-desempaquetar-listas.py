numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#feo
#primero = numeros[0]
#primero = numeros[1]
#primero = numeros[2] 

#lindo
primero, *otros, ultimo  = numeros # *esto para solo llamar a un numero de la lista
print(primero, ultimo, otros)
