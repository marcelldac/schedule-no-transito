from tkinter import ttk
from tkinter.tix import Tree
from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox
from turtle import width

from dados import *

#cores -----------------

co0 = "#f0f3f5" #preto
co1 = "#f0f3f5" #ciza
co2 = "#feffff" #branca
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#6f9fbd" #azul
co6 = "#ef5350" #vermelha
co7 = "#93cd95" #verde

#criando janela -----------------------

janela = Tk ()
janela.title ("")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Frames ---------------------------------

frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela,width=500, height=248, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

#configurando frame cima

l_nome = Label(frame_cima, text="NO TRANSITO", anchor=NE, font=('arial 20 bold'), bg=co3, fg=co1)
l_nome.place(x=5,y=5)

l_linha = Label(frame_cima, text='', width=500, anchor=NE, font=('arial 1'), bg=co2, fg=co1)
l_linha.place(x=0,y=46)




global tree
#configurando frame tabela
def mostrar_dados():

    global tree
    #creating a treeview with dual scrollbars
    dados_h = ['Nome','Data', 'Assunto', 'Obs' ]
            
    dados = ver_dados()

    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree cabeçalho

    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Data', anchor=NW)
    tree.heading(2, text='Assunto', anchor=NW)
    tree.heading(3, text='Obs', anchor=NW)

    #tree corpo

    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=120, anchor='nw')
            
    for item in dados:
        tree.insert('', 'end', values=item)


mostrar_dados()



#funcao inserir

def inserir():
    nome = e_nome.get()
    data = e_data.get()
    assunto = e_assunto.get()
    obs = e_obs.get()

    dados = [nome, data, assunto, obs]

    if nome == '' or data == '' or assunto == '' or obs == '':
        messagebox.showwarning('Dados', 'Preencha todos os campos(se não tiver oq preencher bota um ".")')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Tudo certo')

        e_nome.delete(0, 'end')
        e_data.delete(0, 'end')
        e_assunto.delete(0, 'end')
        e_obs.delete(0, 'end')

        mostrar_dados()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        data = tree_lista[1]
        assunto = tree_lista[2]
        obs = tree_lista[3]

        e_nome.insert(0,nome)
        e_data.insert(0,data)
        e_assunto.insert(0,assunto)
        e_obs.insert(0,obs)




        def confirmar():
            nome_novo = e_nome.get()
            data = e_data.get()
            assunto = e_assunto.get()
            obs = e_obs.get()

            dados = [nome ,nome_novo, data, assunto, obs]

            print(dados)


            atualizar_dados(dados)

            messagebox.showinfo('Dados', 'Atualizado')

            e_nome.delete(0, 'end')
            e_data.delete(0, 'end')
            e_assunto.delete(0, 'end')
            e_obs.delete(0, 'end')

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar = Button(frame_baixo,command=confirmar, text='Confirmar', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290,y=110)



    except:
        messagebox.showwarning('Dados', 'Selecione um evento na tabela clicando nele')


def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]

        remover_dados(nome)

        messagebox.showinfo('Dados', 'Excluído')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()

    except:
        messagebox.showwarning('Dados', 'Selecione um evento na tabela clicando nele')


def procurar():
    nome = e_procurar.get()

    dados = pesquisar_dados(nome)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0, 'end')

#configruando frame baixo

l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10,y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_nome.place(x=80,y=20)

l_data = Label(frame_baixo, text='Data *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data.place(x=10,y=50)
e_data = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_data.place(x=80,y=50)

l_assunto = Label(frame_baixo, text='Assunto *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_assunto.place(x=10,y=80)
e_assunto = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_assunto.place(x=80,y=80)

l_obs = Label(frame_baixo, text='Obs *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_obs.place(x=10,y=110)
e_obs = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('',10), highlightthickness=1)
e_obs.place(x=80,y=110)

b_procurar = Button(frame_baixo,command=procurar, text='Procurar', anchor=NW, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290,y=20)
e_procurar = Entry(frame_baixo, width=16, justify='left', font=('',10), highlightthickness=1)
e_procurar.place(x=347,y=21)


b_ver = Button(frame_baixo,command=mostrar_dados, text='Ver dados', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290,y=50)

b_adicionar = Button(frame_baixo,command=inserir, text='Adicionar', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=400,y=50)

b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400,y=80)

b_deletar = Button(frame_baixo,command=remover, text='Deletar', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400,y=110)




global tree
#configurando frame tabela
def mostrar_dados():

    global tree
    #creating a treeview with dual scrollbars
    dados_h = ['Nome','Data', 'Assunto', 'Obs' ]
            
    dados = ver_dados()

    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree cabeçalho

    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Data', anchor=NW)
    tree.heading(2, text='Assunto', anchor=NW)
    tree.heading(3, text='Obs', anchor=NW)

    #tree corpo

    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=120, anchor='nw')
            
    for item in dados:
        tree.insert('', 'end', values=item)



mostrar_dados()

janela.mainloop()

