
numero2 = str('teste')

numeros = [1, 2, 3, 4, 5, 6]
multiplicados =[]


for num in numeros:
    multiplicados.append(num * 15)
print(multiplicados)

# OU

multiplicado = [i*15 for i in range(1,7)]
print(multiplicado)