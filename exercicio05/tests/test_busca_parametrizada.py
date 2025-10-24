import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
    d.get("https://www.google.com")
    # Aceita cookies/consentimento se aparecer (melhora estabilidade)
    try:
        d.find_element(By.TAG_NAME, "body")
        time.sleep(1)
        buttons = d.find_elements(By.TAG_NAME, "button")
        for b in buttons:
            if "Aceitar" in b.text or "Accept" in b.text:
                b.click()
                break
    except Exception:
        pass

    box = d.find_element(By.NAME, "q")
    box.send_keys(termo_busca)
    box.send_keys(Keys.ENTER)

    time.sleep(2)
    assert termo_busca.lower() in d.page_source.lower()
