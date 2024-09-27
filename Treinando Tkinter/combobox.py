from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Criando um Combobox")
janela.geometry("300x300")

combo = Combobox(janela)
combo["values"]= (1, 2, "Victor", "Brasil")
combo.current(2)
combo.grid(row=0, column=0)


def obter(eventObject):
    v = combo.get()
    lb = Label(janela, text=v)
    lb.grid(row=1, column=0)


combo.bind("<<ComboboxSelected>>",obter)   

janela.mainloop()