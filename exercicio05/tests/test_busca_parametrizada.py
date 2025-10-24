import pytest
from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.web
@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    d = chrome_driver
    # Abre direto a SERP, evitando a homepage/consentimento
    q = quote(termo_busca)
    d.get(f"https://www.google.com/search?q={q}&hl=pt-BR")

    # Espera o container principal de resultados
    wait = WebDriverWait(d, 15)
    wait.until(EC.presence_of_element_located((By.ID, "search")))

    # Validação robusta: título contém o termo (mais estável que page_source)
    assert termo_busca.lower() in d.title.lower()

    # (Opcional) fallback extra — pelo menos 1 resultado orgânico visível
    resultados = d.find_elements(By.CSS_SELECTOR, "div#search h3")
    assert len(resultados) > 0
