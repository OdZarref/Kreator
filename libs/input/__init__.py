def read_name_surname():
    name_surname = str(input('Name: ')).lower().split()

    return name_surname


def read_birth_date():
    while True:
        birth_date = str(input('Birth Date: '))

        if len(birth_date) == 6 or len(birth_date) == 8 or len(birth_date) == 0:
            break

    return birth_date


def read_nicknames():
    nicknames = str(input('Apelido: ')).split()

    return nicknames