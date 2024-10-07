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
        
    except Exception as e:
        # Captura qualquer erro que possa ocorrer e exibe a mensagem de erro
        print(f"Ocorreu um erro: {str(e)}")

    # Exibe uma mensagem de sucesso informando que a pasta foi organizada
    txt_end.config(text=f"O vídeo foi baixado com sucesso!", font=("Arial", 11), bg="#23CF5C")
    txt_end.grid(column=0, row=3, padx=10, pady=10)


janela = Tk()
janela.title("App YouTube")
janela.geometry('200x100')

label_link = Label(janela, text="Link do video: ")
label_link.grid(column=1, row=0)

linkk = Entry(janela, width=30)
linkk.grid(column=1, row=1)


butão = Button(janela, text='baixar', command=baixar)
butão.grid(column=1, row=2)

txt_end = Label(janela, text="Video baixado", font=("Arial", 13, "bold"), bg="#23CF5C", fg="white")
txt_end.grid_forget()

janela.mainloop()
