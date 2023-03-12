#set significa grupo o conjunto
primer ={1,2,2,3,4,4}
segundo = [3, 4, 5]#convirtiendo una lista en un set
segundo = set(segundo)#convirtiendo una lista en un set


#print(primer | segundo)#uniendo set al ser un set elimina los elementos repetidos
#print(primer & segundo)#para que te muestre la "interseccion" con el & en este caso es 3-4
#print(primer - segundo)#diferencia elimina los elemento del segundo valor al primero  en este caso entrega los numeros {1,2}
print(primer ^ segundo ) #diferencia simetrico entrega los que se encuentre en el primero y el segundo pero que no se encuentren en uno y el otro en este caso es 1 2 5

if 3 in segundo:
    print("hola bish")

#primer.add(5)
#primer.remove(1)
#print(primer)
