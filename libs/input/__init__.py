def read_name_surname():
    name_surname = str(input('Name: ')).lower().split()

    return name_surname


def read_birth_date():
    from libs.interface import lines

    while True:
        birth_date = str(input('Birth Date: '))

        if len(birth_date) == 6 or len(birth_date) == 8 or len(birth_date) == 0:
            break
        else:
            lines('DEVEM SER VALORES NUMÉRICOS DE 6 OU 8 CARACTERES DE COMPRIMENTO.')

    return birth_date


def read_nicknames():
    nicknames = str(input('Nickname: ')).split()

    return nicknames