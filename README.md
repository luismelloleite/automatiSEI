# AutomatiSEI! 

## Automação do SEI! com Selenium e Python

### Exemplos de Scripts

#### 1. Exportação de Processos para CSV
**Script: `automatiSEI-busca_processos.py`**

Gera um arquivo CSV com a lista completa de processos de uma unidade específica no SEI!. 

**Notas Importantes:**
- Antes de rodar, você precisará inserir seu **usuário** e **senha** para acessar o SEI! no início do script.
- Poderá ser adaptado para outros parâmetros de busca.

#### 2. Download em Massa de Processos
**Script: `automatiSEI-download_zip.py`**

Realiza o download em formato ZIP de todos os processos listados em um arquivo CSV (que pode ser gerado via `busca_processos.py`).

**Notas Importantes:**
- Você precisará definir o nome da pasta onde os arquivos serão salvos.

> **Aviso:** Os scripts foram desenvolvidos e testados no SEI! versão 4.0.12. Podem estar desatualizados ou não funcionar corretamente em versões diferentes do SEI!.

### Preparação do Ambiente

#### 1. Criação de Ambiente Virtual (Recomendado)

Um ambiente virtual ajuda a isolar as bibliotecas do projeto, evitando conflitos com outras versões no seu computador.

```bash
# Navegue até a pasta do projeto
cd caminho/para/projeto

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```

#### 2. Instalação das Bibliotecas Necessárias

Com o ambiente virtual ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

#### 3. Configuração dos Scripts

##### automatiSEI-busca_processos.py
- Abra o script e insira seu **usuário** e **senha** do SEI! no início do arquivo.

##### automatiSEI-download_zip.py
- Defina o **nome da pasta** onde os arquivos ZIP serão salvos.

#### 4. Execução dos Scripts

```bash
# Rodar script de busca de processos
python automatiSEI-busca_processos.py

# Rodar script de download em massa
python automatiSEI-download_zip.py
```

### Sobre o Arquivo `requirements.txt`

O arquivo `requirements.txt` contém a lista de bibliotecas Python necessárias para o projeto. Facilita a instalação das dependências de forma consistente.

### Contribuições

Se você tem scripts para automatizar funções do SEI! e deseja compartilhar, entre em contato!

### Contato

**Luis Carlos**  
📧 Email: [luismelloleite@gmail.com](mailto:luismelloleite@gmail.com)

### Licença

MIT
