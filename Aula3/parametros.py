#!/usr/bin/python3

##########################
## parâmetros de função ##
##########################


# def retorna_pessoa(nome,idade):
#     print(f'nome: {nome} \nidade: {idade}')
# retorna_pessoa(nome='Danubio' idade=37)

# def retorna_valor_int( inteiro : int) -> int:
#     '''Função com anotação de tipo

#     Se refere a função que possui tipos especificos e mostram na sua 
#     sintaxe de construção o que é necessário, sempre tem que pular uma linha '''

#     inteiro = int(inteiro)
#     return int(inteiro)

# print(retorna_valor_int)

### args e kwargs
# print('olá','mundo','.','prazer','sou','Danubio')

# ### Criando uma função que recebe multiplos valores
# def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
#     print(parametros_estaticos,'parametro estatico')
#     for argumento in argumento_variavel:
#         print(argumento)

# funcao_multi_valores('valor estático obrigatório',
#                     'Daniel', 'Andresa', 'João','Ana',
#                     'Paula','Lucas','Leonardo','Pedro')


# ## Argumentos com palavra chave - kwargs

# def parametros_chave_valor(**dados):
#     if dado('nome') == 'Daniel'
#         print('Acesso Negado')
#     else:
#         print('Permitido')

# #Execução - metodo 1
# print('Metodo 1')
# parametros_chave_valor(nome='Daniel', sobrnome='Silva',
#                         idade=19, sexo='Masculino')

# #Execução - metodo 2

def mudaCor(funcao):
    def modificaAzul(funcao):
        return f'\033[94m{funcao}\033[0m' 
    return modificaAzul()

def log(texto):
    return(texto)
    
print(log('oi'))