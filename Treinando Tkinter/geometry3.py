from tkinter import *

janela = Tk()
janela.geometry('200x200')

vermelha = Button(janela, text="vermelha", fg="red")
vermelha.grid(column=1, row=0)

verde = Button(janela, text="verde", fg="green")
verde.grid(column=0, row=0)

azul = Button(janela, text="azul", fg="blue")
azul.grid(column=2, row=1)


janela.mainloop()
