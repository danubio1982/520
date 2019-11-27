#!usr/pin/python3

##########################################
## Escopo de variáveis locais e globais ##
##########################################

variavel = 3

def muda_variavel():
    #variavel = 2 #variável de escopo local
    global  variavel
    variavel = 2  #variável de escopo global
    print(variavel)

muda_variavel()

print(variavel)