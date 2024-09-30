from tkinter import *

janela = Tk()
janela.title("ListBox")
janela.geometry("300x200")

def test():
    print(listbox.get(ACTIVE))
    l = Label(janela, text=listbox.get(ACTIVE), width=20)
    l.grid(column=1, row=0)


def deletar():
    listbox.delete(0, END)


listbox = Listbox(janela, height=8)
listbox.grid(column=0, row=0)
listbox.insert(0, "PHP")
listbox.insert(1, "Python")
listbox.insert(2, "MySql")

itens = ["JS", "Java", "C++"]
for i in itens:
    listbox.insert(END, i)

b = Button(janela, text="Imprimir", command=test)
b.grid(column=0, row=1)

bd = Button(janela, text="Deletar", command=deletar)
bd.grid(column=0, row=2)

janela.mainloop()
