#tupla es lo mismo que una lista solo que no puedes eliminar ni modificar ni agregar elementos
numeros = (1, 2, 3) +(4, 5, 6)
print(numeros)


punto = tuple([1, 2])#lista convertida en tupla
print(punto)

#menosNumeros = numeros[1:3]
#print(menosNumeros)

primero, segundo, *otros =numeros#desmpaquetar 
print(primero, segundo, otros)#desempaquetar
for n in numeros:#para llamar cada numero en su linea
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "la katiuska"
print(listaNumeros) #aqui para modificar tienes que hacer una lista y modificar dicha para poder modificarla entrando al indicecon []