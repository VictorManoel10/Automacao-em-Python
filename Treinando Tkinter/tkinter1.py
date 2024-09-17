from tkinter import *

janela = Tk() #Criar um janela
janela.title("Olá Mundo!") #Titulo da janela
janela.geometry("200x200") #Configurar largura e comprimento da janela

label = Label(janela, text="Primeiro label", font=("Arial", 20, "bold"), bg="red", fg="white") #Add um Label(rotulo/legenda) na janela
label.grid(column=0, row=0) #Determina a posição do label na janela

janela.mainloop() #Loop para manter a janela aberta