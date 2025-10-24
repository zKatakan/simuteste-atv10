import pytest
import requests

BASE = "https://fakestoreapi.com"

@pytest.mark.api
def test_listar_produtos():
    r = requests.get(f"{BASE}/products", timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]

@pytest.mark.api
@pytest.mark.parametrize("pid", [1, 2, 3])
def test_buscar_produto_por_id(pid):
    r = requests.get(f"{BASE}/products/{pid}", timeout=20)
    assert r.status_code == 200
    item = r.json()
    assert item["id"] == pid
    assert "title" in item and "price" in item and "category" in item

@pytest.mark.api
@pytest.mark.parametrize("categoria", [
    "electronics", "jewelery", "men's clothing", "women's clothing"
])
def test_filtrar_por_categoria(categoria):
    r = requests.get(f"{BASE}/products/category/{categoria}", timeout=20)
    assert r.status_code == 200
    items = r.json()
    assert isinstance(items, list)
    for it in items:
        assert it["category"] == categoria

@pytest.mark.api
def test_validar_schema_produto():
    r = requests.get(f"{BASE}/products/1", timeout=20)
    assert r.status_code == 200
    item = r.json()

    expected_keys = {"id", "title", "price", "description", "category", "image", "rating"}
    assert expected_keys.issubset(set(item.keys()))

    assert isinstance(item["id"], int)
    assert isinstance(item["title"], str)
    assert isinstance(item["price"], (float, int))
    assert isinstance(item["description"], str)
    assert isinstance(item["category"], str)
    assert isinstance(item["image"], str)
    assert "rate" in item["rating"] and "count" in item["rating"]

@pytest.mark.api
def test_limite_de_produtos():
    limit = 5
    r = requests.get(f"{BASE}/products?limit={limit}", timeout=20)
    assert r.status_code == 200
    items = r.json()
    assert isinstance(items, list)
    assert len(items) == limit
