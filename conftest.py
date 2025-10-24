import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="session")
def chrome_driver():
    """
    Driver Chrome com webdriver-manager.
    Defina HEADLESS=true no ambiente para rodar sem UI.
    """
    headless = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
