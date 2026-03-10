.PHONY: prepare-venv test coverage

VENV   ?=
PYTHON  = $(if $(VENV),$(CURDIR)/$(VENV)/bin/python3,python3)

prepare-venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install ".[dev]"

test:
	$(PYTHON) -m coverage run -m unittest discover \
		-s ws/tests -p 'test*.py' -v

coverage: test
	$(PYTHON) -m coverage report -m
	$(PYTHON) -m coverage html
	open htmlcov/index.html
