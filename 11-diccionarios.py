#diccionarios una coleccion de datos que se encuentra agrupados por una llave y un valor

punto = {"x":25, "y":50, "ami":49}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
#print(punto,punto["ami"])
if "ami" in punto:
    print( punto ["ami"])

print(punto.get("ami0", 97))

del punto["z"]
del(punto["y"])

for valor in punto:
    print(valor,punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave,valor)  

usuarios =[

    {"id":1,"nombre":"ami"},
    {"id":2,"nombre":"inay"},
    {"id":3,"nombre":"andi"},
    {"id":4,"nombre":"ñiñi"},

]
for usuario in usuarios:
    print(usuario ["nombre"])

