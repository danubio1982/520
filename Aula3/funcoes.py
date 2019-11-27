#!/usr/bin/python3

#############
## FUNÇÕES ##
#############

#ckicis de cpidugi pré-definidos pra execução

def mostrar_hello_world():
     print('Hello World')

# mostrar hello world()

def menu():
    print('Escolher opção:')
    print('1 - Registrar produto')
    print('2 - Consultar saldo do caixa')
    print('3 - Abrir caixa registradora')
    print('4 - Fechamento do mês')
    return input('Digite a opção desejada: ')

def registrar_produto():
    print('produto registrado')
def consultar_saldo():
    print('Saldo é de R$ X')
def abrir_caixa():
    print('Abrindo')
def fechamento():
    print('fechando')

# estrutura principal
print('Caixa Registradora')
opcao = menu()
if opcao == '1':
    pass #funcao 1
elif opcao == '2':
    pass #funcao 2
elif opcao == '3':
    pass #funcao 3
elif opcao == '4':
    pass #funcao 4
else:
    pass #funcao 5
