numeros = input("Digite uma lista de números separados por virgula:")
numeros_lista = numeros.split(",")
soma = 0

for numeros in numeros_lista:
    if int(numeros) % 2 == 1:
        soma += int(numeros)
print("A soma de todos números impares é:",soma)