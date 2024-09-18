import os
from tkinter.filedialog import askdirectory
from tkinter import *


def centralizar_janela(janela, largura, altura):
    # Obtém as dimensões da tela
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    
    # Calcula as coordenadas x e y para a centralização
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 2

    # Define a geometria da janela
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def orgArq():
    caminho = askdirectory(title="Selecione uma pasta")

    if not caminho:  # Caso o usuário cancele a seleção da pasta
        txt_end.config(text="Você não selecionou nenhuma pasta!", bg="#CF2323")  # Atualiza a mensagem e a cor de fundo
        txt_end.grid(column=0, row=3, padx=10, pady=10)
        return

    lista_arquivos = os.listdir(caminho)

    locais = {
        "Imagens e Videos": [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp", ".svg",
        ".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".mpg", ".mpeg", ".3gp", "ico", ".avif"],
        "Musicas": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".aiff", ".aif",
        ".alac", ".opus", ".amr", ".mid", ".midi"],
        "planilhas": [".xlsx", ".xls", ".csv"],
        "Pdfs": [".pdf"],
        "Winrar": [".rar", ".zip", ".7z", ".tar", ".gz"],
        "Arquivos de Texto": [".docx", ".txt", ".doc", ".rtf"],
        "Instaladores e Programas": [".exe", ".msi", ".bat", ".app", ".apk", ".dmg", ".pkg", ".jar", ".run", ".sh"],
        "Torrents": [".torrent"],
        "Photoshop": [".psd"],
        "Arquivos de Código": [".py", ".js", ".html", ".css", ".json", ".xml", ".java", ".c", ".cpp", ".h",
        ".php", ".rb", ".swift", ".go", ".ts", ".r", ".sql", ".sh"]
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        extensao = extensao.lower()
        
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    txt_end.config(text="Seus arquivos agora estão organizados!", bg="#23CF5C")  # Atualiza a mensagem e a cor de fundo
    txt_end.grid(column=0, row=3, padx=10, pady=10)



janela = Tk()
janela.title("FolderFix 1.0.3")
janela.iconbitmap(r"C:\Users\lordz\Documents\Projetos de automação python\Automacao-em-Python\Orgazinador de Arquivos em pastas\folder.ico")

# Define as dimensões da janela
largura_janela = 350
altura_janela = 165

# Centraliza a janela
centralizar_janela(janela, largura_janela, altura_janela)

# Impede o redimensionamento da janela
janela.resizable(False, False)

name_app = Label(janela, text="FolderFix", font=("Impact", 20), fg="black")
name_app.grid(column=0, row=0)

txt_main = Label(janela, text="Vamos organizar seus arquivos em pastas!", font=("Arial", 13))
txt_main.grid(column=0, row=1, padx=10)

botao = Button(janela, text="Escolha uma pasta...", font=("Arial", 12, "bold"), bg="#EAC40B", fg="white" ,relief="flat", bd='3', command=orgArq)
botao.grid(column=0, row=2, padx=10, pady=10)

txt_end = Label(janela, text="Seus arquivos agora estão organizados!", font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

 
janela.mainloop()