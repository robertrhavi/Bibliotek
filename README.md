# Bibliotek

API REST em Python, FastAPI e SQLAlchemy para gerenciamento de bibliotecas.

## Estado atual

O código possui rotas de autores, categorias, editoras, livros, exemplares, usuários e empréstimos em `/api/v1`, além de `GET /health`.
O projeto está em desenvolvimento. O módulo de autenticação ainda é inicial.

## Executar localmente

Na raiz do repositório:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m uvicorn server:app --app-dir src --reload --port 8080
```

No Windows, use `.venv\Scripts\activate` e copie o arquivo de ambiente pelo explorador ou terminal.

Configure `DATABASE_URL` no `.env` para seu banco e instale o driver correspondente. O exemplo usa SQLite para desenvolvimento.
A aplicação atual não cria automaticamente as tabelas. Para um banco local novo, execute explicitamente:

```bash
PYTHONPATH=src python -c "import models; from database import Base, engine; Base.metadata.create_all(bind=engine)"
```

Esse comando cria as tabelas ausentes; alterações de esquema existentes precisam de um processo de migração.
A documentação fica em http://localhost:8080/docs.

## Organização

| Caminho | Responsabilidade |
| --- | --- |
| `src/server.py` | Aplicação principal e registro das rotas |
| `src/routes/` | Endpoints HTTP |
| `src/controllers/` | Operações por entidade |
| `src/crud_controllers/` | Abstrações de CRUD |
| `src/services/` | Regras de empréstimos |
| `src/models/` | Modelos SQLAlchemy |
| `src/schemas/` | Validação e contratos de dados |
| `src/events/` | Eventos dos modelos |
| `src/config.py` e `src/database.py` | Ambiente e sessões do banco |
| `examples/library_in_memory.py` | Protótipo independente em memória |

`src/main.py` é um alias da aplicação principal, preservando o comando `uvicorn main:app --app-dir src`.

## Próximos passos

- Implementar autenticação e autorização.
- Adicionar testes de integração de empréstimos e devoluções.
- Definir migrações de banco e documentar os drivers suportados.

Licença MIT; consulte [LICENSE](LICENSE).
