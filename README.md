# Automacao-em-Python

Pasta com projetos de Automação feitos em python


## App de Cotação
Este projeto é uma aplicação simples em Python que exibe as cotações atuais do Dólar, Euro e Bitcoin em relação ao Real. Ele utiliza a API da AwesomeAPI para buscar as informações e exibe os valores em uma interface gráfica construída com Tkinter.

###Funcionalidades:
##-Faz uma requisição à API para obter as cotações de USD-BRL, EUR-BRL e BTC-BRL.

##-Exibe os valores atualizados em uma janela com interface gráfica.
-Atualização das cotações ao clicar em um botão.

## Envio Automático de Emails 
Este script em Python automatiza o envio de emails utilizando a biblioteca smtplib e email.mime. Ele se conecta a um servidor SMTP, faz login com as credenciais fornecidas e envia um email com conteúdo em HTML.

Funcionalidades:
-Criação e envio de um email automático com um corpo em formato HTML.
-Configuração do servidor SMTP para enviar o email via Gmail.
-Envio do email para o destinatário especificado.
Atenção:
-Certifique-se de configurar as credenciais (email e senha) de maneira segura antes de utilizar o código.

# Organizador de Arquivos em Pastas
Este projeto é um organizador de arquivos simples em Python, que categoriza automaticamente os arquivos em uma pasta selecionada, movendo-os para subpastas de acordo com suas extensões. A interface gráfica é criada com Tkinter.

Funcionalidades:
-Seleciona uma pasta através de uma janela gráfica.
-Organiza os arquivos em subpastas baseadas em tipos pré-definidos (imagens, vídeos, músicas, planilhas, PDFs, etc.).
-Cria automaticamente as subpastas necessárias e move os arquivos para elas.
Extensões Suportadas(por enquanto):
-Imagens e Vídeos: .png, .jpg, .mp4, .avi, .wmv
-Músicas: .mp3, .wav
-Planilhas: .xlsx
-PDFs: .pdf
-Arquivos Compactados: .rar
-Documentos e Textos: .docx, .txt

# Renomeador de arquivos
Este script em Python permite que o usuário selecione uma pasta e renomeia todos os arquivos contidos nela, adicionando o nome do usuário ao início de cada arquivo. Ele usa a biblioteca os para manipulação de arquivos e tkinter.filedialog para permitir a seleção da pasta.

Funcionalidades:
-Solicita o nome do usuário para personalizar os nomes dos arquivos.
-Permite a seleção de uma pasta através de uma janela gráfica.
-Renomeia todos os arquivos da pasta, adicionando "Arquivos do(a) [nome do usuário]" ao início de cada nome de arquivo.
