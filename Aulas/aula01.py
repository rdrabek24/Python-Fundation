#!/usr/bin/python3

## Identação

# nome = input('Digite seu nome: ')

# if nome == str: # : após condicionais
#     print('nome é uma string') # identação de 4 espaços

# else: # : após condicionais
#     print('nome nã é uma string') # identação de 4 espaços


## Entrada e saída de dados

# nome = input('Digite seu nome: ')

# print(nome)

# numero = float(input('Digite um número: '))

# print(type(numero))

## métodos de string

# texto = 'isso é uma string'
comida = ['lasanha']
print(comida)
comida.append('espaguete')
comida.append('capeletti')
comida.insert(1,'penne')
print(comida)
print(comida[2])
comida.pop(2)
comida.remove('lasanha')
print(comida)
print()
lista00 =[[1,2,3],[4,5,6],'lasanha',160.6]
print(lista00[0][2])
lista = [[1,2,[1,5,6]],[4,5,6],'penne', 156.7]
print(lista[0][2][1])
lista[0][2][1] = 34
print(lista)