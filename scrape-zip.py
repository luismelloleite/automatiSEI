# Atualizado - SEI v4.0.12	

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

diretorio_projeto = os.getcwd()

# Solicita ao usuário o nome da pasta para os downloads
nome_pasta = "SETI"

# Verifica se o nome da pasta foi fornecido
if not nome_pasta:
    raise ValueError("A pasta de downloads não foi informada.")

diretorio_downloads = os.path.join(diretorio_projeto, nome_pasta)
if not os.path.exists(diretorio_downloads):
    os.makedirs(diretorio_downloads)

# Função para iniciar o navegador no modo headless (sem interface gráfica)
def iniciar_chrome_headless():
    opcoes_chrome = Options()
    opcoes_chrome.add_argument("--headless")
    opcoes_chrome.add_argument("--disable-gpu")
    opcoes_chrome.add_argument("--no-sandbox")
    opcoes_chrome.add_argument("--disable-dev-shm-usage")
    opcoes_chrome.add_argument("--disable-webgl")
    
    # Configura o diretório de download
    prefs = {"download.default_directory": diretorio_downloads}
    opcoes_chrome.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=opcoes_chrome)
    return driver

def iniciar_chrome_gui():
    opcoes_chrome = Options()
    
    prefs = {"download.default_directory": diretorio_downloads}
    opcoes_chrome.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=opcoes_chrome)
    return driver

# Descomente a linha do modo que deseja rodar, comente a outra
# driver = iniciar_chrome_headless()  # Modo headless
driver = iniciar_chrome_gui()  # Modo GUI (padrão)
driver.get("https://sei.ufcat.edu.br/sip/login.php?sigla_orgao_sistema=UFCAT&sigla_sistema=SEI") # Adicione o link do SEI desejado

# Credenciais de login
usuario = ''
senha = ''

campo_usuario = driver.find_element(By.ID, "txtUsuario")
campo_senha = driver.find_element(By.ID, "pwdSenha")
campo_usuario.send_keys(usuario)
campo_senha.send_keys(senha)

botao_login = driver.find_element(By.ID, "sbmAcessar")
botao_login.click()

# Abre o arquivo CSV e lê os dados (ignora o cabeçalho)
with open(nome_pasta + '_processo.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    # Para cada linha no arquivo CSV
    for linha in leitor:
        # Obtém o número do processo
        numero_processo = linha[0]

        # Verifica se o número do processo foi fornecido
        if not numero_processo:
            raise ValueError("O número do processo não foi fornecido.")

        # Localiza e preenche o campo de pesquisa rápida com o número do processo
        campo_pesquisa_rapida = driver.find_element(By.ID, "txtPesquisaRapida")
        campo_pesquisa_rapida.clear()
        campo_pesquisa_rapida.send_keys(numero_processo)
        campo_pesquisa_rapida.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)

        # Muda para o frame de visualização do processo
        campo_visualizacao = WebDriverWait(driver, 30).until(
            lambda d: d.find_element(By.ID, "ifrVisualizacao")
        )
        driver.switch_to.frame(campo_visualizacao)

        # Localiza o campo de árvore de ações e seus elementos
        campo_arvore_acoes = WebDriverWait(driver, 30).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="divArvoreAcoes"]')
        )
        elementos = campo_arvore_acoes.find_elements(By.XPATH, "*")

        # Itera sobre os elementos da árvore de ações
        for elemento in elementos:
            outer_html = elemento.get_attribute("outerHTML")
            
            if 'procedimento_gerar_zip' in outer_html:
                elemento.click()
                btn_gerar = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.NAME, "btnGerar"))
                )
                btn_gerar.click()
                break

        driver.switch_to.default_content()

driver.quit()
