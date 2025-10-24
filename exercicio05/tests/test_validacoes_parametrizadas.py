import pytest
import requests

emails_invalidos = [
    "sem-arroba.com",
    "@sem-usuario.com",
    "sem-dominio@",
    "espacos no meio@teste.com",
    "caracteres!especiais@teste.com",
    "..pontos@teste.com",
    "teste@",
    "@teste.com"
]

@pytest.mark.api
@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    r = requests.post("https://reqres.in/api/register", json={
        "email": email_invalido,
        "password": "senha123"
    }, timeout=20)
    assert r.status_code == 400

senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem número"),
    ("semmaiuscula123", "sem maiúscula"),
    ("12345678", "só números"),
    ("ab", "muito curta")
]

@pytest.mark.api
@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha(senha, motivo):
    r = requests.post("https://reqres.in/api/register", json={
        "email": "test@test.com",
        "password": senha
    }, timeout=20)
    assert r.status_code == 400
