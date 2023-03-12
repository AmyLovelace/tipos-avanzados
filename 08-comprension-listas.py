usuarios = [["ami", 4],
            ["copin", 2 ],
            ["andy", 10]
]

#nombres = []
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)

#map
#nombres = [usuario[0] for usuario in usuarios]#aqui le indicas que quieres llamar al indice 0 de cada usuario , osea su nombre

#filtrar /filter
#nombres = [usuario for usuario in usuarios if usuario[1]> 2]#asi puedes filtrar elementos dentro de la lista
#nombres = [usuario[0] for usuario in usuarios if usuario[1]> 2]#asi puedes transformar y filtrar la lista



#nombres = list(map(lambda usuario: usuario [], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(menosUsuarios)
