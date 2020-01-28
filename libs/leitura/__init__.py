def read_name_surname():
    name_surname = str(input('Name: ')).lower().split()

    return name_surname


def read_birth_date():
    birth_date = str(input('Birth Date: '))

    return birth_date


def read_nicknames():
    nicknames = str(input('Apelido: ')).split(', ')

    return nicknames