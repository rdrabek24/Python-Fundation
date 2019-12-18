# Entrada e saída de dados

# Crie um programa que peça um número e multiplique por 15


# numero2 = str('teste')
# numero = int(numero2)
# print(type(numero))


# num = int(input('Digite um número: '))
# print(f' O número digitado foi {num} e multiplicado por 15 é {num * 15}')


# Repetição
# Multiplique os numeros da lista numeros por 15
# e  coloque o resultado na lista multiplicados

# numeros = [1, 2, 3, 4, 5, 6]
# multiplicados = []

# for numero in numeros:
#     multiplicados.append(numero * 15)

# print(multiplicados)

# # ou


# multiplicado = [i*15 for i in range(1 , 7)]

# print(multiplicado)

# usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']

# Peça para o usuario digitar o seu nome e caso não
# esteja na lista print um erro

# fazer um sistema que pergunte o sexo do usuario sendo, M, F
# mostre se o usuario é do sexo masculino ou feminino.

print('Digite seu sexo')
print('M - para Masculino')
print('F - para Feminino')

while True:
    user = input('>>> ')
     if user.lower() == 'm':
        print('Usuario de sexo masculino')
        break
    elif user.lower() == 'f':
        print('Usuario do sexo feminino')
        break
    else:
        print('Entrada Invalida, Digite novamente! ')
        continue