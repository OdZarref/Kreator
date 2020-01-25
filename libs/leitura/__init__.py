def ler_nome_sobrenome():
    nome_sobrenome = str(input('Nome completo: ')).split()

    return nome_sobrenome


def ler_nascimento():
    data_nascimento = str(input('Data de nascimento: '))

    return data_nascimento


def ler_apelidos():
    apelidos = str(input('Apelido: ')).split(', ')

    return apelidos