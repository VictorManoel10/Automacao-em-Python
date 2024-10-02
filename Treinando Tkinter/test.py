import os
import zipfile
import threading
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory
from tkinter import *

# Função para centralizar a janela no meio da tela
def centralizar_janela(janela):
    janela.update_idletasks()  # Atualiza o layout da janela
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para renomear um arquivo caso ele já exista no destino
def renomear_arquivo(destino_arquivo):
    base, extensao = os.path.splitext(destino_arquivo)
    contador = 1
    while os.path.exists(destino_arquivo):
        destino_arquivo = f"{base}_{contador}{extensao}"
        contador += 1
    return destino_arquivo

# Função que compacta pastas e exibe o progresso
def zipar_pastas(caminho, progresso_bar):
    pasta_nome = os.path.basename(caminho)
    zip_destino = os.path.join(caminho, f"{pasta_nome}_organizado.zip")

    if os.path.exists(zip_destino):
        os.remove(zip_destino)

    pastas = [os.path.join(caminho, d) for d in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, d))]

    total_itens = sum([len(files) for r, d, files in os.walk(caminho)])
    progresso_bar["maximum"] = total_itens

    progresso = 0
    step = 50 if total_itens > 500 else 20 if total_itens > 100 else 5

    with zipfile.ZipFile(zip_destino, 'w') as arq_zip:
        for pasta in pastas:
            for root, dirs, files in os.walk(pasta):
                for arquivo in files:
                    caminho_arquivo = os.path.join(root, arquivo)
                    arq_zip.write(caminho_arquivo, os.path.relpath(caminho_arquivo, caminho))
                    progresso += 1
                    if progresso % step == 0:
                        progresso_bar["value"] = progresso
                        progresso_bar.update_idletasks()

    progresso_bar["value"] = total_itens
    progresso_bar.update_idletasks()
    messagebox.showinfo("FolderFix", f"As pastas foram compactadas em {zip_destino} com sucesso!")

# Função para executar a compactação das pastas em uma nova thread
def zipar_pastas_thread(caminho, progresso_bar):
    progresso_bar.grid(column=0, row=4, padx=10, pady=10)
    janela.update()  # Força o redimensionamento da janela
    centralizar_janela(janela)  # Centraliza a janela após a barra de progresso aparecer
    thread = threading.Thread(target=zipar_pastas, args=(caminho, progresso_bar))
    thread.start()

# Função principal que organiza os arquivos nas pastas corretas
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
        "Musicas": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".aiff", ".aif", ".alac", ".opus", ".amr", ".mid", ".midi"],
        "planilhas": [".xlsx", ".xls", ".csv"],
        "Pdfs": [".pdf"],
        "Winrar": [".rar", ".zip", ".7z", ".tar", ".gz"],
        "Arquivos de Texto": [".docx", ".txt", ".doc", ".rtf"],
        "Instaladores e Programas": [".exe", ".msi", ".bat", ".app", ".apk", ".dmg", ".pkg", ".jar", ".run", ".sh"],
        "Torrents": [".torrent"],
        "Photoshop": [".psd"],
        "Arquivos de Código": [".py", ".js", ".html", ".css", ".json", ".xml", ".java", ".c", ".cpp", ".h",
        ".php", ".rb", ".swift", ".go", ".ts", ".r", ".sql", ".sh"],
        "Apresentações": [".ppt", ".pptx", ".key", ".odp"],
        "Fontes": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
        "Imagens 3D": [".obj", ".stl", ".fbx", ".gltf", ".3ds", ".dae"],
        "Projetos CAD": [".dwg", ".dxf", ".step", ".stp", ".iges", ".igs"]
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

    centralizar_janela(janela)

    resposta = messagebox.askyesno("FolderFix", "Você quer compactar as pastas criadas?")
    if resposta:
        progresso_bar.grid_forget()
        zipar_pastas_thread(caminho, progresso_bar)

# Configurações da janela principal
janela = Tk()
janela.title("FolderFix 1.0.6")

name_app = Label(janela, text="FolderFix", font=("Impact", 20), fg="black")
name_app.grid(column=0, row=0)

txt_main = Label(janela, text="Vamos organizar seus arquivos em pastas!", font=("Arial", 13))
txt_main.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Escolha uma pasta...", font=("Arial", 12, "bold"), bg="#EAC40B", fg="white", relief="flat", bd='3', command=orgArq)
botao.grid(column=0, row=2, padx=10, pady=10)

txt_end = Label(janela, text="Seus arquivos agora estão organizados!", font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

progresso_bar = ttk.Progressbar(janela, orient="horizontal", length=250, mode="determinate")
progresso_bar.grid_forget()

# Centraliza a janela no início
janela.update_idletasks()
centralizar_janela(janela)

janela.mainloop()
