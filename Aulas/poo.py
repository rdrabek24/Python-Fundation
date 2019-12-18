"""

Abstração

entidades ## generalização
atributos ## Caractereisticas
métodos ## Ações
Instâncias

"""


class Passaro():

    def __init__(self):  # atributos
        self.asas = 2
        self.penas = True
        self.bico = True
        self.patas = 2
    
    def voar(self):
        if self.asas < 2:
            self.cont = 0
            print('Passaro com necessidades especiais!')
            print('Não pode voar')
        else
            self.cont = 1
            print('Voando...')

    def pousar(self):
        print('Pousando...')

    def comer(self):
        print('Comendo...')

    def dormir(self):
        print('Dormindo...')

sabia = Passaro()
sabia.asas = 1
sabia.voar()
print(sabia.asas)


