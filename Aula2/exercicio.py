#!/usr/bin/python3

#Criar uma variavel idade onde recebe uma
#idade via linha de comando, validade se essa
#essa pessoa pode beber ou não, caso possa, atribuir
#ao valor de uma variável embriagado o valor true, senão false

# nome = input('Qual o seu nome? ')
# idade = int(input('Quantos anos você tem? '))

# if idade >= 18:
#     print(f'{nome}, qual bebida você quer?') = embriagado
# else:
#     print(f'Você não pode beber, {nome}!') = sobrio

#criar condicional para que se a pessoa estiver embreagada, não podeá beber

# idade = int(input('Quantos anos você tem? '))



# #criar validacao se a pessoa bebeu para atribuir a variavel embriafado como true e false
# embriagado = True
# embriagado = False

# if idade >= 18
#     bebeu = input('você bebeu? [y para sim e n para não]').strip().lower()
#         if bebeu:
#             embriagado = True
#         else:
#             embriagado = False
# else:
#     embriagado = false

# CRIAR UMA VALIDAÇÃO COM ELIF PARA QUE SE A IDADE FOR MENOR QUE 0 ANOS A PESSOA SEJA INVALIDA

idade = int(input('Quantos anos você tem? '))
if idade >= 18:
    habilitacao = input('Você possui habilitacao? [y para sim e n para não]').strip().lower()
    if habilitacao == 'y':
        habilitacao = True
        bebeu = input('Você bebeu? [y para sim e n para não]').strip().lower()
        if bebeu == 'y':
            embriagado = True
        else:
            embriagado = False
    else:
        habilitacao = False
else:
    embriagado = False

if habilitacao and not embriagado:
    print('Você pode dirigir')
else:
    print('Você não pode dirigir')


