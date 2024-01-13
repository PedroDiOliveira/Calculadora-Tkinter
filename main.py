#########################################
##Treinando TKinter com uma calculadora##
#########################################

###########
##imports##
###########

from tkinter import *
from tkinter import font

################################
##janela principal de execucao##
################################

janela = Tk()
janela.title("Simple Calculator")
janela.configure(background = "#0d192b")
janela.geometry('570x707+700+200')
janela.resizable(False, False)


####################
##Janela resultado##
####################

frame = Frame(janela, width = 550, height = 100, background = "#09c184")
frame.grid(padx = 10, pady =15)
frame2 = Frame(frame, width = 530, height = 130, background = "#0a8967")
frame2.grid(padx = 10, pady = 10)


###########
##Teclado##
###########


frame_teclado = Frame(janela, width = 550, height = 600, background = "#0a8967")
frame_teclado.grid(padx = 10, pady = 10, sticky = "nsew")

reset = Button(frame_teclado, text = "C", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
reset.grid(row = 0, column = 0, padx = 10, pady = 15 )

troca_valor = Button(frame_teclado, text = "+/-", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
troca_valor.grid(row = 0, column = 1, padx = 10, pady = 15 )

porcentagem = Button(frame_teclado, text = "%", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
porcentagem.grid(row = 0, column = 2, padx = 10, pady = 15 )

divisao = Button(frame_teclado, text = "/", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
divisao.grid(row = 0, column = 3, padx = 10, pady = 15 )

multiplicacao = Button(frame_teclado, text = "x", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
multiplicacao.grid(row = 1, column = 3, padx = 10, pady = 15 )

subtracao = Button(frame_teclado, text = "-", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
subtracao.grid(row = 2, column = 3, padx = 10, pady = 15 )

adicao = Button(frame_teclado, text = "+", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
adicao.grid(row = 3, column = 3, padx = 10, pady = 15 )

igual = Button(frame_teclado, text = "=", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
igual.grid(row = 4, column = 3, padx = 10, pady = 15 )

ponto = Button(frame_teclado, text = ".", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
ponto.grid(row = 4, column = 2, padx = 10, pady = 15 )

num_1 = Button(frame_teclado, text = "1", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_1.grid(row = 1, column = 0, padx = 10, pady = 15 )

num_2 = Button(frame_teclado, text = "2", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_2.grid(row = 1, column = 1, padx = 10, pady = 15 )

num_3 = Button(frame_teclado, text = "3", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_3.grid(row = 1, column = 2, padx = 10, pady = 15 )

num_4 = Button(frame_teclado, text = "4", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_4.grid(row = 2, column = 0, padx = 10, pady = 15 )

num_5 = Button(frame_teclado, text = "5", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_5.grid(row = 2, column = 1, padx = 10, pady = 15 )

num_6 = Button(frame_teclado, text = "6", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_6.grid(row = 2, column = 2, padx = 10, pady = 15 )

num_7 = Button(frame_teclado, text = "7", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_7.grid(row = 3, column = 0, padx = 10, pady = 15 )

num_8 = Button(frame_teclado, text = "8", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_8.grid(row = 3, column = 1, padx = 10, pady = 15 )

num_9 = Button(frame_teclado, text = "9", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_9.grid(row = 3, column = 2, padx = 10, pady = 15 )

num_0 = Button(frame_teclado, text = "0", height = 4, width = 15, background = "#0c5149", activebackground = "#0d192b", fg = "white")
num_0.grid(row = 4, column = 0, columnspan = 2, sticky = "ew", padx = 10, pady = 15 )



janela.mainloop()
