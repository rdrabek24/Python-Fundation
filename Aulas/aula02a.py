


## MANIPULACAO DE ARQUIVOS

with open('arquivo.txt', 'a') as p:
    p.seek(0)
    p.write('Curso de Python fundamentos dia 2\n\r')
    p.close()