#########################################
##Treinando TKinter com uma calculadora##
#########################################

###########
##imports##
###########

from tkinter import *
from tkinter import font

#############
##Variaveis##
#############

cor_caracter = "#99B4BF"
fundo_botao = "#BF8D30"
fundo_teclado = "#58788C"
fundo_frame = "#58788C"     
borda_frame = "#99B4BF"
cor_janela = "#253C59"

#cor_caracter = "black"
#fundo_botao = "#F2BC8D"
#fundo_teclado = "#73341D"
#fundo_frame = "#73341D"     #cookie
#borda_frame = "#A65F37"
#cor_janela = "#260C07"

#cor_caracter = "black"
#fundo_botao = "#C4EEF2"
#fundo_teclado = "#3F858C"
#fundo_frame = "#3F858C"       #cyano gay
#borda_frame = "#C4EEF2"
#cor_janela = "#025159"

################################
##janela principal de execucao##
################################

janela = Tk()
janela.title("Simple Calculator")
janela.configure(background = cor_janela)
janela.geometry('570x707+700+200')
janela.resizable(False, False)


####################
##Janela resultado##
####################

frame = Frame(janela, width = 550, height = 100, background = borda_frame)
frame.grid(padx = 10, pady =15)
frame2 = Frame(frame, width = 530, height = 130, background = fundo_frame)
frame2.grid(padx = 10, pady = 10)


###########
##Teclado##
###########



frame_teclado = Frame(janela, width = 550, height = 600, background = fundo_teclado)
frame_teclado.grid(padx = 10, pady = 10, sticky = "nsew")

reset = Button(frame_teclado, text = "C", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
reset.grid(row = 0, column = 0, padx = 10, pady = 15 )

troca_valor = Button(frame_teclado, text = "+/-", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
troca_valor.grid(row = 0, column = 1, padx = 10, pady = 15 )

porcentagem = Button(frame_teclado, text = "%", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
porcentagem.grid(row = 0, column = 2, padx = 10, pady = 15 )

divisao = Button(frame_teclado, text = "/", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
divisao.grid(row = 0, column = 3, padx = 10, pady = 15 )

multiplicacao = Button(frame_teclado, text = "x", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
multiplicacao.grid(row = 1, column = 3, padx = 10, pady = 15 )

subtracao = Button(frame_teclado, text = "-", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
subtracao.grid(row = 2, column = 3, padx = 10, pady = 15 )

adicao = Button(frame_teclado, text = "+", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
adicao.grid(row = 3, column = 3, padx = 10, pady = 15 )

igual = Button(frame_teclado, text = "=", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
igual.grid(row = 4, column = 3, padx = 10, pady = 15 )

ponto = Button(frame_teclado, text = ".", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
ponto.grid(row = 4, column = 2, padx = 10, pady = 15 )

num_1 = Button(frame_teclado, text = "1", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_1.grid(row = 1, column = 0, padx = 10, pady = 15 )

num_2 = Button(frame_teclado, text = "2", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_2.grid(row = 1, column = 1, padx = 10, pady = 15 )

num_3 = Button(frame_teclado, text = "3", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_3.grid(row = 1, column = 2, padx = 10, pady = 15 )

num_4 = Button(frame_teclado, text = "4", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_4.grid(row = 2, column = 0, padx = 10, pady = 15 )

num_5 = Button(frame_teclado, text = "5", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_5.grid(row = 2, column = 1, padx = 10, pady = 15 )

num_6 = Button(frame_teclado, text = "6", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_6.grid(row = 2, column = 2, padx = 10, pady = 15 )

num_7 = Button(frame_teclado, text = "7", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_7.grid(row = 3, column = 0, padx = 10, pady = 15 )

num_8 = Button(frame_teclado, text = "8", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_8.grid(row = 3, column = 1, padx = 10, pady = 15 )

num_9 = Button(frame_teclado, text = "9", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_9.grid(row = 3, column = 2, padx = 10, pady = 15 )

num_0 = Button(frame_teclado, text = "0", height = 4, width = 15, background = fundo_botao, activebackground = "#0d192b", fg = cor_caracter)
num_0.grid(row = 4, column = 0, columnspan = 2, sticky = "ew", padx = 10, pady = 15 )



janela.mainloop()
