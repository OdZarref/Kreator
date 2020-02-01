from file_writing import *
from text_manipulation import *
from interface import *
from input import *

mostra_logo()
name = ''
sobrenomes = list()
data_name = leia_nome_completo()
data_nascimento = leia_nascimento()
apelidos = leia_apelidos()

if len(data_name) == 0 and len(data_nascimento) == 0 and len(apelidos) == 0:
    linhas('No arguments have been entered. Program closed.')
else:
    complementos = criar_complementos(data_nascimento)

    if len(data_name) != 0:
        for names in data_name:
            if names == data_name[0]:
                name = names
            else:
                sobrenomes.append(names)

        nome_arquivo = name
    else:
        nome_arquivo = 'passwords'
        
    verificar_arquivo = verificar_arquivo(nome_arquivo)
    if not verificar_arquivo:
        criar_arquivo(nome_arquivo)

    if len(data_nascimento) != 0:
        escrever_senhas_nascimento(nome_arquivo, data_nascimento)

    if name != '':
        escrever_senhas(nome_arquivo, name, complementos)

    sobrenome_pequeno = concatenacao_sobrenome_pequeno(name, sobrenomes)
    if sobrenome_pequeno != '':
        escrever_senhas(nome_arquivo, sobrenome_pequeno, complementos)
        
    sobrenomes = remove_sobrenome_pequeno(name, sobrenomes)

    if len(sobrenomes) == 0:
        escrever_senhas(nome_arquivo, name, complementos)
    elif len(sobrenomes) == 1:
        escrever_um_nome(nome_arquivo, name, sobrenomes, complementos)
    elif len(sobrenomes) == 2:
        escrever_dois_nomes(nome_arquivo, name, sobrenomes, complementos)
    elif len(sobrenomes) == 3:
        escrever_tres_nomes(nome_arquivo, name, sobrenomes, complementos)
    elif len(sobrenomes) == 4:
        escrever_quatro_nomes(nome_arquivo, name, sobrenomes, complementos)

    if len(apelidos) > 0:
        for apelido in apelidos:
            if len(sobrenomes) == 0:
                escrever_senhas(nome_arquivo, apelido, complementos)
            elif len(sobrenomes) == 1:
                escrever_um_nome(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 2:
                escrever_dois_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 3:
                escrever_tres_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 4:
                escrever_quatro_nomes(nome_arquivo, apelido, sobrenomes, complementos)

    for surname in sobrenomes:
        escrever_senhas(nome_arquivo, surname, complementos)

    for apelido in apelidos:
        escrever_senhas(nome_arquivo, apelido, complementos)

linhas(f'Passwords written: {conta_senhas(nome_arquivo)}')
