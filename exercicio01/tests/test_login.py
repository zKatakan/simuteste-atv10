import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://practicetestautomation.com/practice-test-login/"

@pytest.mark.web
def test_login_sucesso(chrome_driver):
    d = chrome_driver
    d.get(BASE_URL)
    d.find_element(By.ID, "username").send_keys("student")
    d.find_element(By.ID, "password").send_keys("Password123")
    d.find_element(By.ID, "submit").click()

    WebDriverWait(d, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    assert "Logged In Successfully" in d.page_source
    assert "/logged-in-successfully/" in d.current_url

@pytest.mark.web
def test_login_email_invalido(chrome_driver):
    d = chrome_driver
    d.get(BASE_URL)
    d.find_element(By.ID, "username").send_keys("student@")
    d.find_element(By.ID, "password").send_keys("Password123")
    d.find_element(By.ID, "submit").click()

    err = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.ID, "error")))
    assert "Your username is invalid!" in err.text

@pytest.mark.web
def test_login_senha_incorreta(chrome_driver):
    d = chrome_driver
    d.get(BASE_URL)
    d.find_element(By.ID, "username").send_keys("student")
    d.find_element(By.ID, "password").send_keys("Password1234")
    d.find_element(By.ID, "submit").click()

    err = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.ID, "error")))
    assert "Your password is invalid!" in err.text or "Your username is invalid!" in err.text

@pytest.mark.web
def test_login_campos_vazios(chrome_driver):
    d = chrome_driver
    d.get(BASE_URL)
    d.find_element(By.ID, "submit").click()

    err = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.ID, "error")))
    assert "invalid" in err.text.lower()

@pytest.mark.web
def test_mensagens_erro_adequadas(chrome_driver):
    d = chrome_driver
    d.get(BASE_URL)
    d.find_element(By.ID, "username").send_keys("foo")
    d.find_element(By.ID, "password").send_keys("bar")
    d.find_element(By.ID, "submit").click()

    err = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.ID, "error")))
    assert err.is_displayed()
    assert any(substr in err.text for substr in [
        "username is invalid", "password is invalid"
    ])
