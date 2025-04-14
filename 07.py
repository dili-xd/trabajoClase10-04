palabras=["Dilii","Dilana","Ruth"]
filtrar=filter(lambda palabra:len(palabra)>=5,palabras)
print(list(filtrar))