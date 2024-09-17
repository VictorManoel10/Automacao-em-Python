import os
from tkinter.filedialog import askdirectory
from tkinter import *

def orgArq():
    caminho = askdirectory(title="Selecione uma pasta")

    if not caminho:  # Caso o usuário cancele a seleção da pasta
        return

    lista_arquivos = os.listdir(caminho)

    locais = {
        "Imagens e Videos": [".png", ".jpg", ".mp4", ".avi", ".wmv", ".gif", ".jpeg", ".ico"],
        "Musicas": [".mp3", ".wav"],
        "planilhas": [".xlsx"],
        "Pdfs": [".pdf"],
        "Winrar": [".rar", ".zip", ".7z"],
        "Arquivos de Texto": [".docx", ".txt"],
        "Instaladores": [".exe", ".msi", ".dmg"],
        "Torrents": [".torrent"]
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        extensao = extensao.lower()
        
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    txt_end.grid(column=0, row=2, padx=10, pady=10)



janela = Tk()
janela.title("Organizador de arquivos")

txt_main = Label(janela, text="Vamos organizar seus arquivos em pastas!")
txt_main.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Procurar pasta", command=orgArq)
botao.grid(column=0, row=1, padx=10, pady=10)

txt_end = Label(janela, text="Seus arquivos agora estão organizados!")
txt_end.grid_forget()

 
janela.mainloop()