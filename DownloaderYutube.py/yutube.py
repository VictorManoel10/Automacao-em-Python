import yt_dlp  # Importa a biblioteca yt_dlp para download de vídeos
import os  # Para manipulação de diretórios
from pathlib import Path  # Para facilitar o manuseio de caminhos
from tkinter import *


def obter_dir_downloads():
    return str(Path.home() / 'Downloads')


# Define o diretório de Downloads
download_dir = obter_dir_downloads()

# Opções para baixar o melhor áudio disponível (sem conversão)
ydl_opts = {
    'format': 'bestaudio/best',  # Seleciona o melhor formato de áudio disponível
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Define o caminho do arquivo baixado
    'noplaylist': True  # Baixa apenas um vídeo se for uma playlist
}


def baixar():
    try:
        link = linkk.get()  # Obtém o link do vídeo fornecido pelo usuário

        # Usa o contexto 'with' para garantir que recursos sejam liberados após o uso
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extrai as informações do vídeo sem fazer o download ainda (download=False)
            info_dict = ydl.extract_info(link, download=False)
            
            # Obtém o título do vídeo ou define 'Áudio Desconhecido' se o título não for encontrado
            audio_title = info_dict.get('title', 'Áudio Desconhecido')
            
            # Exibe o nome do áudio que será baixado
            print(f'Baixando {audio_title} para {download_dir}')
            
            # Faz o download do áudio usando o link fornecido
            ydl.download([link])
        
        # Mensagem de confirmação quando o download for concluído
        print("Download Concluído!")
        
        # Mensagem de sucesso
        txt_end.config(text=f"A música {audio_title} foi baixada com sucesso!", font=("Arial", 11), bg="#23CF5C")
        txt_end.grid(column=1, row=3, padx=10, pady=10)

    except Exception as e:
        # Captura qualquer erro que possa ocorrer e exibe a mensagem de erro
        print(f"Ocorreu um erro: {str(e)}")
        # Exibe mensagem de erro
        txt_end.config(text=f"Ocorreu um erro: {str(e)}", font=("Arial", 11), bg="red", fg="white")
        txt_end.grid(column=1, row=3, padx=10, pady=10)


# Interface gráfica
janela = Tk()
janela.title("TubeSaver 1.0")
janela.geometry('450x200')

# Permite que as colunas e linhas se expandam ao redimensionar a janela
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(1, weight=1)

# Labels e campos de entrada
label_link = Label(janela, text="Link do video: ")
label_link.grid(column=1, row=0)

linkk = Entry(janela, width=30)
linkk.grid(column=1, row=1)

# Botão de download
butao = Button(janela, text='baixar', command=baixar)
butao.grid(column=1, row=2, padx=10, pady=10)

# Mensagem final
txt_end = Label(janela, font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

janela.mainloop()
