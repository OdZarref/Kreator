from file_writing import *
from text_manipulation import *
from interface import *
from input import *

mostra_logo()
nome = ''
sobrenomes = list()
dados_nome = leia_nome_completo()
dados_nascimento = leia_nascimento()
apelidos = leia_apelidos()

if len(dados_nome) == 0 and len(dados_nascimento) == 0 and len(apelidos) == 0:
    linhas('No arguments have been entered. Program closed.')
else:
    complementos = criar_complementos(dados_nascimento)

    if len(dados_nome) != 0:
        for nomes in dados_nome:
            if nomes == dados_nome[0]:
                nome = nomes
                nome_arquivo = nome
            else:
                sobrenomes.append(nomes)
    else:
        nome_arquivo = 'passwords'
        
    verificar_arquivo = verificar_arquivo(nome_arquivo)
    if not verificar_arquivo:
        criar_arquivo(nome_arquivo)

    if len(dados_nascimento) != 0:
        escrever_senhas_nascimento(nome_arquivo, dados_nascimento)

    if nome != '':
        escrever_senhas(nome_arquivo, nome, complementos)

    sobrenome_pequeno = sobrenome_pequeno(nome, sobrenomes)
    if sobrenome_pequeno != '':
        escrever_senhas(nome_arquivo, nome + sobrenome_pequeno, complementos)
        
    sobrenomes = remove_sobrenome_pequeno(nome, sobrenomes)

    if len(sobrenomes) == 0:
        escrever_senhas(nome_arquivo, nome, complementos)
    elif len(sobrenomes) == 1:
        escrever_um_nome(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 2:
        escrever_dois_nomes(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 3:
        escrever_tres_nomes(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 4:
        escrever_quatro_nomes(nome_arquivo, nome, sobrenomes, complementos)

    if len(apelidos) > 0:
        for apelido in apelidos:
            if len(sobrenomes) == 0:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_senhas(nome_arquivo, apelido, complementos)

            elif len(sobrenomes) == 1:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_um_nome(nome_arquivo, apelido, sobrenomes, complementos)

            elif len(sobrenomes) == 2:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_dois_nomes(nome_arquivo, apelido, sobrenomes, complementos)

            elif len(sobrenomes) == 3:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_tres_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 4:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)
                    
                escrever_quatro_nomes(nome_arquivo, apelido, sobrenomes, complementos)

    for surname in sobrenomes:
        if sobrenome_pequeno != '':
            escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

        escrever_senhas(nome_arquivo, surname, complementos)

    linhas(f'Passwords written: {conta_senhas(nome_arquivo)}')
