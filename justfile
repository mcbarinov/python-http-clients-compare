clean:
    rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage dist build src/*.egg-info


format:
    uv run ruff check --select I --fix src
    uv run ruff format src

lint: format
    uv run ruff check src
    uv run mypy src

sync:
    uv sync
