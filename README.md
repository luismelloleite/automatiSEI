# AutomatiSEI

## Descrição
Projeto demonstrativo em Python que ilustra automação do Sistema Eletrônico de Informações (SEI) usando Selenium. Fornece exemplos de automação de tarefas comuns como login, busca, exportação e download de processos. Destina-se a fins educativos.

## Escopo e objetivo
Este repositório contém exemplos para automatizar:
1. Autenticação no SEI
2. Busca e filtragem de processos
3. Exportação de resultados para CSV
4. Download em massa de processos em formato ZIP

## Principais scripts
1. `automatiSEI-busca_processos.py` — busca processos e gera CSV com os resultados
2. `automatiSEI-download_zip.py` — realiza download em massa a partir de um CSV

## Compatibilidade
Desenvolvido e testado com SEI versão 4.0.12. Pode não ser compatível com outras versões.

## Requisitos
1. Python 3.7 ou superior
2. pip
3. Navegador Chrome e ChromeDriver compatível
4. Dependências listadas em `requirements.txt`

## Instalação rápida
1. Clone o repositório
   git clone https://github.com/luismelloleite/automatiSEI.git
   cd automatiSEI
2. Crie e ative um ambiente virtual
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate   # macOS ou Linux
3. Instale as dependências
   pip install -r requirements.txt

## Configuração
1. Configure credenciais de acesso ao SEI nos scripts ou via variáveis de ambiente ou arquivos de configuração.
2. Ajuste parâmetros de busca conforme a unidade e filtros desejados.
3. Defina o diretório de destino para os downloads no script de download.

## Execução
1. Buscar processos
   python automatiSEI-busca_processos.py
2. Efetuar download em massa
   python automatiSEI-download_zip.py

## Contribuições
Contribuições são bem-vindas. Abra issues para bugs ou sugestões e envie pull requests com melhorias ou novos exemplos.

## Contato
Luis Carlos  
luismelloleite@gmail.com

## Licença
MIT License  
https://opensource.org/licenses/MIT
