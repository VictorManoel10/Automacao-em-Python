from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Primeiro RadioButton")
janela.geometry("200x200")

def obter():
    print("O valor do botão selecionado é: ", selecionado.get())

selecionado = BooleanVar()

rad_1 = Radiobutton(janela, text="Primeiro", value=0, var=selecionado, command=obter)
rad_1.grid(column=0, row=0)

rad_2 = Radiobutton(janela, text="Segundo", value=1, var=selecionado, command=obter)
rad_2.grid(column=0, row=1)


janela.mainloop()
