#!/usr/bin/python3

#############################
## Operadores Aritimeticos ##
#############################

# variaveis por nomeclatura podem ter no maximo 16 caracteres

num1 = 6 #numero 1
num2 = 8 #numero 2
adicao = num1 + num2 #adicao
subtracao = num1 - num2 #subtracao
maltiplicacao = num1 * num2 #multiplicacao
divisao = num1 / num2 #divisao
result_div_int = num1 // num2 #Resultado de uma divisao inteira
resto_div_int = num1 % num2 #Resultado de uma divisao inteira (modulo)

#Operadores de Forma Abreviada
#Pega o valor atual do numero e realiza um calculo
#Atribuindo o resultado a variavel

numero = 1 
numero += 3 # 1+3
numero -= 3 # 4-3
numero *= 4 # 1*4
numero /= 2 # 4/2
numero %= 2 #2/2=0

###########################
# Operadores Relacionais ##
###########################

numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2) #igualdade False
print(numero1 != numero2) #Diferenciacao true
print(numero1 < numero2) #Menor que True
print(numero1 <= numero2) #Menor ou igual que True
print(numero1 > numero2) #Maior que False
print(numero1 >= numero2) #Menor ou igual que False

print(numero1 is numero3) #Compara se estao alocados no mesmo bloco de memoria True

lista = ['item1','item2','item3']
print('item1' in lista) #compara existencia de valores em lista True

