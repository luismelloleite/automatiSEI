# AutomatiSEI! 🤖📄

## Descrição do Projeto

AutomatiSEI! é uma solução de automação para o Sistema Eletrônico de Informações (SEI!) utilizando Selenium e Python. O projeto oferece exemplos de scripts para automatizar tarefas repetitivas no sistema SEI!, facilitando a extração e manipulação de processos administrativos.

### 🚀 Scripts 

#### 1. Exportação de Processos para CSV
**Script:** `automatiSEI-busca_processos.py`

- Gera arquivo CSV com lista completa de processos de uma unidade específica
- Personalizável para diversos parâmetros de busca
- Simplifica a extração de dados do SEI!

#### 2. Download em Massa de Processos
**Script:** `automatiSEI-download_zip.py`

- Baixa processos em formato ZIP a partir de lista CSV
- Automatiza o download de múltiplos processos
- Integração direta com script de busca

> **⚠️ Aviso:** Desenvolvido e testado no SEI! versão 4.0.12. Compatibilidade com outras versões pode variar.

## 🛠 Configuração do Ambiente

### Pré-requisitos

- Python 3.7+
- Pip
- Navegador Chrome (para Selenium)

### Configuração Passo a Passo

#### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/automatisei.git
cd automatisei
```

#### 2. Criar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

#### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### 4. Configurar Credenciais

##### `automatiSEI-busca_processos.py`
- Abra o script
- Insira seu **usuário** e **senha** do SEI! 

##### `automatiSEI-download_zip.py`
- Defina o **diretório de destino** para downloads

### 🚀 Execução dos Scripts

```bash
# Buscar processos
python automatiSEI-busca_processos.py

# Download em massa
python automatiSEI-download_zip.py
```

## 📦 Dependências

- Selenium
- Pandas
- ChromeDriver
- Outras dependências listadas em `requirements.txt`

## 🤝 Contribuições

Contribuições são bem-vindas! 

Formas de contribuir:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests
- Compartilhar scripts de automação do SEI!

## 📞 Contato

**Luis Carlos**  
📧 [luismelloleite@gmail.com](mailto:luismelloleite@gmail.com)

## 📄 Licença

[MIT License](https://opensource.org/licenses/MIT)

```
MIT License

Copyright (c) 2024 Luis Carlos Leite de Mello

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
