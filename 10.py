nombres= [("Juan", 25), ("Ana", 20), ("Luis", 30)]
lista=sorted(nombres,key=lambda edad:edad[1])
print(list(lista))