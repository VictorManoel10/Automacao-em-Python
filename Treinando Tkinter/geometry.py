from tkinter import *

janela = Tk()

a = Button(janela, text="Usando place")
a.place(x=100, y=100)
b = Button(janela, text="Usando place 2")
b.place(x=50, y=50)

janela.mainloop()