redondear={
    "numero1":25.6,
    "numero2":26.7,
    "numero3":27.5
}
valores=map(lambda valor:(valor[0],round(valor[1])),redondear.items())
print(dict(valores))