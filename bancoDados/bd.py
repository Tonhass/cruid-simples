import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Projeto"
)

cursor = conexao.cursor()

def Cadastrar(dados):
    cursor.execute("INSERT INTO pessoa(Nome, Sobrenome, Nascimento, Logradouro, Numero, Bairro, Cidade, Estado, CEP, Sexo) VALUES "
                   "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", dados)
    conexao.commit()
    return True

def Listar():
    cursor.execute("SELECT * FROM projetosefaz.pessoa ORDER BY idPessoa")
    return cursor.fetchall()

def Atualizar(dados):
    cursor.execute("UPDATE `projetosefaz`.`pessoa` SET `Nome` = %s, `Sobrenome` = %s, `Nascimento` = %s, `Logradouro` = %s,\
    `Numero` = %s, `Bairro` = %s, `Cidade` = %s, `Estado` = %s, `CEP` = %s, `Sexo` = %s\
    WHERE(`idPessoa` = %s)", dados)
    conexao.commit()
    return True

def Excluir(dados):
    cursor.execute("DELETE FROM pessoa WHERE idPessoa ="+dados)
    conexao.commit()
    return True



