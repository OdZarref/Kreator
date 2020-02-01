def remove_sobrenome_pequeno(nome, sobrenomes):
    """Se a pessoa tiver um sobrenome menor que quatro letras, este sobrenome será removido para ser escrito aparte.
    
    Arguments:
        nome {str} -- Nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
    
    Returns:
        list() -- A lista sem o sobrenome pequeno
    """
    for sobrenome in sobrenomes:
        if len(sobrenome) <= 3:
            sobrenomes.remove(sobrenome)

    return sobrenomes


def criar_complementos(nascimento):
    """Cria os complementos que será concatenados com os dados do nome completo
    
    Arguments:
        nascimento {str} -- A data de nascimento da pessoa
    
    Returns:
        list() -- Uma lista com todos os complementos gerados
    """
    complementos = ['123', '1234', '12345']

    if len(nascimento) == 8:
        complementos.append(nascimento[0:2])
        complementos.append(nascimento[-2:])
        complementos.append(nascimento[-4:])

        numero = int(nascimento[-2:])
        if numero < 10:
            complementos.append(nascimento[-1])

    return complementos


def concatenacao_sobrenome_pequeno(nome, sobrenomes):
    """Concatenará o sobrenome pequeno com o nome e com o sobrenome que vier à frente.
    
    Arguments:
        nome {str} -- Nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
    
    Returns:
        str -- O nome + sobrenome_pequeno + o sobrenome que vier à frente.
    """
    nome_concatenado = ''

    for pos, sobrenome in enumerate(sobrenomes):
        if len(sobrenome) <= 3:
            nome_concatenado = nome + sobrenome + sobrenomes[pos + 1]

    return nome_concatenado
