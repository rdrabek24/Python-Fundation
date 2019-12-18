
def somar(valor1, valor2):
    return valor1 + valor2

def subtrair(valor1, valor2):
    return valor1 - valor2

def dividir(valor1, valor2):
    return valor1 / valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2


entrada1 = int(input('Valor 1 = '))
entrada2 = int(input('Valor 2 = '))


res_soma = somar(entrada1,entrada2)
print(f'Soma de dois numeros =  {res_soma}')

res_subtrair = subtrair(entrada1,entrada2)
print(f'Subtração de dois numeros =  {res_subtrair}')

res_dividir = dividir(entrada1,entrada2)
print(f'Soma de dois numeros =  {res_dividir}')

res_multiplicar = multiplicar(entrada1,entrada2)
print(f'Multiplicação de dois numeros =  {res_multiplicar}')