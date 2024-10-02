import yt_dlp  # Importa a biblioteca yt_dlp para download de vídeos
import os  # Para manipulação de diretórios
from pathlib import Path  # Para facilitar o manuseio de caminhos


def obter_dir_downloads():
    return str(Path.home() / 'Downloads')


# Solicita ao usuário o link do vídeo
link = input("Digite o Link do vídeo que você deseja baixar: ")

# Define o diretório de Downloads
download_dir = obter_dir_downloads()

# Define as opções de download (neste caso, 'best' seleciona o melhor formato disponível)
ydl_opts = {'format': 'best', 'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s')}

try:
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
