from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    SUCCESS_TEXT = "Logged In Successfully"

    def esta_logado(self):
        return self.SUCCESS_TEXT.lower() in self.driver.page_source.lower()

    def obter_mensagem_boas_vindas(self):
        try:
            h1 = self.encontrar((By.TAG_NAME, "h1"))
            return h1.text
        except Exception:
            return ""
