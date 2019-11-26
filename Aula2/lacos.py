#!/usr/bin/python3

#######################
## LAÇO DE REPETIÇÃO ##
#######################

################
## LAÇO WHILE ##
################

#LAÇO WHILE executa uma ação enquanto a condição for verdadeira
 
# i = 0
# while(i < 10): # enquanto i for menor que 10
#         print(i) # mostrar o valor de i
#         i += 1 # i = i + 1
#         #repete

#Fazendo controle de um loop while

# i = 0
# while(True):
#     print('Teóricamente, um loop infinito')
#     i += 1
#     if i == 3 :
#       break
#     if i == 5:
#         continue
#     print('Teóricamente, um loop infinito', i)

# # Continue retoma do começo a execução de um loop
# i = 100 #Número inicial
# while i > 0: #enquanto i<0
#     i -= 1 # i = i - 1
#     if i % 2 == 1:
#         continue
#     print(i)

##############
## LAÇO FOR ##
##############

# Percorre itens em determinado alcance de valores

# lista = []
# for i in range(100): #começa no 1 e vai até o 100 de 2 em 2
#     lista.append(i)
# print(lista)

# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[91m{i}\033[0m','par')
#     if i % 2 == 1:
#         print(f'\033[1;32m{i}\033[0m','impar')

# #percorrer um dicionário

# dicionario = {
#     'nome':'Daniel',
#     'sobrenome':'Silva'
#     }

# # for i in dicionario:
# #     print(dicionario[i])

# for chave,valor in dicionario.items():
#     print(chave)
#     print(valor)

# Enumerando itens de uma lista

#lista = ['item1','item2','item3','item4','item5','item6','item7']

# print(list(enumerate(lista)))

# for i in enumerate(lista):
#     print(i)

# for indice,valor in enumerate(lista):
#     print(indice)

# List comprehension (compreensão em listas)

# lista = [x for x in range(1,101)]
# print(lista)


lista = [x*2 for x in range(1,100)]
print(lista)
