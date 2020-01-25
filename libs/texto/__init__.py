def remover_sobrenome_pequeno(nome, sobrenomes):
    for sobrenome in sobrenomes:
        if len(sobrenome) <= 3:
            sobrenomes.remove(sobrenome)

    return sobrenomes


def criar_complementares(data_nascimento):
    complementar = ['123', '1234', '12345']
    complementar.append(data_nascimento[0:2])
    complementar.append(data_nascimento[-4:])
    complementar.append(data_nascimento[-2:])

    numero = int(data_nascimento[-2:])
    if numero < 10:
        complementar.append(data_nascimento[-1])

    return complementar


def concatenacao_sobrenome_pequeno(nome, sobrenomes):
    nome_concatenado = ''

    for pos, sobrenome in enumerate(sobrenomes):
        if len(sobrenome) <= 3:
            nome_concatenado = nome + sobrenome + sobrenomes[pos + 1]

    return nome_concatenado
    