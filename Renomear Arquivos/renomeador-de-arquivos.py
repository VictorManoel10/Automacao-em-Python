import os
from tkinter.filedialog import askdirectory

nome_User = str(input("Qual o seu nome: "))

caminho = askdirectory(title="Selecione uma pasta")
os.chdir(caminho)

lista_de_arquivos = os.listdir(caminho)

for arquivo in lista_de_arquivos:
    if os.path.isfile(arquivo):
        novo_nome = f'Arquivos do(a) {nome_User} - {arquivo}'
        os.rename(arquivo, novo_nome)
