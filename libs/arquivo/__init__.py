def verify_file(file_name):
    from time import sleep
    from libs.interface import lines

    try:
        file = open(file_name + '.txt', 'rt')
        file.close()
    except FileNotFoundError:
        text = f'ARQUIVO "{file_name}.txt" NÃO ENCONTRADO'
        lines(text)
        sleep(1)
        return False
    else:
        text = f'ARQUIVO "{file_name}.txt" ENCONTRADO'
        lines(text)
        sleep(1)
        return True


def create_file(file_name):
    from time import sleep

    try:
        file = open(file_name + '.txt', 'wt+')
        file.close()
    except:
        print('ERRO AO CRIAR ARQUIVO')
        sleep(1)
    else:
        print(f'ARQUIVO "{file_name}.txt" CRIADO')
        print('=' * (15 + int(len(file_name))))
        sleep(1)


def write_passwords(file_name, name, complements):
    from time import sleep

    try:
        file = open(file_name + '.txt', 'at')
    except:
        print('ERRO AO TENTAR ABRIR ARQUIVO PARA ESCRITURA')
        sleep(0.5)
    else:
        if len(name) >= 6:
            print(name)
            file.write(name + '\n')

        for item in complements:
            print(name + item)
            file.write(name + item + '\n')
            sleep(0.2)
    finally:
        file.close()


def write_one_surnames(file_name, name, surnames, complements):
    concatenation = name + surnames[0]
    write_passwords(file_name, concatenation, complements)


def write_two_surnames(file_name, name, surnames, complements):
    concatenation = name + surnames[0] 
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[1]
    write_passwords(file_name, concatenation, complements)
    concatenation = name + surnames[0] + surnames[1]
    write_passwords(file_name, concatenation, complements)


def write_three_surnames(file_name, name, surnames, complements):
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


def write_four_surnames(file_name, name, surnames, complements):
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
