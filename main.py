# João 8:32 "E conhecereis a verdade, e a verdade vos libertará."
import time
import os
import time
from datetime import datetime
from datetime import timedelta

import run

run.Leitores.BDleitores(None)
run.Livros.BDlivros(None)
run.Emprestimos.BDemprestimos(None)

#
print("            BEM VINDO À BIBLIOTECA ULTIMATE")
print("----------------------------------------------------------")
print("Para iniciar, selecione a opção desejada:  ")
#
while True:
    print("1 para registrar novo empréstimo")
    print("2 para cadastrar novo leitor")
    print("3 para cadastrar novo livro ao acervo")
    menu = int(input("0 para finalizar o programa: "))
    print("")
    #
    if menu == 0:
        break
    #
    if menu == 1:
        nome_leitor = str(input("Entre com o nome completo do leitor: ").upper())
        livro = str(input("Nome do livro: ").upper())
        spc = str(input("É especial? S/N: ").upper())
        if str(nome_leitor) in open("leitores.txt").read() and str(livro) in open("livros.txt").read():
            if spc == "S":
                x = open("emprestimos.txt","a")
                x.write(str(nome_leitor)+"\n")
                x.write(str(livro)+"\n")
                x.write(str((datetime.now() + timedelta(days=7)))+"\n")
                x.write("-------------------------------------------------------------------------")
                x.close()
                print("")
                print("Emprestimo efetuado com sucesso!")
                print(("Devolução para {0}").format((datetime.now() + timedelta(days=7))))
                print("")
            if spc == "N":
                x = open("emprestimos.txt", "a")
                x.write(str(nome_leitor) + "\n")
                x.write(str(livro) + "\n")
                x.write(str((datetime.now() + timedelta(days=15))) + "\n")
                x.write("-------------------------------------------------------------------------")
                x.close()
                print("")
                print("Emprestimo efetuado com sucesso!")
                print(("Devolução para {0}").format((datetime.now() + timedelta(days=15))))
                print("")
        else:
            print("")
            print("Leitor ou livro não consta no banco de dados ")
            print("")
    if menu == 2:
        novo_leitor = str(input("Entre com o nome completo: ").upper())
        email = str(input("Entre com o endereço: ").upper())
        tel = str(input("Entre com o numero de telefone: ").upper())
        if str(novo_leitor) in open("leitores.txt").read():
            print("")
            print("O leitor já é cadastrado")
            print("")
        else:
            x = open("leitores.txt","a")
            x.write(str(novo_leitor)+"\n")
            x.write(str(email) + "\n")
            x.write(str(tel) + "\n")
            x.write("-------------------------------------------------------------------------")
            x.close()
    if menu == 3:
        novo_livro = str(input("Entre com o nome do livro: ").upper())
        autor = str(input("Nome do autor: ").upper())
        genero = str(input("Genero do livro: "))
        if str(novo_livro) in open("livros.txt").read():
            print("")
            print("O livro já é cadastrado")
            print("")
        else:
            x = open("livros.txt","a")
            x.write(str(novo_livro) + "\n")
            x.write(str(autor) + "\n")
            x.write(str(genero) + "\n")
            x.write("-------------------------------------------------------------------------")
            x.close()






