def remove_small_surname(name, surnames):
    for surname in surnames:
        if len(surname) <= 3:
            surnames.remove(surname)

    return surnames


def create_complements(birth_date=999):
    complements = ['123', '1234', '12345']

    if birth_date == 999:
        complements.append(birth_date[0:2])
        complements.append(birth_date[-4:])
        complements.append(birth_date[-2:])

    number = int(birth_date[-2:])
    if number < 10:
        complements.append(birth_date[-1])

    return complements


def concatenation_small_surname(name, surnames):
    name_concatenated = ''

    for pos, surname in enumerate(surnames):
        if len(surname) <= 3:
            name_concatenated = name + surname + surnames[pos + 1]

    return name_concatenated
