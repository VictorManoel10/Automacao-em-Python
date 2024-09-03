import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
os.chdir(caminho)

lista_de_arquivos = os.listdir(caminho)

for arquivo in lista_de_arquivos:
    if os.path.isfile(arquivo):
        novo_nome = f'Arquivos do Victor - {arquivo}'
        os.rename(arquivo, novo_nome)
