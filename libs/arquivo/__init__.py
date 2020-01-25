def verificar_arquivo(nome_arquivo):
    from time import sleep
    from libs.interface import linhas

    try:
        arquivo = open(nome_arquivo + '.txt', 'rt')
        arquivo.close()
    except FileNotFoundError:
        texto = f'ARQUIVO "{nome_arquivo}.txt" NÃO ENCONTRADO'
        linhas(texto)
        sleep(1)
        return False
    else:
        texto = f'ARQUIVO "{nome_arquivo}.txt" ENCONTRADO'
        linhas(texto)
        sleep(1)
        return True


def criar_arquivo(nome_arquivo):
    from time import sleep

    try:
        arquivo = open(nome_arquivo + '.txt', 'wt+')
        arquivo.close()
    except:
        print('ERRO AO CRIAR ARQUIVO')
        sleep(1)
    else:
        print(f'ARQUIVO "{nome_arquivo}.txt" CRIADO')
        print('=' * (15 + int(len(nome_arquivo))))
        sleep(1)


def escrever_senhas(nome_arquivo, nome, complementar):
    from time import sleep

    try:
        arquivo = open(nome_arquivo + '.txt', 'at')
    except:
        print('ERRO AO TENTAR ABRIR ARQUIVO PARA ESCRITURA')
        sleep(0.5)
    else:
        if len(nome) >= 6:
            print(nome)
            arquivo.write(nome + '\n')

        for item in complementar:
            print(nome + item)
            arquivo.write(nome + item + '\n')
            sleep(0.2)
    finally:
        arquivo.close()