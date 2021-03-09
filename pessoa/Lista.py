from tkinter import *
from tkinter import Tk,ttk,messagebox

from bancoDados import bd
from bancoDados.bd import Listar, Excluir



class Lista:
    def __init__(self):
        self.win = Tk()

        self.win.title("Lista")

        self.win.canvas = Canvas(self.win, height=75, width=1000, bg='#48D1CC')
        self.win.canvas.pack()
        self.win.canvas.place(x=0, y=0)

        self.lbTitulo = Label(self.win, text="Lista", bg="#48D1CC", foreground="white",
                               font=("Georgia", 20, 'bold'))
        self.lbTitulo.place(x=370, y=25)

        self.win.canvasLista = Canvas(self.win, height=200, width=763, bg='#C0C0C0')
        self.win.canvasLista.pack()
        self.win.canvasLista.place(x=10, y=90)
        self.lista_canvas()

        self.lista = Listar()
        #
        for i in self.lista:
            self.listaPess.insert("",END, values=i)

        self.listaPess = ttk.Treeview(self.win.canvasLista)
        self.listaPess['show'] = 'headings'

        s= ttk.Style(self.win.canvasLista)
        s.theme_use("clam")

        #
        self.lbId = Label(self.win, text="Informe o id da pessoa\ncaso queira excluir os dados.", bg="#00FFFF", foreground="Black",
                          font=("Georgia", 10, 'bold'))
        self.lbId.place(x=285, y=330)

        self.txtId = Entry(self.win, font=('Georgia', 10), width=4)
        self.txtId.place(x=497, y=340)


        self.btVoltar = Button(self.win, text="Voltar ", font=('Georgia', 13, 'bold')
                                  , width=10, bg='#48D1CC', fg='white',command=self.TelaInicial)
        self.btVoltar.place(x=95, y=328)

        self.btAtualizar = Button(self.win, text="Atualizar ", font=('Georgia', 13, 'bold')
                               , width=10, bg='#48D1CC', fg='white', command=self.Atualizar)
        self.btAtualizar.place(x=560, y=310)

        self.btRemover = Button(self.win, text="Remover ", font=('Georgia', 13, 'bold')
                               , width=10, bg='#48D1CC', fg='white', command=self.Excluirrr)
        self.btRemover.place(x=560, y=350)

        self.win.resizable(width=False, height=False)
        self.win["background"] = "#00FFFF"
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 760 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "800x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.mainloop()

    def lista_canvas(self):#, ,  "",   "",   "",   "",  "",  "",  "",   "",  ""
        self.listaPess = ttk.Treeview(self.win.canvasLista, height=1000, column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11"))
        self.listaPess.heading("#0", text="")
        self.listaPess.heading("#1",text="ID")
        self.listaPess.heading("#2", text="Nome")
        self.listaPess.heading("#3", text="Sobrenome")
        self.listaPess.heading("#4", text="Nascimento")
        self.listaPess.heading("#5", text="Logradouro")
        self.listaPess.heading("#6", text="Número")
        self.listaPess.heading("#7", text="bairro")
        self.listaPess.heading("#8", text="Cidade")
        self.listaPess.heading("#9", text="Estado")
        self.listaPess.heading("#10", text="CEP")
        self.listaPess.heading("#11", text="Sexo")


        self.listaPess.column("#0", minwidth=0,width=0)
        self.listaPess.column("#1", minwidth=0,width=20)
        self.listaPess.column("#2", minwidth=0,width=70)
        self.listaPess.column("#3", minwidth=0,width=80)
        self.listaPess.column("#4", minwidth=0,width=90)
        self.listaPess.column("#5", minwidth=0, width=84)
        self.listaPess.column("#6", minwidth=0, width=54)
        self.listaPess.column("#7", minwidth=0, width=75)
        self.listaPess.column("#8", minwidth=0, width=80)
        self.listaPess.column("#9", minwidth=0, width=60)
        self.listaPess.column("#10", minwidth=0, width=70)
        self.listaPess.column("#11", minwidth=0, width=70)

        self.listaPess.place(x=5, y=5)

    def TelaInicial(self):
        self.win.destroy()
        from telaInicial import TelaInicial
        TelaInicial()

    def Atualizar(self):
        from pessoa.Atualizar import Atualizacao
        self.win.destroy()
        Atualizacao()

    def Excluirrr(self):
        self.ID = str(self.txtId.get())
        data = (
            self.ID
        )
        print(self.ID)
        if self.ID == "":
            messagebox.showinfo("Alerta!", "Campo vazio")
        else:
            res = bd.Excluir(data)
            if res:
                self.win.destroy()
                from telaInicial import TelaInicial
                TelaInicial()