from tkinter import *
from tkinter import Tk, messagebox
from bancoDados import bd

class novaPessoa:
    def __init__(self):
        self.win = Tk()

        self.win.title("Cadastro")

        self.win.canvas = Canvas(self.win, height=75, width=500, bg='#48D1CC')
        self.win.canvas.pack()
        self.win.canvas.place(x=0, y=0)

        self.lbInserir = Label(self.win, text="Inserção", bg="#48D1CC", foreground="white",
                                        font=("Georgia", 15, 'bold'))
        self.lbInserir.place(x=210, y=25)
        #Cadastro de dados da pessoa
        self.lbNome_pessoa = Label(self.win, text="Nome:", bg="#00FFFF", foreground="black",
                                     font=('Georgia', 10, 'bold'))
        self.lbNome_pessoa.place(x=145, y=100)

        self.txtNome_pessoa = Entry(self.win, font=('Georgia', 10))
        self.txtNome_pessoa.place(x=200, y=100)

        self.lbSobrenome_pessoa = Label(self.win, text="Sobrenome:", bg="#00FFFF", foreground="black",
                                   font=('Georgia', 10, 'bold'))
        self.lbSobrenome_pessoa.place(x=105, y=140)

        self.txtSobrenome_pessoa = Entry(self.win, font=('Georgia', 10))
        self.txtSobrenome_pessoa.place(x=200, y=140)

        self.lbNascimento = Label(self.win, text="Nascimento:", bg="#00FFFF", foreground="black",
                                        font=('Georgia', 10, 'bold'))
        self.lbNascimento.place(x=101, y=180)

        self.txtNascimento = Entry(self.win, font=('Georgia', 10))
        self.txtNascimento.place(x=200, y=180)
        #Dados para endereço
        self.lbEndereço = Label(self.win, text="Dados do endereço:", bg="#00FFFF", foreground="black",
                                  font=('Georgia', 10, 'bold'))
        self.lbEndereço.place(x=218, y=210)

        self.lbLogradouro = Label(self.win, text="logradouro:", bg="#00FFFF", foreground="black",
                                  font=('Georgia', 10, 'bold'))
        self.lbLogradouro.place(x=98, y=240)

        self.txtLogradouro = Entry(self.win, font=('Georgia', 10))
        self.txtLogradouro.place(x=200, y=240)

        self.lbNumero = Label(self.win, text="Número:", bg="#00FFFF", foreground="black",
                                   font=('Georgia', 10, 'bold'))
        self.lbNumero.place(x=128, y=280)

        self.txtNumero = Entry(self.win, font=('Georgia', 10))
        self.txtNumero.place(x=200, y=280)

        self.lbBairro = Label(self.win, text="Bairro:", bg="#00FFFF", foreground="black",
                             font=('Georgia', 10, 'bold'))
        self.lbBairro.place(x=142, y=320)

        self.txtBairro = Entry(self.win, font=('Georgia', 10))
        self.txtBairro.place(x=200, y=320)

        self.lbCidade = Label(self.win, text="Cidade:", bg="#00FFFF", foreground="black",
                              font=('Georgia', 10, 'bold'))
        self.lbCidade.place(x=140, y=360)

        self.txtCidade = Entry(self.win, font=('Georgia', 10))
        self.txtCidade.place(x=200, y=360)

        self.lbEstado = Label(self.win, text="Estado:", bg="#00FFFF", foreground="black",
                              font=('Georgia', 10, 'bold'))
        self.lbEstado.place(x=140, y=400)

        self.txtEstado = Entry(self.win, font=('Georgia', 10))
        self.txtEstado.place(x=200, y=400)

        self.lbCep = Label(self.win, text="Cep:", bg="#00FFFF", foreground="black",
                              font=('Georgia', 10, 'bold'))
        self.lbCep.place(x=162, y=440)

        self.txtCep = Entry(self.win, font=('Georgia', 10))
        self.txtCep.place(x=200, y=440)

        #radiobutton
        self.radio_valor = IntVar()
        self.radio_valor.set(1)

        self.lbSexo = Label(self.win, text="Sexo:", bg="#00FFFF", foreground="black",
                           font=('Georgia', 10, 'bold'))
        self.lbSexo.place(x=156, y=480)

        self.radSexoM = Radiobutton(self.win, text='Masculino',bg="#00FFFF",font=('Georgia', 8),
                                  variable=self.radio_valor, value=1)
        self.radSexoM.place(x=200,y=480)

        self.radSexoF = Radiobutton(self.win, text='Feminino', bg="#00FFFF",font=('Georgia', 8),
                                   variable=self.radio_valor, value=2)
        self.radSexoF.place(x=300, y=480)
        #

        self.btCadastrar = Button(self.win, text="Cadastrar ", font=('Georgia', 13, 'bold')
                                  , width=12, bg='#48D1CC', fg='white',command=self.Cadastrar)
        self.btCadastrar.place(x=280, y=520)

        self.btLimpar = Button(self.win, text="Voltar", font=('Georgia', 13, 'bold')
                                  , width=12, bg='#48D1CC', fg='white', command=self.TelaInicial)
        self.btLimpar.place(x=70, y=520)

        self.win.resizable(width=False, height=False)
        self.win["background"] = "#00FFFF"
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 500 / 2)
        y = int(height / 2 - 650 / 2)
        str1 = "500x600+" + str(x) + "+" + str(y)
        self.win.geometry(str1)
        self.win.mainloop()

    def Cadastrar(self):
        self.Nome_pessoa = str(self.txtNome_pessoa.get())
        self.Sobrenome_pessoa = str(self.txtSobrenome_pessoa.get())
        self.Nascimento = str(self.txtNascimento.get())
        self.Logradouro = str(self.txtLogradouro.get())
        self.Numero = str(self.txtNumero.get())
        self.Bairro = str(self.txtBairro.get())
        self.Cidade = str(self.txtCidade.get())
        self.Estado = str(self.txtEstado.get())
        self.CEP = str(self.txtCep.get())
        if self.radio_valor.get() == 1:
            self.Sexo = "Masculino"
        elif self.radio_valor.get() == 2:
            self.Sexo = "Feminino"

        data = (
            self.Nome_pessoa,
            self.Sobrenome_pessoa,
            self.Nascimento,
            self.Logradouro,
            self.Numero,
            self.Bairro,
            self.Cidade,
            self.Estado,
            self.CEP,
            self.Sexo
        )
        self.Limpar()
        if self.Nome_pessoa == "":
            messagebox.showinfo("Alerta!", "Digite o nome")
        elif self.Sobrenome_pessoa == "":
            messagebox.showinfo("Alerta!", "Digite o Sobrenome")
        elif self.Nascimento == "":
            messagebox.showinfo("Alerta!", "Digite o Nascimento")
        elif self.Logradouro == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        elif self.Numero == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        elif self.Bairro == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        elif self.Cidade == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        elif self.Estado == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        elif self.CEP == "":
            messagebox.showinfo("Alerta!", "Digite o Endereço completo")
        else:
            res = bd.Cadastrar(data)
            if res:
                self.win.destroy()
                from telaInicial import TelaInicial
                TelaInicial()



    def Limpar(self):
        self.txtNome_pessoa.delete(0, len(self.txtNome_pessoa.get()))
        self.txtSobrenome_pessoa.delete(0, len(self.txtSobrenome_pessoa.get()))
        self.txtNascimento.delete(0, len(self.txtNascimento.get()))
        self.txtLogradouro.delete(0, len(self.txtLogradouro.get()))
        self.txtNumero.delete(0, len(self.txtNumero.get()))
        self.txtBairro.delete(0, len(self.txtBairro.get()))
        self.txtCidade.delete(0, len(self.txtCidade.get()))
        self.txtEstado.delete(0, len(self.txtEstado.get()))
        self.txtCep.delete(0, len(self.txtCep.get()))

    def TelaInicial(self):
        self.win.destroy()
        from telaInicial import TelaInicial
        TelaInicial()