export PYTHONPATH=.
export PYTHONDONTWRITEBYTECODE=1

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
POETRY = $(VENV)/bin/poetry
ISORT = $(VENV)/bin/isort
BLACK = $(VENV)/bin/black
JUPYTER = $(VENV)/bin/jupyter
PYTEST = $(VENV)/bin/pytest
COVERAGE = $(VENV)/bin/coverage 

clean:	
	@find . -name "__pycache__" -type d | xargs rm -rf	
	@find . -name ".coverage" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name "htmlcov" -type d | xargs rm -rf

build-env:
	python3 -m pip install --upgrade pip
	python3 -m venv $(VENV)
	$(PIP) install poetry
	
install:
	$(POETRY) install --with ci,tests

run:	
	$(POETRY) run python app.py

test:
	$(POETRY) run pytest

coverage:
	$(COVERAGE) run -m pytest

coverage-report:
	$(COVERAGE) report -m

coverage-html:
	$(COVERAGE) html

format:
	$(BLACK) .


