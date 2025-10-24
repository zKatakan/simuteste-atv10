# Exercícios — Testes Web e REST

Este repositório contém a solução completa dos exercícios:

- **Exercício 1**: Testes de login (Selenium)
- **Exercício 2**: Testes da API Fake Store
- **Exercício 3**: CRUD na API JSONPlaceholder
- **Exercício 4**: Refatoração para POM
- **Exercício 5**: Testes parametrizados (REST + Web)

## Requisitos

- Python 3.10+ recomendado
- Google Chrome instalado
- Dependências do `requirements.txt`

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

### Modo headless (opcional)
Para rodar os testes Web sem abrir janela do navegador:
```bash
# Windows (CMD)
set HEADLESS=true
# PowerShell
$env:HEADLESS="true"
# Linux/Mac
export HEADLESS=true
```

## Execução

### Rodar tudo com relatório HTML
```bash
pytest --html=report.html --self-contained-html
```

### Rodar apenas Web
```bash
pytest -m web --html=report_web.html --self-contained-html
```

### Rodar apenas API
```bash
pytest -m api --html=report_api.html --self-contained-html
```

## Estrutura

```
exercicios-teste-software/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── exercicio01/
│   └── tests/
│       └── test_login.py
├── exercicio02/
│   └── tests/
│       └── test_products_api.py
├── exercicio03/
│   └── tests/
│       └── test_todos_crud.py
├── exercicio04/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   └── dashboard_page.py
│   └── tests/
│       └── test_login_pom.py
└── exercicio05/
    └── tests/
        ├── test_validacoes_parametrizadas.py
        └── test_busca_parametrizada.py
```
