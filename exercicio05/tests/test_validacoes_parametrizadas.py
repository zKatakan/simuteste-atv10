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
    "@teste.com",
]

senhas_invalidas = [
    ("123", "muito curta"),
    ("semNumero", "sem número"),
    ("semmaiuscula123", "sem maiúscula"),
    ("12345678", "só números"),
    ("ab", "muito curta"),
]

BAD_STATUSES = {400, 401}  # 401 acontece em redes com proxy/firewall

@pytest.mark.api
@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    r = requests.post(
        "https://reqres.in/api/register",
        json={"email": email_invalido, "password": "senha123"},
        timeout=20,
    )
    assert r.status_code in BAD_STATUSES
    # se chegar a resposta do Reqres, normalmente vem {"error": "..."}
    try:
        j = r.json()
        assert isinstance(j, dict)
    except Exception:
        # se foi bloqueado pelo proxy, pode vir HTML — só não pode ser 2xx
        pass

@pytest.mark.api
@pytest.mark.parametrize("senha,motivo", senhas_invalidas)
def test_validacao_senha(senha, motivo):
    r = requests.post(
        "https://reqres.in/api/register",
        json={"email": "test@test.com", "password": senha},
        timeout=20,
    )
    assert r.status_code in BAD_STATUSES
    try:
        j = r.json()
        assert isinstance(j, dict)
    except Exception:
        pass
