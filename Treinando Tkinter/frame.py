from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry("300x300")

frame_1 = Frame(janela, width=150, height=200, bg="red")
frame_1.grid(column=0, row=0)

frame_2 = Frame(janela, width=150, height=200, bg="green")
frame_2.grid(column=1, row=0)

frame_3 = Frame(janela, width=300, height=200, bg="blue")
frame_3.grid(column=0, row=1, columnspan=2)

label = Label(frame_1, width=20, text="Olá Mundo!", fg="black")
label.grid(column=0, row=0)

label = Label(frame_1, width=20, text="Olá Mundo!", fg="black")
label.grid(column=0, row=1)

janela.mainloop()
