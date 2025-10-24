import pytest
from exercicio04.pages.login_page import LoginPage
from exercicio04.pages.dashboard_page import DashboardPage

@pytest.mark.web
class TestLoginPOM:

    def test_login_sucesso(self, chrome_driver):
        login = LoginPage(chrome_driver)
        dash = DashboardPage(chrome_driver)

        login.abrir()
        login.fazer_login("student", "Password123")

        assert dash.esta_logado()
        assert "Logged In Successfully" in dash.obter_mensagem_boas_vindas()

    def test_login_invalido(self, chrome_driver):
        login = LoginPage(chrome_driver)

        login.abrir()
        login.fazer_login("student@", "Password123")

        assert "invalid" in chrome_driver.page_source.lower()
