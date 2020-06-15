import tkinter as tk

#--------------------------------------------Escritura------------------------------------------
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

#------------------------------------------------Manipulação--------------------------------
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
    """Criará o arquivo que conterá as senhas.

    Args:
        nome_arquivo (str, optional): [Se for dado um argumento, o nome do arquivo será este argumento]. Senão, recebe 'passwords'.
    """
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
    """Escreverá as senhas no arquivo.

    Args:
        nome_arquivo (str): O nome do arquivo que contem as senhas.
        nome (str): O nome da pessoa, ou nomes concatenados.
        complementos (list): São os dados que serão concatenados com o [nome].
    """
    try:
        arquivo = open(nome_arquivo + '.txt', 'at')
    except:
        labelResposta = tk.Label(mainFrame, text='Error trying to open writing file..', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
        labelResposta.grid(row=5, columnspan=4)
    else:
        if len(nome) >= 6:
            arquivo.write(nome + '\n')

        for item in complementos:
            if len(nome + item) >= 6:
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

def combinacao_permutacao_metodo(elementos, nome_arquivo, complementos):
    """Gerará todas as combinações e permutações possíveis de senhas e para cada, concatenará com os complementos.

    Args:
        elementos ([list]): [São os nomes, sobrenomes e apelidos. Juntos em uma lista.]
        nome_arquivo ([str]): [É o nome do arquivo que foi criado anteriormente.]
        complementos ([list]): [São uma série de strings que normalmente são concatenados com alguma senha.]
    """
    from itertools import permutations, combinations

    stop = len(elementos)

    while stop != 0:
        combinacoes = combinations(elementos, stop)
        stop -= 1

        for combinacao in combinacoes:
            permutacoes = permutations(combinacao)

            for permutacao in permutacoes:
                escrever_senhas(nome_arquivo, ''.join(permutacao), complementos)

def calcular_senhas_permutacao(elementos):
    """Contará, aproximadamente, quantas senhas serão escritas através do método de permutação.

    Args:
        elementos (list): São os nomes, sobrenomes e apelidos juntos em uma lista.

    Returns:
        int: Quantas senhas, aproximadamente serão geradas.
    """
    from math import factorial
    from itertools import combinations

    resultado = 0
    p = len(elementos)

    while p != 0:
        total = 0
        for combinacao in combinations(elementos, p):
            total += 1

        resultado += (factorial(p) * 8) * total
        p -= 1

    return resultado

def probabilidade_metodo(nome, nome_arquivo, complementos, sobrenomes, dados_nascimento, apelidos):
    """Criará diversas senhas, que terão uma maior probabilidade de serem a correta.

    Args:
        nome (str): O nome, ou apelido, ou nome concatenado com alguma coisa.
        nome_arquivo (str): O nome do arquivo que foi criado anteriormente.
        complementos (list): Uma série de strings que normalmente são concatenadas com um nome para formar uma senha.
        sobrenomes (list): Uma lista com os sobrenomes.
        dados_nascimento (str): A data de nascimento da pessoa.
        apelidos (list): Uma lista com os apelidos.
    """
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
            if sobrenome_pequeno != '':
                escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

            if len(sobrenomes) == 0:
                escrever_senhas(nome_arquivo, apelido, complementos)
            elif len(sobrenomes) == 1:
                escrever_um_nome(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 2:
                escrever_dois_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 3:
                escrever_tres_nomes(nome_arquivo, apelido, sobrenomes, complementos)
            elif len(sobrenomes) == 4:
                escrever_quatro_nomes(nome_arquivo, apelido, sobrenomes, complementos)

    for surname in sobrenomes:
        if sobrenome_pequeno != '':
            escrever_senhas(nome_arquivo, apelido + sobrenome_pequeno, complementos)

        escrever_senhas(nome_arquivo, surname, complementos)
    
    contar_senhas_probabilidade(nome_arquivo)

def escrever_resposta(texto):
    labelResposta['text'] = texto

def contar_senhas_probabilidade(nome_arquivo):
    """Após a escritura do método de probalidade, esta função todo o arquivo de senhas, contando uma por uma.

    Args:
        nome_arquivo (str): O nome do arquivo com as senhas
    """
    with open(nome_arquivo + '.txt') as arquivo:
        total = 0

        for linha in arquivo:
            total += 1

    escrever_resposta(f'Passwords Written {total}')

def tamanho_popup(elementos):
    import os

    if os.name == 'nt':
        width = 5.5 * (41 + len(str(calcular_senhas_permutacao(elementos))))
    else:
        width = 7 * (41 + len(str(calcular_senhas_permutacao(elementos))))

    return width

def verificar_entrys():
    """Verifica se o usuário digitou os argumentos necessários. Se sim, cria algumas variáveis necessárias e chama outras funções, passando como parâmetro estas variáveis.
    """
    if len(entryNome.get().split()) == 0 and len(entryNascimento.get()) == 0 and len(entryApelido.get().split()) == 0:
        labelResposta['text'] = 'Fill in the fields above!'
    else:
        nome = ''
        sobrenomes = list()
        complementos = criar_complementos(entryNascimento.get())

        if len(entryNome.get().split()) != 0:
            for nomes in entryNome.get().split():
                if nomes == entryNome.get().split()[0]:
                    nome = nomes
                    nome_arquivo = nome
                else:
                    sobrenomes.append(nomes)
        else:
            nome_arquivo = 'passwords'

        if not verificar_arquivo(nome_arquivo):
            criar_arquivo(nome_arquivo)

        if marcadorRadio.get() == 1:
            probabilidade_metodo(nome, nome_arquivo, complementos, sobrenomes, entryNascimento.get(), entryApelido.get().split())
        else:
            def init_permutation():
                popUp.destroy()
                combinacao_permutacao_metodo(elementos, nome_arquivo, complementos)
                labelResposta['font'] = 'Arial 13'
                labelResposta['text'] = f'Passwords written: {calcular_senhas_permutacao(elementos)}.'

            elementos = list()
            elementos.append(nome)
            for sobrenome in sobrenomes: elementos.append(sobrenome)
            for apelido in entryApelido.get().split(): elementos.append(apelido)

            popUp = tk.Toplevel(root, bg='#0F0F0F')
            popUp.title('Note')

            height = 70
            width = tamanho_popup(elementos)
            posy = (root.winfo_screenheight() / 2) - (height / 2)
            posx = (root.winfo_screenwidth() / 2) - (width / 2)
            popUp.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
            if calcular_senhas_permutacao(elementos) > 100000:
                topLabel = tk.Label(popUp, text=f'Approximately {calcular_senhas_permutacao(elementos)} passwords will be written.\nThis may take a while...', bg='#0F0F0F', fg='#ffffff')
            else:
                topLabel = tk.Label(popUp, text=f'Approximately {calcular_senhas_permutacao(elementos)} passwords will be written.', bg='#0F0F0F', fg='#ffffff')
            botao1 = tk.Button(popUp, text='Ok', command=init_permutation)
            topLabel.grid(row=0, column=0, sticky='we')
            botao1.grid(row=1, column=0)

#inicio
root = tk.Tk()
height = 600
width = 700
#O ícone está fazendo com que o executável do programa não rode. Retirando ícone enquanto não é resolvido.
#root.iconphoto(True, tk.PhotoImage(file='files/kreator-logo-100x100.png'))
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
radioButton2 = tk.Radiobutton(mainFrame, text='Permutation', variable=marcadorRadio, value=2, font='Arial 12')
radioButton1.grid(row=3, column=1, sticky='w')
radioButton2.grid(row=3, column=1, sticky='e')
radioButton1.select()

labelResposta = tk.Label(mainFrame, font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
labelResposta.grid(row=5, columnspan=4)

botaoNome = tk.Button(mainFrame, text='Run', font='Arial 20', command=lambda: verificar_entrys())
botaoNome.grid(row=4, column=0, columnspan=4, sticky='we')

root.mainloop()
