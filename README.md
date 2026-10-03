# Tempo [![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](https://opensource.org/licenses/MIT)

Time tracking CLI for developers.

## Features

- Start/stop/cancel activity tracking
- Current session status
- Daily statistics
- PostgreSQL persistence
- Alembic migrations
- Docker development environment
- Automated tests

## Tech Stack

- Python 3.13
- Typer
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Pytest
- Docker
- uv

## Installation

Clone the repository:

```bash
git clone https://github.com/guwisu/tempo.git
cd tempo
```

Install dependencies:

```bash
uv sync
```

Copy environment variables file:
```bash
cp .env.example .env
```

Start PostgreSQL:

```bash
docker compose up -d
```

Apply database migrations:

```bash
uv run alembic upgrade head
```

Run Tempo:

```bash
uv run tempo --help
```


## Usage

- tempo start ...
- tempo status
- tempo stop
- tempo cancel
- tempo today
- tempo about

## Architecture
```
└── tempo/
    ├── README.md
    ├── alembic.ini
    ├── docker-compose.yml
    ├── Dockerfile
    ├── LICENSE
    ├── pyproject.toml
    ├── .python-version
    ├── src/
    │   ├── __init__.py
    │   ├── migrations/
    │   ├── presentation/
    │   │   ├── console.py
    │   │   └── formatters.py
    │   └── tempo/
    │       ├── __init__.py
    │       ├── cli.py
    │       ├── config.py
    │       ├── database.py
    │       ├── exceptions.py
    │       ├── main.py
    │       ├── models/
    │       │   ├── __init__.py
    │       │   └── session.py
    │       ├── repositories/
    │       │   ├── __init__.py
    │       │   └── session.py
    │       ├── schemas/
    │       │   ├── __init__.py
    │       │   └── session.py
    │       └── services/
    │           ├── __init__.py
    │           └── session.py
    └── tests/
        ├── conftest.py
        └── test_services.py
```

## Testing

Run the test suite:
```bash
uv run pytest -v
```
Tests use a PostgreSQL container provided by Testcontainers.

## License

This project is under the MIT license.
