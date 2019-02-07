# João 8:32 "E conhecereis a verdade, e a verdade vos libertará."
from datetime import datetime
import os
#
class Leitores:
    def BDleitores(self):
        sublocal = os.listdir()
        p = False

        for x in sublocal:
            if x == "leitores.txt":
                p = True
        if p == False:
            txt = open("leitores.txt", "w")
            txt.write("BANCO DE DADOS: LEITORES\n")
            txt.write("--------------------------------------------------------\n")
            txt.write("LEITORES CADASTRADOS: \n")
            txt.close()
            p = True
#
class Livros:
    def BDlivros(self):
        sublocal = os.listdir()
        p = False

        for x in sublocal:
            if x == "livros.txt":
                p = True
        if p == False:
            txt = open("livros.txt", "w")
            txt.write("BANCO DE DADOS: LIVROS\n")
            txt.write("--------------------------------------------------------\n")
            txt.write("LIVROS CADASTRADOS: \n")
            txt.close()
            p = True
#
class Emprestimos:
    def BDemprestimos(self):
        sublocal = os.listdir()
        p = False

        for x in sublocal:
            if x == "emprestimos.txt":
                p = True
        if p == False:
            txt = open("emprestimos.txt", "w")
            txt.write("BANCO DE DADOS: EMPRESTIMOS\n")
            txt.write("--------------------------------------------------------\n")
            txt.write("EMPRESTIMOS REALIZADOS: \n")
            txt.close()
            p = True
