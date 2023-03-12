#manipulando listas 
mascotas = ["pulgas", "pelusa", "copito", "mechi", "pancito"]
print(mascotas[2])
mascotas[2] = "molotov"
#print(mascotas)
#print(mascotas[2:])#AQUI SE UTILIZA EL : PARA LLAMAR DE UNA PARTE DE 
#LA LISTA A OTRA EN ESTE CASO SERIA DESDE EL STRING 2 AL X
#print(mascotas[-3])
#AQUI TE DEVUELVES Y TE LLAMA EL STRING QUE ESTE EN ESE LUGAR EN ESTE CASO ES MOLOTOV 
#print(mascotas[1::2])
#con el ::te dice salte uno los valores expresan de donde a donde , en este caso vas desde 
#pelusa y mechi saltanto a copito  

numeros = list(range(21))
print(numeros[::2])
print(numeros[1::2])