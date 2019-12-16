#dada a lista abaixo:

lista = ['Corinthians', [1, 2, 3, 4, 5],
         'Palmeiras', 'São Paulo', 
        [10, 11, 12, 13, 14],'Flamengo', 'Vasco']



# print 3, 13, Vasco
print(lista[1][2], lista[-3][-2], lista[-1])
# print 5, São Paulo, 14
print(lista[1][-1], lista[3], lista[-3][-1])
# mude o valor de 4 para 40
lista[1][-2] = 40

# mude o valor de 14 para 150
lista [-3][-1] = 150
print(lista)