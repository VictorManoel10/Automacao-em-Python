#1. Gerador de Senhas Seguras
#Crie um programa que gere senhas aleatórias seguras. O usuário poderá especificar o tamanho da senha e se deseja incluir números, letras maiúsculas, minúsculas e caracteres especiais. Garanta que a senha tenha pelo menos um caractere de cada tipo selecionado.
#Desafios:
#Manipulação de strings
#Uso da biblioteca random ou secrets

from random import *
import string

def gerar_senha():

    senha = list()

    for c in range(2):
        senha.append(str(randint(0, 9)))

    for c in range(4):
        senha.append(choice(string.ascii_letters))

    for c in range(2):
        senha.append(choice(string.punctuation))

    shuffle(senha)

    return ''.join(senha)



print("+++Gerador de senha+++")
senha_gerada = gerar_senha()
print(f"Senha gerada: {senha_gerada}")