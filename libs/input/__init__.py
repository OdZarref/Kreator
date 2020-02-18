def leia_nome_completo():
    nome_completo = str(input('Full Name: ')).lower().split()

    return nome_completo


def leia_nascimento():
    from libs.interface import linhas

    while True:
        nascimento = str(input('Birth Date: [dd/mm/yyyy] '))

        if len(nascimento) == 8 or len(nascimento) == 0:
            break
        else:
            linhas('Must be numeric values of 8 characters.')

    return nascimento


def leia_apelidos():
    apelidos = str(input('Nicknames: ')).split()

    return apelidos
    