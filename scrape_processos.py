# Atualizado - SEI v4.0.12	

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import csv
import os
import chromedriver_autoinstaller
import time

# Instala o chromedriver automaticamente se necessário
chromedriver_autoinstaller.install()

# Obtém o diretório do projeto
diretorio_projeto = os.getcwd()

# Função que iniciar o navegador no modo headless (sem interface gráfica)
def iniciar_chrome_headless():
    opcoes_chrome = Options()
    opcoes_chrome.add_argument("--headless")
    opcoes_chrome.add_argument("--disable-gpu")
    opcoes_chrome.add_argument("--no-sandbox")
    opcoes_chrome.add_argument("--disable-dev-shm-usage")
    opcoes_chrome.add_argument("--disable-webgl")
    driver = webdriver.Chrome(options=opcoes_chrome)
    return driver

# Função que auxilia iniciar o navegador no modo GUI (com interface gráfica)
def iniciar_chrome_gui():
    driver = webdriver.Chrome()
    return driver

# Descomente a linha do modo que deseje rodar, comente a outra
driver = iniciar_chrome_headless()  # Modo headless
# driver = iniciar_chrome_gui()  # Modo GUI (padrão)
driver.get("https://sei.ufcat.edu.br/sip/login.php?sigla_orgao_sistema=UFCAT&sigla_sistema=SEI") # Adicione o link do SEI desejado

# Credenciais de login
usuario = ''
senha = ''

# Preenche os campos de login
campo_usuario = driver.find_element(By.ID, "txtUsuario")
campo_senha = driver.find_element(By.ID, "pwdSenha")
campo_usuario.send_keys(usuario)
campo_senha.send_keys(senha)

# Clica no botão de login
botao_login = driver.find_element(By.ID, "sbmAcessar")
botao_login.click()

# Realiza uma pesquisa rápida vazia
# Utilizado para chegar rapidamente a página de pesquisa sem utilizar JS, visto que a pesquisa direta falha com Selenium
campo_pesquisa_rapida = driver.find_element(By.ID, "txtPesquisaRapida")
campo_pesquisa_rapida.send_keys("")
campo_pesquisa_rapida.send_keys(Keys.RETURN)

# Marca a opção "Processos"
# Utiliza JS para isso, pois existem limitações no Selenium atual quando lida com radio buttons
processos_radio_button = driver.find_element(By.ID, "optProcessos")
driver.execute_script("arguments[0].checked = true;", processos_radio_button)
driver.execute_script("arguments[0].click();", processos_radio_button)

# Preenche o campo de unidade geradora
campo_unidade_geradora = driver.find_element(By.CSS_SELECTOR, "input#txtUnidade")
campo_unidade_geradora.click()

# Define o nome da unidade geradora
nome_unidade_geradora = "SETI"
ultimo_char = nome_unidade_geradora[-1]

# Preenche o campo da unidade geradora char por char
for char in nome_unidade_geradora:
    campo_unidade_geradora.send_keys(char)
    # Adiciona uma demora entre cada letra, assim não gera problemas na digitação
    # Além disso, evita clicar em outra unidade com devido a demora ao carregar, para isso espera mais tempo no último char
    time.sleep(1.5 if char == ultimo_char else 0.5)

# Seleciona a unidade geradora na lista de opções
campo_unidade_geradora.send_keys(Keys.ARROW_DOWN)
campo_unidade_geradora.send_keys(Keys.ENTER)
campo_unidade_geradora.send_keys(Keys.TAB)

# Clica no botão de pesquisa
botao_pesquisar = driver.find_element(By.ID, 'sbmPesquisar')
botao_pesquisar.click()

# Aguarda 5 segundos para garantir que os resultados sejam carregados
driver.implicitly_wait(5)

# Define o nome do arquivo CSV
# Utiliza o nome da unidade geradora definida em nome_unidade_geradora
nome_csv = f"{nome_unidade_geradora}_processo.csv"

# Loop para percorrer as páginas de resultados
while True:
    try:
        # Localiza a área de resultados e os elementos de processo
        div_infra_area = driver.find_element(By.XPATH, '//*[@id="divInfraAreaTelaD"]')
        conteudo = driver.find_element(By.XPATH, '//*[@id="conteudo"]')

        # Encontra todos os elementos de link com a classe 'protocoloNormal' que carrega o número do processo consigo
        elementos_processos = conteudo.find_elements(By.XPATH, './/a[@class="protocoloNormal"]')

        # Abre o arquivo CSV para adicionar os números dos processos
        with open(nome_csv, mode='a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            for elemento_processo in elementos_processos:
                numero_processo = elemento_processo.text.strip()
                escritor.writerow([numero_processo])  # Escreve o número do processo no CSV

        # Navega para a próxima página
        link_proxima = driver.find_element(By.LINK_TEXT, "Próxima")
        link_proxima.click()

    except NoSuchElementException:
        
        # Caso não encontre mais elemento "Próxima" significa que não existe mais páginas de pesquisa
        # Então infere o fim do processo
        print("Todas as páginas foram processadas com sucesso.")
        break

driver.quit()
exit()
