from libs.arquivo import *
from libs.texto import *
from libs.interface import *
from libs.leitura import *

lines('WD KREATOR')
data_name = read_name_surname()
birth_date = read_birth_date()
nicknames = read_nicknames()
complements = create_complements(birth_date)
name = ''
surnames = list()

for names in data_name:
    if names == data_name[0]:
        name = names
    else:
        surnames.append(names)

file_name = name

verify_file = verify_file(file_name)
if not verify_file:
    create_file(file_name)

small_surname = concatenation_small_surname(name, surnames)
if small_surname != '':
    write_passwords(file_name, small_surname, complements)
    
surnames = remove_small_surname(name, surnames)

if len(surnames) == 1:
    write_one_surnames(file_name, name, surnames, complements)
elif len(surnames) == 2:
    write_two_surnames(file_name, name, surnames, complements)
elif len(surnames) == 3:
    write_three_surnames(file_name, name, surnames, complements)
elif len(surnames) == 4:
    write_four_surnames(file_name, name, surnames, complements)


if len(nicknames) > 0:
    for nickname in nicknames:
        if len(surnames) == 0:
            write_passwords(file_name, nickname, complements)
        elif len(surnames) == 1:
            write_one_surnames(file_name, nickname, surnames, complements)
        elif len(surnames) == 2:
            write_two_surnames(file_name, nickname, surnames, complements)
        elif len(surnames) == 3:
            write_three_surnames(file_name, nickname, surnames, complements)
        elif len(surnames) == 4:
            write_four_surnames(file_name, nickname, surnames, complements)
