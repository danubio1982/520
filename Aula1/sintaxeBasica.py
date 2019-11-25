#!/usr/bin/python3

# # #!/usr/bin/python3 - "she bangs" - direciona para o pyton

# # print('Oi')

# # contagem de listas começa com 0

# #lista = ['Arroz','Feijão','Óleo','Sal','Açucar','Temperos']
# #           0       1       2       3       4       5   

# # print(lista[0])

# # print(lista[-2])

# # print(lista[1:4:2])

# #lista2 = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

# # print(lista[-2])

# #lista3d = [
# #    ['domingo','segunda','terça','quarta','quinta','sexta','sabado'],
#    # [1,2,3,4,5,6,7,],
#  #   ['a','b','c','d','e','f','g']
# #]

# # print(lista3d)
# # print(lista3d[2][2])

# # lista = ['Arroz','Feijão','Óleo','Sal','Açucar','Temperos']

# #lista.append('Carne')
# #lista.insert(-1,'Sabão em pó')
# #lista.sort()
# #lista.reverse()

# #print(lista)
# #print(len(lista))

# #print(lista.index('Açucar'))

# #print(lista.count('Arroz'))

# #lista.remove('Sabão em pó')

# #print(lista)


# #!/usr/bin/python3

# #contagem de lista começa sempre do 0
# lista = ['Arroz','Feijão','Óleo','Sal','Açucar','Temperos','Cerveja']
# #           0       1       2       3       4       5
# #lista3d = [
#  #   [ 2 , 3 , 4 , 5 ],
#   #  [ 3 , 4 , 5 , 6 ],
#    # [ 7 , 5 , 7 , 8],
# #]

# #lista.append('Carne')

# #lista.insert(4,'Sabão em pó')

# #print(lista)

# # lista.pop(4)

# #lista.sort()

# #lista.reverse()

# #print(lista)


# # ############
# # ## Tuplas ##
# # ############

# tupla = ('Maçã','Banana','Laranja','Abacaxi','Uva')
# print(type(tupla))

# #segundo metodo pra criar tuplas
# tupla2 = 'valor', 2, True, 2j
# print(type(tupla2))


# #Acessando índices de uma tupla
# print(tupla[3])
# print(tupla[1:4])
# print(tupla[0:4:2])
# print(tupla[-3])

# #converter tupla para lista
# lista_da_tupla = list(tupla)
# print(type(lista_da_tupla))

# print(tupla)

#################
## Dicionários ##
#################

# # Criando Dicionário

# apresentacoes = {
#     'Paulista':'Salve',
#     'Carioca': 'Eae',
#     'Pirata':'Argh',
#     'Mineiro':'Pão de queijo',
#     'Acre':'Barulhos de Dinossauro'
# }

# #Acessando indices em um dicionário
# print(apresentacoes['Paulista'])

# #Criando um dicionário com multi-valores internos
# linguagem_favorita = {
#     'Daniel':{
#         'linguagem':'python',
#         'tempo_de_experiencia':5
#     },
#     'Olympio':{
#         'linguagem':'R',
#         'linguagem2':'VBA',
#         'tempo_de_experiencia':10

#     },
#     'Danubio':{
#         'linguagem':'HTML',
#         'tempo_de_experiencia': 15
#     },
#     'Valquiria':{
#         'linguagem':'CSS',
#         'tempo_de_experiencia': 2
#     },
# }

# valores = {'nome':'Daniel','Sobrenome':'Silva'}
# print(linguagem_favorita.get('Danubio')['linguagem'])

# #acesso a todas as chaves
# print(linguagem_favorita.keys())

# #Acesso aos valores
# print(linguagem_favorita.values())

# #Acesso aos itens
# print(valores.items())

somar = 2+2
print(2+2, 'Retornando o valor de 2 + 2')
print(somar, 'Retornando somar')

subtrair = somar - 2 #somar retorna um tipo inteiro
print(subtrair,'retornando o subtrair')

multiplicar = subtrair * 3 #subtrair também retorna um tipo inteiro
print(multiplicar, 'retornando o Multiplicar')

divisao = multiplicar /5 #multiplicar tbm retorna um número inteiro
print(divisao, 'retornando o dividir') #Retorna um valor de ponto flutuante

potencia = 2**2
print(potencia, 'Retornando o valor da potencia')

raiz = 2 ** 0.5
print(raiz, 'Retornando o valor da raiz')

letras = 'abcdefghijk'+'lmnopqrstuvwxyz'
print(letras)

print.float(input('Digite um numero: ') + float(input('Digite outro numero: '))






