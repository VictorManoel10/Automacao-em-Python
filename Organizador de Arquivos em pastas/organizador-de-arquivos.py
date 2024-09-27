import os  # Módulo para manipulação de arquivos e diretórios
import zipfile  # Módulo para trabalhar com arquivos ZIP
import threading  # Módulo para trabalhar com threads (execução paralela)
from tkinter import messagebox, ttk  # Importa componentes de interface gráfica do Tkinter
from tkinter.filedialog import askdirectory  # Função para abrir o diálogo de seleção de pasta
from tkinter import *  # Importa todo o Tkinter

# Função para centralizar a janela no meio da tela
def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()  # Obtém a largura da tela
    tela_altura = janela.winfo_screenheight()  # Obtém a altura da tela
    x = (tela_largura - largura) // 2  # Calcula a posição X para centralizar
    y = (tela_altura - altura) // 2  # Calcula a posição Y para centralizar
    janela.geometry(f"{largura}x{altura}+{x}+{y}")  # Define a geometria da janela

# Função para renomear um arquivo caso ele já exista no destino
def renomear_arquivo(destino_arquivo):
    base, extensao = os.path.splitext(destino_arquivo)  # Divide o nome do arquivo e sua extensão
    contador = 1
    # Enquanto o arquivo existir, ele será renomeado
    while os.path.exists(destino_arquivo):
        destino_arquivo = f"{base}_{contador}{extensao}"  # Adiciona um número ao nome do arquivo
        contador += 1
    return destino_arquivo  # Retorna o nome do arquivo renomeado

# Função que compacta pastas e exibe o progresso
def zipar_pastas(caminho, progresso_bar):
    pasta_nome = os.path.basename(caminho)  # Obtém o nome da pasta base
    zip_destino = os.path.join(caminho, f"{pasta_nome}_organizado.zip")  # Define o caminho do arquivo ZIP

    # Se o arquivo ZIP já existir, remove-o para evitar duplicação
    if os.path.exists(zip_destino):
        os.remove(zip_destino)

    # Obter todas as pastas criadas no caminho
    pastas = [os.path.join(caminho, d) for d in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, d))]

    # Contar o número total de arquivos que serão compactados
    total_itens = sum([len(files) for r, d, files in os.walk(caminho)])
    progresso_bar["maximum"] = total_itens  # Define o valor máximo da barra de progresso

    progresso = 0  # Inicializa o progresso
    # Criação do arquivo ZIP
    with zipfile.ZipFile(zip_destino, 'w') as arq_zip:
        # Itera pelas pastas e arquivos
        for pasta in pastas:
            for root, dirs, files in os.walk(pasta):
                for arquivo in files:
                    caminho_arquivo = os.path.join(root, arquivo)  # Caminho completo do arquivo
                    arq_zip.write(caminho_arquivo, os.path.relpath(caminho_arquivo, caminho))  # Adiciona ao ZIP
                    
                    # Atualiza a barra de progresso a cada 10 arquivos
                    progresso += 1
                    if progresso % 10 == 0:
                        progresso_bar["value"] = progresso  # Atualiza o valor da barra de progresso
                        progresso_bar.update_idletasks()  # Atualiza a interface

    # Atualiza a barra de progresso para o valor máximo
    progresso_bar["value"] = total_itens
    progresso_bar.update_idletasks()

    # Exibe uma mensagem de sucesso
    messagebox.showinfo("FolderFix", f"As pastas foram compactadas em {zip_destino} com sucesso!")

# Função para executar a compactação das pastas em uma nova thread
def zipar_pastas_thread(caminho, progresso_bar):
    progresso_bar.grid(column=0, row=4, padx=10, pady=10)  # Exibe a barra de progresso
    thread = threading.Thread(target=zipar_pastas, args=(caminho, progresso_bar))  # Cria uma nova thread
    thread.start()  # Inicia a thread

# Função principal que organiza os arquivos nas pastas corretas
def orgArq():
    caminho = askdirectory(title="Selecione uma pasta")  # Abre o diálogo para o usuário escolher uma pasta

    # Verifica se o usuário selecionou uma pasta
    if not caminho:
        txt_end.config(text="Você não selecionou nenhuma pasta!", bg="#CF2323")  # Exibe uma mensagem de erro
        txt_end.grid(column=0, row=3, padx=10, pady=10)  # Posiciona o texto de erro na interface
        return

    lista_arquivos = os.listdir(caminho)  # Lista todos os arquivos da pasta

    # Dicionário de tipos de arquivos e suas respectivas extensões
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
        ".php", ".rb", ".swift", ".go", ".ts", ".r", ".sql", ".sh"],
        "Apresentações": [".ppt", ".pptx", ".key", ".odp"],
        "Fontes": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
        "Imagens 3D": [".obj", ".stl", ".fbx", ".gltf", ".3ds", ".dae"],
        "Projetos CAD": [".dwg", ".dxf", ".step", ".stp", ".iges", ".igs"]
    }

    # Para cada arquivo na lista
    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)  # Obtém o caminho completo do arquivo
        nome, extensao = os.path.splitext(arquivo)  # Separa o nome e a extensão do arquivo
        extensao = extensao.lower()  # Converte a extensão para minúscula

        pasta_destino = None
        # Verifica qual é a pasta correta para o arquivo com base na sua extensão
        for pasta, extensoes in locais.items():
            if extensao in extensoes:
                pasta_destino = pasta
                break

        # Se encontrou uma pasta de destino para o arquivo
        if pasta_destino:
            destino_pasta = os.path.join(caminho, pasta_destino)  # Define o caminho da pasta de destino
            if not os.path.exists(destino_pasta):
                os.mkdir(destino_pasta)  # Cria a pasta se ela não existir
            destino_arquivo = os.path.join(destino_pasta, arquivo)  # Define o caminho do arquivo na pasta de destino

            # Renomeia o arquivo se ele já existir no destino
            if os.path.exists(destino_arquivo):
                destino_arquivo = renomear_arquivo(destino_arquivo)

            os.rename(caminho_arquivo, destino_arquivo)  # Move o arquivo para a pasta de destino

    # Exibe uma mensagem de sucesso informando que a pasta foi organizada
    pasta_nome = os.path.basename(caminho)
    txt_end.config(text=f"Sua pasta {pasta_nome} agora está organizada!", font=("Arial", 11), bg="#23CF5C")
    txt_end.grid(column=0, row=3, padx=10, pady=10)

    # Pergunta ao usuário se deseja compactar as pastas organizadas
    resposta = messagebox.askyesno("FolderFix", "Você quer compactar as pastas criadas?")
    if resposta:
        progresso_bar.grid_forget()  # Oculta a barra de progresso até o usuário decidir zipar
        zipar_pastas_thread(caminho, progresso_bar)  # Inicia o processo de zipar

# Configurações da janela principal
janela = Tk()
janela.title("FolderFix 1.0.6")

largura_janela = 350
altura_janela = 225
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

# Barra de progresso
progresso_bar = ttk.Progressbar(janela, orient="horizontal", length=250, mode="determinate")
progresso_bar.grid_forget()  # Inicialmente oculta a barra de progresso

janela.mainloop()