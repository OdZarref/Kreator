import tkinter as tk
from libs.file_writing import *
from libs.text_manipulation import *
from libs.input import *

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

#inicio
root = tk.Tk()
height = 600
width = 700
posy = (root.winfo_screenheight() / 2) - (height / 2)
posx = (root.winfo_screenwidth() / 2) - (width / 2)
root.title('Kreator')
root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
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

botaoNome = tk.Button(mainFrame, text='Run', font='Arial 20', command=lambda: verificar())
botaoNome.grid(row=4, column=0, columnspan=4, sticky='we')


def verificar():
    if len(entryNome.get().split()) == 0 and len(entryNascimento.get()) == 0 and len(entryApelido.get().split()) == 0:
        labelResposta = tk.Label(mainFrame, text='No arguments have been entered.', font='Arial 20', fg='#ffffff', bg='#0F0F0F', pady=10)
        labelResposta.grid(row=5)
    else:
        arquivo(entryNome.get().split(), entryNascimento.get(), entryApelido.get().split())

root.mainloop()


#     nome = ''
# sobrenomes = list()
# dados_nome = entryNome.get().split()
# dados_nascimento = entryNascimento.get()
# apelidos = entryApelido.get().split()