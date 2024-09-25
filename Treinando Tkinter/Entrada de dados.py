from  tkinter import *

janela = Tk()
janela.title("Criando uma Entry")
janela.geometry('300x300')

label_nome = Label(janela, text="Nome:")
label_nome.grid(row=0, column=0)
nome = Entry(janela, width = 10, state="disabled")
nome.grid(row=0, column=1)

label_idade = Label(janela, text="Idade:")
label_idade.grid(row=1, column=0)
idade = Entry(janela, width = 10)
idade.grid(row=1, column=1)

label_pais = Label(janela, text="Pais:")
label_pais.grid(row=2, column=0)
pais = Entry(janela, width = 10)
pais.grid(row=2, column=1)

def test():
    n = nome.get()
    i = idade.get()
    p = pais.get()

    label = Label(janela, text=n + " " + i + " " + p)
    label.grid(row=4, column=0)
    print(n, i, p)



b = Button(janela, text="clica", bg="green", command=test)
b.grid(row=3, column=0)




janela.mainloop()
