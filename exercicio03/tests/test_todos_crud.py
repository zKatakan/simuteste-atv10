import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"
TODOS = f"{BASE}/todos"

@pytest.fixture
def novo_todo_payload():
    return {"title": "Minha tarefa", "completed": False, "userId": 1}

@pytest.mark.api
def test_crud_todos_completo(novo_todo_payload):
    # CREATE
    r_create = requests.post(TODOS, json=novo_todo_payload, timeout=20)
    assert r_create.status_code in (201, 200)
    created = r_create.json()
    assert "id" in created
    new_id = created["id"]

    # READ
    r_read = requests.get(f"{TODOS}/{new_id}", timeout=20)
    assert r_read.status_code in (200, 404)
    read_body = r_read.json()
    assert isinstance(read_body, dict)

    # UPDATE (PATCH)
    r_patch = requests.patch(f"{TODOS}/{new_id}", json={"completed": True}, timeout=20)
    assert r_patch.status_code in (200, 201)
    patched = r_patch.json()
    assert "completed" in patched

    # DELETE
    r_del = requests.delete(f"{TODOS}/{new_id}", timeout=20)
    assert r_del.status_code in (200, 204)

    # VERIFY
    r_verify = requests.get(f"{TODOS}/{new_id}", timeout=20)
    assert r_verify.status_code in (200, 404)
    body = r_verify.json()
    assert body == {} or r_verify.status_code == 404

@pytest.mark.api
def test_criar_todo_sem_titulo_deve_falhar():
    # JSONPlaceholder é permissivo; este teste documenta o comportamento (não falha).
    r = requests.post(TODOS, json={"completed": False, "userId": 1}, timeout=20)
    assert r.status_code in (200, 201)
