#!/usr/bin/python3
import random

class Humano:
    #atributos
    # pernas = 2
    # bracos = 2
    # cabeca = 1
    _PI = 3.1415

    #metodos mágicos
    def __init__(self,nome): #método construtor
        #atributos do objeto
        self.pernas = 2
        self.bracos = 2
        self.cabeca = 1
        self.nome = nome
        self.saldo = 0
        
    #metodo
    def acidente(self):
        self.pernas -= 1
    def saldo_bancario(self):
        if self.pernas < 2 and self.nome == "Carlos":
            self.saldo -= 10.000
            print('Você está de férias permanentes')
            if random.randint(1,10) == 9:
                self.saldo *= -1
        else:
            print('Você não é o Carlos, beleza')
            self.saldo += 10.000
            print(f'você agora tem {self.saldo}')

carlos = Humano('Carlos') #Criando um objeto
# carlos._PI = 4
# print(carlos._PI)
# print(Humano._PI)
print(carlos.pernas)
carlos.acidente()
print(carlos.pernas)
carlos.saldo_bancario()
print('Seu saldo atual é de: R$',carlos.saldo)
# print(carlos.pernas) #acessando um atributo
# carlos.pernas = 1 #mudando um atributo
# print(carlos.pernas)