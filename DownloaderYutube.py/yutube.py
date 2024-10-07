import yt_dlp  # Importa a biblioteca yt_dlp para download de vídeos
import os  # Para manipulação de diretórios
from pathlib import Path  # Para facilitar o manuseio de caminhos
from tkinter import * 


def obter_dir_downloads():
    return str(Path.home() / 'Downloads')


# Solicita ao usuário o link do vídeo
#link = input("Digite o Link do vídeo que você deseja baixar: ")

# Define o diretório de Downloads
download_dir = obter_dir_downloads()

# Define as opções de download (neste caso, 'best' seleciona o melhor formato disponível)
ydl_opts = {'format': 'best', 'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s')}


def baixar():
    try:
        link = linkk.get()

        # Usa o contexto 'with' para garantir que recursos sejam liberados após o uso
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extrai as informações do vídeo sem fazer o download ainda (download=False)
            info_dict = ydl.extract_info(link, download=False)
            
            # Obtém o título do vídeo ou define 'Vídeo Desconhecido' se o título não for encontrado
            video_title = info_dict.get('title', 'Vídeo Desconhecido')
            
            # Exibe o nome do vídeo que será baixado
            print(f'Baixando {video_title} para {download_dir}')
            
            # Faz o download do vídeo usando o link fornecido
            ydl.download([link])
        
        # Mensagem de confirmação quando o download for concluído
        print("Download Concluído!")
        
        # Mensagem de sucesso
        txt_end.config(text=f"O vídeo {video_title} foi baixado com sucesso!", font=("Arial", 11), bg="#23CF5C")
        txt_end.grid(column=1, row=3, padx=10, pady=10)

    except Exception as e:
        # Captura qualquer erro que possa ocorrer e exibe a mensagem de erro
        print(f"Ocorreu um erro: {str(e)}")
        #exibe mensagem de erro
        txt_end.config(text=f"Ocorreu um erro: {str(e)}", font=("Arial", 11), bg="red", fg="white")
        txt_end.grid(column=1, row=3, padx=10, pady=10)
    


janela = Tk()
janela.title("TubeSaver 1.0")
janela.geometry('450x200')

# Permite que as colunas e linhas se expandam ao redimensionar a janela
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(1, weight=1)

label_link = Label(janela, text="Link do video: ")
label_link.grid(column=1, row=0)

linkk = Entry(janela, width=30)
linkk.grid(column=1, row=1)


butão = Button(janela, text='baixar', command=baixar)
butão.grid(column=1, row=2, padx=10, pady=10)

txt_end = Label(janela, font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

janela.mainloop()
