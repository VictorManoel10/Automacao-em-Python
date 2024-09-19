import os
from tkinter.filedialog import askdirectory
from tkinter import *

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def renomear_arquivo(destino_arquivo):
    base, extensao = os.path.splitext(destino_arquivo)
    contador = 1
    while os.path.exists(destino_arquivo):
        destino_arquivo = f"{base}_{contador}{extensao}"
        contador += 1
    return destino_arquivo

def orgArq():
    caminho = askdirectory(title="Selecione uma pasta")

    if not caminho:
        txt_end.config(text="Você não selecionou nenhuma pasta!", bg="#CF2323")
        txt_end.grid(column=0, row=3, padx=10, pady=10)
        return

    lista_arquivos = os.listdir(caminho)

    locais = {
        "Imagens e Videos": [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp", ".svg",
        ".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".mpg", ".mpeg", ".3gp", ".ico", ".avif"],
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
        caminho_arquivo = os.path.join(caminho, arquivo)
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        pasta_destino = None
        for pasta, extensoes in locais.items():
            if extensao in extensoes:
                pasta_destino = pasta
                break

        if pasta_destino:
            destino_pasta = os.path.join(caminho, pasta_destino)
            if not os.path.exists(destino_pasta):
                os.mkdir(destino_pasta)
            destino_arquivo = os.path.join(destino_pasta, arquivo)

            if os.path.exists(destino_arquivo):
                destino_arquivo = renomear_arquivo(destino_arquivo)

            os.rename(caminho_arquivo, destino_arquivo)

    pasta_nome = os.path.basename(caminho)
    txt_end.config(text=f"Sua pasta {pasta_nome} agora está organizada!", font=("Arial", 11), bg="#23CF5C")
    txt_end.grid(column=0, row=3, padx=10, pady=10)

janela = Tk()
janela.title("FolderFix 1.0.4")
janela.iconbitmap(r"C:\Users\lordz\Documents\Projetos de automação python\Automacao-em-Python\Orgazinador de Arquivos em pastas\folder.ico")

largura_janela = 350
altura_janela = 200
centralizar_janela(janela, largura_janela, altura_janela)
janela.resizable(False, False)

name_app = Label(janela, text="FolderFix", font=("Impact", 20), fg="black")
name_app.grid(column=0, row=0)

txt_main = Label(janela, text="Vamos organizar seus arquivos em pastas!", font=("Arial", 13))
txt_main.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Escolha uma pasta...", font=("Arial", 12, "bold"), bg="#EAC40B", fg="white" ,relief="flat", bd='3', command=orgArq)
botao.grid(column=0, row=2, padx=10, pady=10)

txt_end = Label(janela, text="Seus arquivos agora estão organizados!", font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

janela.mainloop()
