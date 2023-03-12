#ordenando listas
numeros = [2, 5, 3, 24, 16, 65, 42, 100]  

#numeros.sort() ordena la lista de numeros menor a mayor
#numeros.sort(reverse=True) ordena la lista de numeros mayor a menor
numeros2 = sorted(numeros)#sorted te entrega una nueva lista ordenada de menor a mayor
#numeros2 = sorted(numeros, reverse=True) te entrega una nueva lista ordenada de menor a mayor
print(numeros)
print(numeros2)

usuarios = [["ami", 4],
            ["copin", 2 ],
            ["andy", 10]
]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=lambda elemento:elemento[1],reverse=True)
print(usuarios)
