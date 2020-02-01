def verificar_arquivo(nome_arquivo='passwords'):
    """Verifica se o arquivo que conterá as senhas já existe.
    
    Keyword Arguments:
        nome_arquivo {str} -- (default: {'passwords'})
    
    Returns:
        [bool] -- [Se já existir recebe True, senão recebe False]
    """
    from time import sleep
    from interface import linhas

    try:
        arquivo = open(nome_arquivo + '.txt', 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo='passwords'):
    from time import sleep

    try:
        arquivo = open(nome_arquivo + '.txt', 'wt+')
        arquivo.close()
    except:
        print('Error creating arquivo.')


def escrever_senhas_nascimento(nome_arquivo, data_nascimento):
    """Escreve como senha somente a data de nascimento.
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo onde será escrito
        data_nascimento {str} -- A data de nascimento
    """
    from time import sleep

    arquivo = open(nome_arquivo + '.txt', 'at')
    arquivo.write(data_nascimento + '\n')
    print(data_nascimento)
    arquivo.write(data_nascimento[0:4] + data_nascimento[-2:] + '\n')
    print(data_nascimento[0:4] + data_nascimento[-2:])


def escrever_senhas(nome_arquivo, nome, complementos):
    from time import sleep

    try:
        arquivo = open(nome_arquivo + '.txt', 'at')
    except:
        print('Error trying to open writing file.')
        sleep(0.5)
    else:
        if len(nome) >= 6:
            print(nome)
            arquivo.write(nome + '\n')

        for item in complementos:
            if len(nome + item) >= 6:
                print(nome + item)
                arquivo.write(nome + item + '\n')
    finally:
        arquivo.close()


def escrever_um_nome(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará o nome com o único sobrenome
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo que será aberto para escritura
        nome {str} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_dois_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo que será aberto para escritura
        nome {str} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_tres_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {[type]} -- Nome do arquivo que será aberto para escritura
        nome {[type]} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_quatro_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {[type]} -- Nome do arquivo que será aberto para escritura
        nome {[type]} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[3]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2] + sobrenomes[3]


def conta_senhas(nome_arquivo):
    with open(nome_arquivo + '.txt') as arquivo:
        total = 0

        for linha in arquivo:
            total += 1

    return total
