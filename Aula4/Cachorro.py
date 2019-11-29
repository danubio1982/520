#!/usr/bin/python3

class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
        pass

    def viver(self):
        print('Estou vivo!!')

class Cachorro(Animal):
    '''Abstração de cachorro
    
    Cria cachorro baseado nos conceitos definidos em sala de aula'''

    _DNA = 'Cachorro'

    def __init__(self, nome, idade, cor, raca='vira-lata', porte='Médio'):
        #parametros obrigatórios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.porte.porte

        # Atributos padrão para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.lingua = True #valores únicos como True ou False
        self.focinho = True
        self.olhos = 2
        self.rabo = True 
        print(f'Cachorro {nome}, construído com sucesso!')

    def latir(self):
        if self.lingua:
            print('Au Au Au')

    def comer(self):
        print('Comendo...')

    def cheirar(self):
        if self.focinho:
            print('funk, funk, funk...')

    def cagar(self):
        print('mmmmmm...')
    
    def dormir(self):
        print('Zzzzzzzzzz1!!!')

    def __del__(self):
        print(f'Descanse em paz, {self.nome}')

    def __str__(self):
        return 'Construir um cachorro'


# rex = Cachorro()
# rex.viver()
# rex.latir()

