#!/usr/bin/python3

# dada a string 

# Não deixe o barulho da opinião dos outros abafar sua voz interior. 
# E mais importante, tenha a coragem de seguir seu coração e sua intuição.
# Eles de alguma forma já sabem o que você realmente quer se tornar. 
# Tudo o mais é secundário.

# conte quantas letras a tem no texto
# mude todas as letras o para s
# divida o texto em uma lista colocando virgulas nos espaços

texto = "Não deixe o barulho da opinião dos outros abafar sua voz interior.\
E mais importante, tenha a coragem de seguir seu coração e sua intuição.\
Eles de alguma forma já sabem o que você realmente quer se tornar.\
Tudo o mais é secundário."
Letras_A = texto.count('a')
print()
print('RESPOSTA:')
print()
print('Letras A = ',Letras_A)
print("Novo texto substituido = ", texto.replace('o','s'))
print("Texto dividido =", texto.split(' '))