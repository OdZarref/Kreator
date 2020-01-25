from libs.arquivo import *
from libs.texto import *
from libs.interface import *
from libs.leitura import *

linhas('WD KREATOR')
dados_nome = ler_nome_sobrenome()
data_nascimento = ler_nascimento()
apelidos = ler_apelidos()
complementar = criar_complementares(data_nascimento)
nome = ''
sobrenomes = list()

for nomes in dados_nome:
    if nomes == dados_nome[0]:
        nome = nomes
    else:
        sobrenomes.append(nomes)

nome_arquivo = nome

existencia_arquivo = verificar_arquivo(nome_arquivo)
if not existencia_arquivo:
    criar_arquivo(nome_arquivo)

nome_pequeno = concatenacao_sobrenome_pequeno(nome, sobrenomes)
if nome_pequeno != '':
    escrever_senhas(nome_arquivo, nome_pequeno, complementar)
    
sobrenomes = remover_sobrenome_pequeno(nome, sobrenomes)

if len(sobrenomes) == 1:
    concatenacao = nome + sobrenomes[0]
    escrever_senhas(nome_arquivo, concatenacao, complementar)

elif len(sobrenomes) == 2:
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)

elif len(sobrenomes) == 3:
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementar)

elif len(sobrenomes) == 4:
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[2]
    concatenacao = nome + sobrenomes[3]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementar)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2] + sobrenomes[3]

for apelido in apelidos:
    if len(sobrenomes) == 1:
        concatenacao = apelido + sobrenomes[0]
        escrever_senhas(nome_arquivo, concatenacao, complementar)

    elif len(sobrenomes) == 2:
        concatenacao = apelido + sobrenomes[0] 
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[0] + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)

    elif len(sobrenomes) == 3:
        concatenacao = apelido + sobrenomes[0] 
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[2]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[0] + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
        escrever_senhas(nome_arquivo, concatenacao, complementar)

    elif len(sobrenomes) == 4:
        concatenacao = apelido + sobrenomes[0] 
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = apelido + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = nome + sobrenomes[2]
        concatenacao = nome + sobrenomes[3]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = nome + sobrenomes[0] + sobrenomes[1]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
        escrever_senhas(nome_arquivo, concatenacao, complementar)
        concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2] + sobrenomes[3]
