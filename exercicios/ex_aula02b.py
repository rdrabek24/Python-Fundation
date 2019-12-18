## Raise esception

usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']while True:
    try:
        senha_usuario = input('Digite seu nome: ')
        if senha_usuario not in usuarios:
            raise NameError('Nome invalido, tente novamente!')
            continue
        else:
            print('Nome localizado.')
            break
    except NameError as n:
        print(n)