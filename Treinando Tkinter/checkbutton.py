from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Primeiro Checkbutton")
janela.geometry("200x200")

def test():
    print("Valor do checkbutton: ",estado.get())


estado = BooleanVar()

check = Checkbutton(janela, text="Escolha", var=estado, onvalue=True, offvalue=False, command=test)
check.grid(column=0, row=0)

estado.set(False)

janela.mainloop()
