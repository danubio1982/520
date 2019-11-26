#!/usr/bin/python3

#######
## Exercicio de excessões
#######

# Criar uma tela de cadastro de usuário em uma lista
# Essa tela não pode aceitar figuras públicas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Tiririca
# Esse Loop é infinito, onde só acaba quando colocado uma figura
# pública

# Arrays de nomes de figura publica
# bolsonaro = [
#     'bolsonaro',
#     'bozo',
#     'bolsanario',
#     'borsalino',
#     'bonoliro',
#     'facista'
#     ]
# lula = [
#     'lula',
#     'mula',
#     '9 dedos',
#     'nove dedos',
#     'ladrão',
#     'luladrão'
#     ]
# hitler = [
#     'adolf hitler',
#     'hitler',
#     'fuhr',
#     'bigodin',
#     'nazista',
#     'argentino'
# ]
# tiririca = [
#     'tiririca',
#     'palhaço',
#     'florentina'
# ]

# #Atribuindo todas as figuras públicas para uma lista
# figuras_publicas = [bolsonaro, lula, hitler, tiririca]

# for figura in figuras_publicas:
#     for apelido in figura:
#         with open('politicos.txt', 'a') as arquivo:
#             arquivo.write(apelido + '\n')

#definindo lista de nomes
lista_nomes = []

with open('politicos.txt', 'r') as arquivo:
    figuras_publicas = arquivo.readlines()
figuras_publicas = [apelido.replace('\n','') for apelido in figuras_publicas]
with open('nomes.txt','r') as nomes:
    lista_nomes = [nome.replace('\n','') for nome in nomes.readlines()]
try:
    while True:
        #requisição pelo nome
        print(figuras_publicas)
        nome = input('Digite um nome: ').lower().strip()
        # para cada figura publica, vou validar o nome digitado
        if nome in figuras_publicas:
            cad_figura_publica = True
        else:
            cad_figura_publica = False
        #Criando lógica para cadastro
        if cad_figura_publica:
            raise ValueError('Você tentou inserir uma figura pública')
        elif nome in lista_nomes:
            print('nome Já existe')
        elif nome == 'visualizar':
            for nome_cadastrado in lista_nomes:
                print(nome_cadastrado,end=', ')
            print('\n')
        else:
            print('\n'*100)
            with open('nomes.txt','a') as nome:
                nome.write(nome + '\n')
            print('Cadastro Realizado')
except Exception:
    print('Você cadastrou uma figura pública')
    print(lista_nomes).title()
