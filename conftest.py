import os
import pytest
from selenium import webdriver

# Imports de opções por navegador
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def _headless_enabled():
    return os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")

@pytest.fixture(scope="session")
def chrome_driver():
    """
    Cria um driver usando Selenium Manager, com fallback:
    1) Chrome (padrão)
    2) Edge
    3) Firefox

    Dicas:
      - Para rodar sem UI: set HEADLESS=true
      - Para usar binário portátil (Chrome for Testing), defina CHROME_BINARY com o caminho do executável.
        Ex.: set CHROME_BINARY=C:\\chrome-for-testing\\chrome.exe
    """
    headless = _headless_enabled()

    # 1) Tenta Chrome
    try:
        c_opts = ChromeOptions()
        if headless:
            c_opts.add_argument("--headless=new")
        c_opts.add_argument("--window-size=1920,1080")
        c_opts.add_argument("--no-sandbox")
        c_opts.add_argument("--disable-dev-shm-usage")

        chrome_binary = os.getenv("CHROME_BINARY")  # opcional: CfT/portátil
        if chrome_binary:
            c_opts.binary_location = chrome_binary

        driver = webdriver.Chrome(options=c_opts)  # Selenium Manager resolve o driver
        yield driver
        driver.quit()
        return
    except Exception as e:
        last_err = e  # guarda o erro para diagnóstico se todos falharem

    # 2) Fallback: Edge (muito comum no Windows)
    try:
        e_opts = EdgeOptions()
        if headless:
            e_opts.add_argument("--headless=new")
        e_opts.add_argument("--window-size=1920,1080")
        e_opts.add_argument("--no-sandbox")
        e_opts.add_argument("--disable-dev-shm-usage")

        edge_binary = os.getenv("EDGE_BINARY")  # opcional
        if edge_binary:
            e_opts.binary_location = edge_binary

        driver = webdriver.Edge(options=e_opts)  # Selenium Manager resolve o msedgedriver
        yield driver
        driver.quit()
        return
    except Exception as e:
        last_err = e

    # 3) Fallback: Firefox
    try:
        f_opts = FirefoxOptions()
        if headless:
            f_opts.add_argument("--headless")
        driver = webdriver.Firefox(options=f_opts)  # Selenium Manager resolve o geckodriver
        yield driver
        driver.quit()
        return
    except Exception as e:
        # Se chegou aqui, nenhum navegador funcionou
        raise RuntimeError(
            "Nenhum navegador pôde ser iniciado (Chrome/Edge/Firefox). "
            "Instale pelo menos um ou aponte CHROME_BINARY/EDGE_BINARY/FIREFOX_BINARY. "
            f"Último erro: {e}"
        )
