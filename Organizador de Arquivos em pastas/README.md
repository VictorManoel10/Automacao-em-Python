
# FolderFix 1.0.6

**FolderFix** é uma ferramenta simples para organizar seus arquivos em pastas específicas com base em suas extensões e opcionalmente compactar as pastas criadas em um arquivo `.zip`. O programa foi desenvolvido com a interface gráfica Tkinter e utiliza a biblioteca `zipfile` para compactação.

## Funcionalidades

### 1. Organização de Arquivos
- O **FolderFix** permite ao usuário selecionar uma pasta. A partir daí, ele organiza todos os arquivos encontrados em subpastas com base em suas extensões.
- As categorias de organização são definidas em um dicionário chamado `locais`, que mapeia extensões de arquivos para tipos de arquivos. Por exemplo:
  - Imagens e Vídeos: `.png`, `.jpg`, `.mp4`, etc.
  - Músicas: `.mp3`, `.wav`, etc.
  - Documentos: `.pdf`, `.docx`, etc.
  - Programas e Instaladores: `.exe`, `.msi`, etc.
  - E várias outras categorias de arquivos, como **Arquivos de Código**, **Apresentações**, **Imagens 3D**, entre outros.
  
- Caso o arquivo já exista na pasta de destino, o programa renomeia o arquivo automaticamente, evitando a sobrescrita.

### 2. Compactação de Pastas
- Após organizar os arquivos, o programa pergunta se o usuário deseja compactar as pastas organizadas em um arquivo `.zip`.
- Se o usuário optar por compactar, será criada uma barra de progresso indicando o andamento da compactação.
- O arquivo `.zip` é salvo com o nome da pasta original seguido de `_organizado.zip`. Se o arquivo já existir, ele será substituído.

### 3. Interface Gráfica
- A interface do programa é simples e intuitiva, com botões e mensagens que guiam o usuário através do processo de organização e compactação.
- O texto final indica que os arquivos foram organizados com sucesso, e, caso a opção de compactação tenha sido escolhida, o usuário é informado sobre a criação do arquivo `.zip`.

## Como Usar
1. Execute o programa **FolderFix**.
2. Clique no botão **Escolha uma pasta...** para selecionar a pasta que deseja organizar.
3. O programa irá organizar seus arquivos em pastas categorizadas com base em suas extensões.
4. Após a organização, você será perguntado se deseja compactar as pastas organizadas.
   - Caso opte por **Sim**, uma barra de progresso aparecerá e o programa criará um arquivo `.zip` contendo as pastas organizadas.
   - Caso opte por **Não**, o programa apenas mostrará uma mensagem de conclusão.

## Contribuições
Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
