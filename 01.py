lista_numeros=[1,2,3,4,5,6]
filtrado_pares=filter(lambda numero: numero % 2 == 0, lista_numeros)

print(list(filtrado_pares))