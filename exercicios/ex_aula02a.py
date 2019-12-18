## Raise esception
while True:
    try:
        senhas = [3030, 3242, 3333, 1240]
        senha_usuario = int(input('Digite sua senha: '))
        if senha_usuario not in senhas:
            raise NameError('Senha invalida, tente novamente!')
            continue
        else:
            print('Login efetuado.')
            break
    except NameError as n:
        print(n)