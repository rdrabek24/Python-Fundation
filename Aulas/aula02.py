## Revisão

# Entrada e saída de dados

# Entrada: input()
# Saída: print()

nome = input('Digite o nome: ')
print(f'O nome digitado foi {nome}')


import os
var = os.getenv("SSH_AUTH_SOCK")



while True:
    try:
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        print(x + y)
    except ValueError as e:
        print('Tipo invalido')
    finally:
        print('Saindo do script')