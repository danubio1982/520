#!/usr/bin/python3

# carro = input('Digite qual o caminho a ser seguido: ')

# a = 'engarrafado'
# b = 'livre'

# if a == 'engarrafado':
#     print('Melhor ir pela b')
# else:
#     print('Indo pelo camiho a')

###
## Estrutura de condicional simples
##

# nome = input('Digite seu nome: ')

# #  if nome == 'Danubio':
# #     print('Ola Aluno')
# #  print('Seja bem vindo')

#  ## Estrutura conficional composta

# if nome == 'Danubio':
#     print(f'Ola Aluno {nome}')
# else:
# #     print(f'Bem vindo professor {nome}')
# # print('Você pode utilizar a plataforma')


# nome = input('Digite seu nome: ').strip().title()
# sobrenome = input('Digite seu sobrenome: ').strip().title()

# if nome == 'Daniel' and sobrenome == 'Silva': #pode-se utilizar o 'or' em que alguma das condicionantes é verdadeira
#     print(f'Bem vindo professor {nome} {sobrenome}')
# else:
#     print(f'Bem vindo aluno {nome} {sobrenome}')


#####
## condicionais encadeadas
##

# if nome == 'Daniel':
#     if sobrenome == 'Silva':
#         print('Olá professor')
#     else:
#         print('Você é Daniel, mas não é professor')
# else:
#     print(f'Olá {nome}, em que posso te ajudar')


##
##Condicionais aninhadas
##


#EL(se)IF consegue fazer validação em mais de um fator com comportamento diferente
nome = input('Digite seu nome: ').strip().title()

if nome == 'Danubio':
    print(f'Seu nome é muito bonito, {nome}')
elif nome == 'Juliana':
    print(f'Seu nome é bem legal, {nome}')
elif nome == 'Malaquias':
    print(f'Seu nome é horroroso, {nome}')
else:
    print(f'{nome}, seu nome é bem normal')
