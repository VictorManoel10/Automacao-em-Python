from tkinter import *

janela = Tk()

vermelho = Button(janela, text="Vermelho", fg="red")
vermelho.pack(side=TOP)

verde = Button(janela, text="Verde", fg="green")
verde.pack(side=LEFT)

amarelo = Button(janela, text="Amarelo", fg="yellow")
amarelo.pack(side=RIGHT)

azul = Button(janela, text="Azul", fg="blue")
azul.pack(side=BOTTOM)

janela.mainloop()
