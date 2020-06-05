import tkinter as tk

def remove_sobrenome_pequeno(nome, sobrenomes):
    """Se a pessoa tiver um sobrenome menor que quatro letras, este sobrenome será removido para ser escrito aparte.
    
    Arguments:
        nome {str} -- Nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
    
    Returns:
        list() -- A lista sem o sobrenome pequeno
    """
    for sobrenome in sobrenomes:
        if len(sobrenome) <= 3:
            sobrenomes.remove(sobrenome)

    return sobrenomes


def criar_complementos(nascimento):
    """Cria os complementos que serão concatenados com os dados do nome completo
    
    Arguments:
        nascimento {str} -- A data de nascimento da pessoa
    
    Returns:
        list() -- Uma lista com todos os complementos gerados
    """
    complementos = ['123', '1234', '12345']

    if len(nascimento) == 8:
        complementos.append(nascimento[0:2])
        complementos.append(nascimento[-2:])
        complementos.append(nascimento[-4:])

        numero = int(nascimento[-2:])
        if numero < 10:
            complementos.append(nascimento[-1])

    return complementos


def concatenar_sobrenome_pequeno(nome, sobrenomes):
    """Concatenará o sobrenome pequeno o sobrenome que vier à frente.
    
    Arguments:
        nome {str} -- Nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
    
    Returns:
        str -- sobrenome_pequeno + o sobrenome que vier à frente.
    """
    sobrenome_pequeno = ''

    for pos, sobrenome in enumerate(sobrenomes):
        if len(sobrenome) <= 3:
            sobrenome_pequeno = sobrenome + sobrenomes[pos + 1]

    return sobrenome_pequeno


def verificar_arquivo(nome_arquivo='passwords'):
    """Verifica se o arquivo que conterá as senhas já existe.
    
    Keyword Arguments:
        nome_arquivo {str} -- (default: {'passwords'})
    
    Returns:
        [bool] -- [Se já existir recebe True, senão recebe False]
    """
    from time import sleep

    try:
        arquivo = open(nome_arquivo + '.txt', 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo='passwords'):
    try:
        arquivo = open(nome_arquivo + '.txt', 'wt+')
        arquivo.close()
    except:
        print('Error creating arquivo.')


def escrever_senhas_nascimento(nome_arquivo, data_nascimento):
    """Escreve como senha somente a data de nascimento.
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo onde será escrito
        data_nascimento {str} -- A data de nascimento
    """
    
    arquivo = open(nome_arquivo + '.txt', 'at')
    arquivo.write(data_nascimento + '\n')
    print(data_nascimento)
    arquivo.write(data_nascimento[0:4] + data_nascimento[-2:] + '\n')
    print(data_nascimento[0:4] + data_nascimento[-2:])


def escrever_senhas(nome_arquivo, nome, complementos):
    try:
        arquivo = open(nome_arquivo + '.txt', 'at')
    except:
        labelResposta = tk.Label(mainFrame, text='Error trying to open writing file..', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
        labelResposta.grid(row=5, columnspan=4)
    else:
        if len(nome) >= 6:
            print(nome)
            arquivo.write(nome + '\n')

        for item in complementos:
            if len(nome + item) >= 6:
                print(nome + item)
                arquivo.write(nome + item + '\n')
    finally:
        arquivo.close()


def escrever_um_nome(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará o nome com o único sobrenome
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo que será aberto para escritura
        nome {str} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_dois_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {str} -- Nome do arquivo que será aberto para escritura
        nome {str} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_tres_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {[type]} -- Nome do arquivo que será aberto para escritura
        nome {[type]} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)


def escrever_quatro_nomes(nome_arquivo, nome, sobrenomes, complementos):
    """Concatenará os dados do nome de forma específica para o comprimento do nome.
    
    Arguments:
        nome_arquivo {[type]} -- Nome do arquivo que será aberto para escritura
        nome {[type]} -- Primeiro nome da pessoa
        sobrenomes {list()} -- Os sobrenomes da pessoa
        complementos {list()} -- Os dados que será concatenados para a formação de diferentes senhas
    """
    concatenacao = nome + sobrenomes[0] 
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[3]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2]
    escrever_senhas(nome_arquivo, concatenacao, complementos)
    concatenacao = nome + sobrenomes[0] + sobrenomes[1] + sobrenomes[2] + sobrenomes[3]

def arquivo(dados_nome, dados_nascimento, apelidos):
    nome = ''
    sobrenomes = list()
    complementos = criar_complementos(dados_nascimento)

    if len(dados_nome) != 0:
        for nomes in dados_nome:
            if nomes == dados_nome[0]:
                nome = nomes
                nome_arquivo = nome
            else:
                sobrenomes.append(nomes)
    else:
        nome_arquivo = 'passwords'
        
    verificar_arquivo1 = verificar_arquivo(nome_arquivo)
    if not verificar_arquivo1:
        criar_arquivo(nome_arquivo)

    if len(dados_nascimento) != 0:
        escrever_senhas_nascimento(nome_arquivo, dados_nascimento)

    if nome != '':
        escrever_senhas(nome_arquivo, nome, complementos)

    sobrenome_pequeno = concatenar_sobrenome_pequeno(nome, sobrenomes)

    if sobrenome_pequeno != '':
        escrever_senhas(nome_arquivo, nome + sobrenome_pequeno, complementos)
        
    sobrenomes = remove_sobrenome_pequeno(nome, sobrenomes)

    if len(sobrenomes) == 0:
        escrever_senhas(nome_arquivo, nome, complementos)
    elif len(sobrenomes) == 1:
        escrever_um_nome(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 2:
        escrever_dois_nomes(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 3:
        escrever_tres_nomes(nome_arquivo, nome, sobrenomes, complementos)
    elif len(sobrenomes) == 4:
        escrever_quatro_nomes(nome_arquivo, nome, sobrenomes, complementos)

    if len(apelidos) > 0:
        for apelido in apelidos:
            if len(sobrenomes) == 0:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_senhas(nome_arquivo, apelido, complementos)

            elif len(sobrenomes) == 1:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_um_nome(nome_arquivo, apelido, sobrenomes, complementos)

            elif len(sobrenomes) == 2:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_dois_nomes(nome_arquivo, apelido, sobrenomes, complementos)

            elif len(sobrenomes) == 3:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

                escrever_tres_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 4:
                if sobrenome_pequeno != '':
                    escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)
                    
                escrever_quatro_nomes(nome_arquivo, apelido, sobrenomes, complementos)

    for surname in sobrenomes:
        if sobrenome_pequeno != '':
            escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

        escrever_senhas(nome_arquivo, surname, complementos)
    
    conta_senhas(nome_arquivo)
    
def conta_senhas(nome_arquivo):
    with open(nome_arquivo + '.txt') as arquivo:
        total = 0

        for linha in arquivo:
            total += 1

    labelResposta = tk.Label(mainFrame, text=f'Passwords written {total}.', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
    labelResposta.grid(row=5, columnspan=4)

def verificar_entrys():
    if len(entryNome.get().split()) == 0 and len(entryNascimento.get()) == 0 and len(entryApelido.get().split()) == 0:
        labelResposta = tk.Label(mainFrame, text='Fill in the fields above!.', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
        labelResposta.grid(row=5, columnspan=4)
    else:
        arquivo(entryNome.get().split(), entryNascimento.get(), entryApelido.get().split())

#inicio
root = tk.Tk()
height = 600
width = 700
posy = (root.winfo_screenheight() / 2) - (height / 2)
posx = (root.winfo_screenwidth() / 2) - (width / 2)
root.title('Kreator')
root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
root.resizable(False, False)
marcadorRadio = tk.IntVar()

#botoes, labels e Frames
labelBackgroundRoot = tk.Label(root, bg='#0F0F0F')
labelBackgroundRoot.place(relheight=1, relwidth=1)

mainFrame = tk.Frame(root, bg='#0F0F0F', bd=5)
mainFrame.place(relx=0.25, rely=0.1, relwidth=0.8, relheight=0.8)

labelNome = tk.Label(mainFrame, text='Full Name', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
labelNome.grid(row=0, column=0)
entryNome = tk.Entry(mainFrame, font='Arial 15', fg='#ffffff', bg='#0F0F0F')
entryNome.grid(row=0, column=1)

labelNascimento = tk.Label(mainFrame,text='Birth Date', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
labelNascimento.grid(row=1, column=0)
entryNascimento = tk.Entry(mainFrame, font='Arial 15', fg='#ffffff', bg='#0F0F0F')
entryNascimento.grid(row=1, column=1)

labelApelido = tk.Label(mainFrame, text='Nicknames', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
labelApelido.grid(row=2, column=0)
entryApelido = tk.Entry(mainFrame, font='Arial 15', fg='#ffffff', bg='#0F0F0F')
entryApelido.grid(row=2, column=1)

labelMetodo = tk.Label(mainFrame, text='Method', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
labelMetodo.grid(row=3, column=0)
radioButton1 = tk.Radiobutton(mainFrame, text='Probability', variable=marcadorRadio, value=1, font='Arial 12')
radioButton2 = tk.Radiobutton(mainFrame, text='Combinatory', variable=marcadorRadio, value=2, font='Arial 11')
radioButton1.grid(row=3, column=1, sticky='w')
radioButton2.grid(row=3, column=1, sticky='e')
radioButton1.select()

botaoNome = tk.Button(mainFrame, text='Run', font='Arial 20', command=lambda: verificar_entrys())
botaoNome.grid(row=4, column=0, columnspan=4, sticky='we')

root.mainloop()
