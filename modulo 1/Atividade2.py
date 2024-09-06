import random
lista_numeros = []
for i in range(10):
    lista_numeros.append(random.randint(1,100))

print("Lista de números:",lista_numeros)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print("Maior Número", maior_numero)
print("Menor Número",menor_numero)