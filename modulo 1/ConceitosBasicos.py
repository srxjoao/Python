# Listas
nota1 = 7.5
nota2 = 9
nota3 = 5

listaNotas = [7.5,9,5]
listaNotas.append('João')
print(listaNotas)

# Tuplas
frutas = ('Banana','Maça')
print(frutas)

# Dicionário
dic = {'nome':'Rodrigo', 'sobrenome':'Duran' , 'formação':'Cientista da computação'}
dic['idade'] = 40
print(dic)
print(dic['formação'])

# Declaração de continua na próxima linha
calc = 2 + \
    5*3 
print(calc)

# Expressões Matemáticas
# * multiplicação
# + adição
# - subtração
# / divisão
# ** exponente
calc2 = (25/5) + 25 -13
print(calc2)

calcRaiz = 27 ** (1/3)
print(calcRaiz)

# Expressões Booleanas
# == igualdade
# > maior
# >= maior ou igual
# < menor ou igual
# != diferente geralmente if e else 

bolean = 52 != 25 
print(bolean)

# Estrutura Condicional,teremos conceito de blocos de informações
if 0 > 1:
    print('Condição Verdadeira')
else:
    print('Condição Falsa')

# IF encadeado
a = 2 
if a > 25:
    print('Eita é Verdade')
elif(a>5):
    print('Eita como é falsão')
elif a >25:
    print(a)
else:
    print('Nenhuma condição satisfeita')
    
# Estrutura de repetição
for x in range(10,15):
    print(x)

listaFrutas = ['morango','laranja','banana']
for i, fruta in enumerate(listaFrutas):
    print(i,listaFrutas)
    
# Funções e DocString
def soma_dois_valores (a:float,b:int) -> int:
    return a + b
soma = soma_dois_valores(10,85)
print(soma)

#Arquivos
f = open('test.txt','r')
f.write('Olá Mundo')
f.close()
print(f)

#Exceções
try:
    s = open('test.txt','r')
    o = s.read()
    s.close()
    print(s)
except:
    print('Não foi possível abrir o aququivo')