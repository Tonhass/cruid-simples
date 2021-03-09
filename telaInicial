from tkinter import *
from tkinter import Tk

from pessoa.Lista import Lista
from pessoa.novaPessoa import novaPessoa


class TelaInicial:
    def __init__(self):
        self.win = Tk()

        self.win.title("CRUID")

        self.lbTitulo= Label(self.win, text="CRUID", bg="#00FFFF", foreground="Black", font=("Georgia", 20, 'bold'))
        self.lbTitulo.place(x=200,y=75)

        self.btLogin = Button(self.win, text="INSERIR NOVA PESSOA", font=('Georgia', 13, 'bold')
                             , width=20, bg='#48D1CC', fg='white', command= self.Inserir)
        self.btLogin.place(x=128, y=170)

        self.btCadastrar = Button(self.win, text="LISTAR", font=('Georgia', 13, 'bold')
                                  , width=20, bg='#48D1CC', fg='white',command=self.Listar)
        self.btCadastrar.place(x=128, y=220)


        self.win.resizable(width=False, height=False)
        self.win["background"] = "#00FFFF"
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 400 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "500x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.mainloop()

    def Inserir(self):
        self.win.destroy()
        novaPessoa()
    def Listar(self):
        self.win.destroy()
        Lista()



TelaInicial()
