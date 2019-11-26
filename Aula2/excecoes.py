#!/usr/bin/python3

#######################
## TRATANDO EXCEÇÕES ##
#######################

# try: #tente a expressão
#     print('soma de dois valores')
#     numero1 = int(input('Digite um numero a ser somado: '))
#     numero2 = int(input('Digite outro numero a ser somado: '))
#     print(numero1 + numero2)
# except ValueError: #em caso de erro/exceção
#     print('Insira somente números')

# try: #tente o script
#     print('Divisão de dois valores')
#     numero1 = int(input('Digite um numero: '))
#     numero2 = int(input('Digite outro numero a ser dividido: '))
#     print(numero1 / numero2)
# except ValueError: #em caso de erro/exceção
#     print('Insira somente números')
# except ZeroDivisionError as e: 
#     print('não foi possível fazer a divisão - Erro:', e)
# except Exception as e:
#     print('Erro na execução do programa', e)
# finally:
#     print('Saindo do script')

# nulo = None

#######################
## LANÇANDO EXCEÇÕES ##
#######################

# try:
opcao = int(input('Não digite 5: '))
if opcao == 5:
    raise ValueError('Eu falei pra não digitar "5"')
# except ValueError as e:
#     print('Deu erro:', e)