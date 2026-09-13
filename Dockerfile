FROM ghcr.io/astral-sh/uv:latest AS uv

FROM python:3.13-slim

WORKDIR /app

COPY --from=uv /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_SYSTEM_PYTHON=1

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

COPY . .

CMD ["python", "main.py"]