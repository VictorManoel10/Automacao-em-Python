from tkinter import *

janela = Tk()
janela.title("Personalização de Botão")

# Definir uma fonte personalizada
fonte_personalizada = ("Helvetica", 14, "bold")

# Criar um botão personalizado
botao = Button(janela, 
               text="Clique Aqui", 
               font=fonte_personalizada,  # Fonte do botão
               bg="lightblue",  # Cor de fundo
               fg="white",  # Cor do texto
               width=15,  # Largura do botão
               height=2,  # Altura do botão
               bd=5,  # Espessura da borda
               relief="raised",  # Tipo de borda
               padx=10,  # Preenchimento horizontal
               pady=10)  # Preenchimento vertical

botao.pack(pady=20)  # Exibir o botão com um espaçamento vertical

janela.mainloop()
