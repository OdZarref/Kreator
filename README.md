# Kreator
Kreator é um programa que dado certas informações sobre alguém, te entrega uma wordlist com as mais prováveis senhas do indivíduo.

![Demo Gif](showcase/demo.gif)

## Instalação
Para rodar o programa são necessários certos passos. Que dependem do sistema do usuário.  

**Linux**:  
É necessário ter o git instalado, caso não tenha:  
`sudo apt install git`  

Clone o repositório localmente:  
`git clone https://github.com/Odzarref/Kreator`

Abra o terminal no diretório do repositório clonado e
digite.  
`python3 kreator.py`

**Windows**:  
Instale o Python:  
https://www.python.org/downloads/

Instale o git:  
https://git-scm.com/downloads

Clone o repositório localmente:  
`git clone https://github.com/Odzarref/Kreator`

Abra o cmd ou Powershell na pasta projeto clonado e escreva:  
`python kreator.py`


## Como usar
Coloque as informações pedidas pelo programa, estas são:

**Nome completo**: Aceita o nome junto com os sobrenomes, apenas o nome e nenhum dado (enter).  
obs: Caso nenhum nome seja dado, o arquivo com as senhas receberá "passwords.txt". Caso sim, o arquivo receberá o nome dado.  
**Data de nascimento**: O nascimento ou nenhum dado (enter).  
**Apelido**: Aceita um ou mais apelidos. Quando mais de um apelido, utilize um espaço para separá-los.


## Progresso
* [x] Criação do projeto
* [x] Leitura e escritura de senhas baseadas em nome completo, data de nascimento e apelidos.
* [] Leitura e escritura de senhas baseadas em país e informações adicionais.
* [] Opção de escritura de todas as combinações possíveis de senhas