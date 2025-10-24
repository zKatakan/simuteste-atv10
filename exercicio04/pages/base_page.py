from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, base_timeout)

    def abrir(self, url):
        self.driver.get(url)

    def encontrar(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visivel(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clicar(self, locator):
        el = self.visivel(locator)
        el.click()

    def digitar(self, locator, texto):
        el = self.visivel(locator)
        el.clear()
        el.send_keys(texto)
