#!/usr/bin/python3

#####################################
## MANIPULANDO ARQUIVOS COM PYTHON ##
#####################################

### Abrir um arquivo para modificação ###

# Método não recomendado
ponteiro = open('nomedoarquivo.txt','r+')
#Abre um ponteiro para escrita de arquivos. O modo utilizado é o read plus (que serve para) leitura e escrita.
# Possuimos vários modos de acesso, por exemplo:
# w = sobrescrita
# r = somente leitura
# + = abre um arquivo para atualização (acrescente e modifica)
# a = complemento
# x = criação
# este método não é recomendado porque o ponteiro sempre necessita ser encerrado com o "close" e isso foi substituido com a adição do comando "with"
# ponteiro.write('Olá Mundo\n')
# ponteiro.read()
# ponteiro.close()

# Método usual

#arquivo em modo de escrita
with open('nomedoarquivo2.txt','w') as arquivo:
    arquivo.write('Olá mundo\n')
    arquivo.writelines(['banana\n','maçã\n'])

#arquivo em modo de leitura
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.read()

print(letras)

