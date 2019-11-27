#!/usr/bin/python3

#
## EXERCÍCIO DE FUNÇÕES
#

#Criar uma função de soma que retorna a soma de 2 valores
#Criar uma função de subtração que retorna a subtração de 2 valores
#Criar uma função de multiplicação que retorna a multiplicação de 2 valores
#Criar uma função de divisão que retorne a divisão de 2 valores
#Criar uma função que gera raiz quadrada de um número x

#Como fazer documentação de sua função
def somar(n1, n2):
    '''Função de soma

    Este módulo realiza soma com dois valores e retorna o valor.'''
    print(__)
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir (n1, n2):
    if n2 == 0
        raise ZeroDivisionError('Não tem como, rapaz!')
    return n1 / n2

def raiz_quadrada(n1):
    if n1 < 0:
        return False
        # raise ValueError('Não há raiz quadrada de número negativo')
    else:
        n1 *= -1
        n1 **= 0.5
        return n1 ** 0.5

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

resultado = somar(n1 + n2)
print(resultado)