import os
import pytest
from selenium import webdriver


from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def _headless_enabled():
    return os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")

@pytest.fixture(scope="session")
def chrome_driver():

    headless = _headless_enabled()

    # 1) Tenta Chrome
    try:
        c_opts = ChromeOptions()
        if headless:
            c_opts.add_argument("--headless=new")
        c_opts.add_argument("--window-size=1920,1080")
        c_opts.add_argument("--no-sandbox")
        c_opts.add_argument("--disable-dev-shm-usage")

        chrome_binary = os.getenv("CHROME_BINARY") 
        if chrome_binary:
            c_opts.binary_location = chrome_binary

        driver = webdriver.Chrome(options=c_opts) 
        yield driver
        driver.quit()
        return
    except Exception as e:
        last_err = e  

    
    try:
        e_opts = EdgeOptions()
        if headless:
            e_opts.add_argument("--headless=new")
        e_opts.add_argument("--window-size=1920,1080")
        e_opts.add_argument("--no-sandbox")
        e_opts.add_argument("--disable-dev-shm-usage")

        edge_binary = os.getenv("EDGE_BINARY")
        if edge_binary:
            e_opts.binary_location = edge_binary

        driver = webdriver.Edge(options=e_opts) 
        yield driver
        driver.quit()
        return
    except Exception as e:
        last_err = e


    try:
        f_opts = FirefoxOptions()
        if headless:
            f_opts.add_argument("--headless")
        driver = webdriver.Firefox(options=f_opts)
        yield driver
        driver.quit()
        return
    except Exception as e:
    
        raise RuntimeError(
            "Nenhum navegador pôde ser iniciado (Chrome/Edge/Firefox). "
            "Instale pelo menos um ou aponte CHROME_BINARY/EDGE_BINARY/FIREFOX_BINARY. "
            f"Último erro: {e}"
        )
