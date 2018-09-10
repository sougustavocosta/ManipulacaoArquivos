#!/usr/bin/env python
# >> Manipulação de arquivo << #

#Biblioteca utilizada para remoção do arquivo
import os

#Pequeno sistema para demonstração da manipulação de arquivos, totalmente modularizado
#Declração da função menu
def menu():
    opc = -1 #Varivável pelo qual faz meu loop ficar infinito até que o usuário deseje sair.
    while opc != 0:
        print('\nEscolha a opção de manipulação do arquivo:')
        print('0. Sair')
        print('1. CriarArquivo')
        print('2. Escrever')
        print('3. Imprimir')
        print('4. Deletar')
        opc = int(input('~> Digite a opção: '))

        #Verifica se o número digitado é uma opção de escolha do menu
        if opc < 0 or opc > 4:
            print('Você digitou uma opção inválida!')
        elif opc == 0:
            print('Obrigado, até a próxima!')
            exit()
        elif opc == 1: #Caso o usuário tenha digitado a opção 1 - Cria arquivo
            file = criarArquivo()
        elif opc == 2:#Caso o usuário tenha digitado a opção 2 - Escrever no arquivo
            x = int(input('O arquivo já está criado!? (1 -> Sim | 2 - > Não): '))
            if x == 1:
                nomeArquivo = input('Digite o nome do arquivo e sua extensão (dados.txt): ')
                escreverArquivo(nomeArquivo)
            elif x == 2:
                print('Por favor, realize primeiro a criação do arquivo')
            else:
                print('Você digitou uma opção inválida!')
        elif opc == 3:#Caso o usuário tenha digitado a opção 3 - imprimir arquivo
            nomeArquivo = input('Digite o nome do arquivo e sua extensão (dados.txt): ')
            imprimirArquivo(nomeArquivo)
        elif opc == 4:#Caso o usuário tenha digitado a opção 4 - Deletar arquivo
            nomeArquivo = input('Digite o nome do arquivo e sua extensão (dados.txt): ')
            deletarArquivo(nomeArquivo)

#Função para criação do arquivo
def criarArquivo():
    #Recebo do usário o nome do arquivo e o seu tipo. Ex.: (Documento.pdf, dados.txt, WellPlay.xls)
    nomeArquivo = input('Digite o nome do arquivo e sua extensão (dados.txt): ')

    try:
        #O terceiro parâmetro é opcional e nele especificamos a codificação do arquivo.
        arq = open(nomeArquivo, 'w', encoding="utf8") # w é o parametro de abertura
        print('Arquivo criado com sucesso!')
        return arq
    except: #Tratamento do erro caso não seja possível a criação do arquivo.
        print('Não foi possível criar o arquivo!')

def escreverArquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo, 'a')  # a é o parametro de abertura para escrita
        text = input('Digite o que você desejar inserir no arquivo: ')
        arq.write(text) #Escrita do arquivo
        fecharArquivo(arq) #Chamada da função para fechamento do arquivo
    except:
        print('Não foi possível acessar o arquivo!')

def deletarArquivo(nomeArquivo):
    os.remove(nomeArquivo) #Método para deleção do arquivo.
    return

def imprimirArquivo(nomeArquivo):
    arq = open(nomeArquivo, 'r') # Abertura do arquivo no modo 'r' apenas leitura.
    print(arq.read())# Imprimindo na tela o conteúdo do arq através do método de leitura. Existe outros como por linha (arq.readlines())
    fecharArquivo(arq)
    return

def fecharArquivo(arq):
    arq.close() # Fechando a conexão com o arquivo.



#Inicializo o programa por aqui e tudo acontece dentro das funções
#Esse é o start do programa
opc = menu()