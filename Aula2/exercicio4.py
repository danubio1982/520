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
bolsonaro = [
    'bolsonaro',
    'bozo',
    'bolsanario',
    'borsalino',
    'bonoliro',
    'facista'
    ]
lula = [
    'lula',
    'mula',
    '9 dedos',
    'nove dedos',
    'ladrão',
    'luladrão'
    ]
hitler = [
    'adolf hitler',
    'hitler',
    'fuhr',
    'bigodin',
    'nazista',
    'argentino'
]
tiririca = [
    'tiririca',
    'palhaço',
    'tiririca',
    'florentina'
]

#Atribuindo todas as figuras públicas para uma lista
figuras_publicas = [bolsonaro, lula, hitler, tiririca]

#definindo lista de nomes
lista_nomes = []

try:
    while True:
        #requisição pelo nome
        nome = input('Digite um nome: ').lower().strip()

        # para cada figura publica, vou validar o nome digitado
        for apelido in figuras_publicas:
            if nome in apelido:
                cad_figura_publica = True
                break
            else:
                cad_figura_publica = False
        #Criando lógica para cadastro
        if cad_figura_publica:
            print('Lançando erro Cadastro de figuras')
        elif nome in lista_nomes:
            print('nome Já existe')
        elif nome == 'visualizar':
            for nome_cadastrado in lista_nomes:
                print(nome_cadastrado,end=', ')
            print('\n')
        else:
            print('Cadastro Realizado')
            lista_nomes.append(nome)

except Exception:
    print('Você cadastrou uma figura pú