#importando CSV
import csv
from operator import index

lista = ['Mar','14074','o mor','tbest']

#função adicionar
def adicionar_dados(i):
    #acessando o csv
    with open('dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)


#funcao ver dados
def ver_dados():
    dados = []
    #acessando o csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return dados

# funcao remover dados 

def remover_dados(i):
    def adicionar_novalista(j):
        #acessando o csv
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
        ver_dados()


    nova_lista = []
    nome = i
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == nome:
                    nova_lista.remove(linha)

    #adicionando nova lista
    adicionar_novalista(nova_lista)





# funcao atualizar dados 
def atualizar_dados(i):
    def adicionar_novalista(j):
        #acessando o csv
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
        ver_dados()


    nova_lista = []
    nome = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == nome:
                    nome = i[1]
                    data = i[2]
                    assunto = i[3]
                    obs = i[4]

                    dados = [nome, data, assunto, obs]

                    #trocando lista por index
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados

    #adicionando nova lista
    adicionar_novalista(nova_lista)




#funcao pesquisar dados
def pesquisar_dados(i):
    dados = []
    nome = i
    #acessando o csv
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == nome:
                    dados.append(linha)
    return dados

print(pesquisar_dados('Marcell'))