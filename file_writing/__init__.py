def verify_file(file_name='passwords'):
    from time import sleep
    from interface import lines

    try:
        file = open(file_name + '.txt', 'rt')
        file.close()
    except FileNotFoundError:
        text = f'"{file_name}.txt" not found'
        lines(text)
        sleep(1)
        return False
    else:
        text = f'"{file_name}.txt" found'
        lines(text)
        sleep(1)
        return True


def create_file(file_name='passwords'):
    from time import sleep

    try:
        file = open(file_name + '.txt', 'wt+')
        file.close()
    except:
        print('Error creating file.')
        sleep(1)
    else:
        print(f'"{file_name}.txt" created.')
        print('=' * (15 + int(len(file_name))))
        sleep(1)


def write_passwords_birth_date(file_name, birth_date):
    from time import sleep

    file = open(file_name + '.txt', 'at')
    file.write(birth_date + '\n')
    print(birth_date)
    sleep(0.05)
    file.write(birth_date[0:4] + birth_date[-2:] + '\n')
    print(birth_date[0:4] + birth_date[-2:])
    sleep(0.05)


def write_passwords(file_name, name, complements):
    from time import sleep

    try:
        file = open(file_name + '.txt', 'at')
    except:
        print('Error trying to open writing file.')
        sleep(0.5)
    else:
        if len(name) >= 6:
            print(name)
            file.write(name + '\n')

        for item in complements:
            if len(name + item) >= 6:
                print(name + item)
                file.write(name + item + '\n')
                sleep(0.05)
    finally:
        file.close()


def write_one_names(file_name, name, surnames, complements):
    concatenation = name + surnames[0]
    write_passwords(file_name, concatenation, complements)


def write_two_names(file_name, name, surnames, complements):
    concatenation = name + surnames[0] 
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1]
    write_passwords(file_name, concatenation, complements)


def write_three_names(file_name, name, surnames, complements):
    concatenation = name + surnames[0] 
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[2]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1] + surnames[2]
    write_passwords(file_name, concatenation, complements)


def write_four_names(file_name, name, surnames, complements):
    concatenation = name + surnames[0] 
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[2]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[3]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1] + surnames[2]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1] + surnames[2] + surnames[3]
