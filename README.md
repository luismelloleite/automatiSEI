# automatiSEI!
## Automação do SEI! com Selenium e Python

### Exemplos de Scripts

- **Exportação de Processos para CSV (automatiSEI-busca_processos.py)**: Gera um arquivo CSV com a lista completa de processos de uma unidade específica no SEI! (poderá ser adaptado para outros parâmetros). **Antes de rodar, você precisará inserir seu usuário e senha para acessar o SEI! no início do script**.
- **Download em Massa de Processos (automatiSEI-download_zip.py)**: Realiza o download em formato ZIP de todos os processos listados em um arquivo CSV (que pode ser gerado via busca_processos.py). **Você também precisará definir o nome da pasta onde os arquivos serão salvos**.

**Observação:** Os scripts abaixo foram desenvolvidos e testados no SEI! versão 4.0.12. Eles podem estar desatualizados ou não funcionar corretamente em versões superiores ou inferiores do SEI!.

---

### Como Preparar o Ambiente para Rodar os Scripts

Para rodar os scripts deste projeto, você precisará instalar algumas bibliotecas Python. Abaixo, explico de forma simples como configurar o ambiente no seu computador.

#### 1. **Criando um Ambiente Virtual (Recomendado)**

Um **ambiente virtual** ajuda a isolar as bibliotecas que você vai usar no seu projeto, evitando conflitos com outras versões de bibliotecas no seu computador.

- Abra o terminal (ou Prompt de Comando no Windows) e navegue até a pasta onde você baixou o projeto.
- Crie o ambiente virtual com um comando simples. Isso criará uma pasta para armazenar as dependências do seu projeto.
- Ative o ambiente virtual para começar a usar.

#### 2. **Instalando as Bibliotecas Necessárias**

Após ativar o ambiente virtual, você precisa instalar as bibliotecas que o projeto usa. As bibliotecas necessárias estão listadas em um arquivo chamado `requirements.txt`.

- Com o ambiente ativado, instale as bibliotecas necessárias com um comando simples. Isso vai garantir que o script funcione corretamente.

#### 3. **Configurando os Scripts**

Antes de rodar os scripts, você precisa fazer algumas configurações:

- **No script `automatiSEI-busca_processos.py`**: Você precisará abrir o script e inserir seu **usuário** e **senha** do SEI! no início do arquivo. Isso permite que o script acesse o SEI! automaticamente.
  
- **No script `automatiSEI-download_zip.py`**: Abra o script e defina o **nome da pasta** onde os arquivos ZIP serão salvos. Escolha uma pasta existente no seu computador para armazenar os downloads.

#### 4. **Rodando os Scripts**

Depois de configurar tudo, você pode rodar os scripts. Para rodar o script de busca de processos, basta executar o comando correspondente no terminal.

O script de download em massa funciona da mesma forma. Certifique-se de que todos os parâmetros estão configurados corretamente antes de executar os scripts.

---

### O Que é o Arquivo `requirements.txt`?

O arquivo `requirements.txt` contém uma lista das bibliotecas Python necessárias para o seu projeto. Ele facilita a instalação dessas bibliotecas de uma vez, garantindo que o script funcione como esperado.

---

### Contribua com seus Scripts

Se você tem algum script que automatiza funções do SEI! e deseja compartilhar, entre em contato!

---

### Contato para dúvida, contribuição e consultoria em geral.

Luis Carlos  
[luismelloleite@gmail.com](mailto:luismelloleite@gmail.com)
