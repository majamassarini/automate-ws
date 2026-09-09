.PHONY: prepare-venv test coverage field-test field-test-docker

VENV                    ?=
PYTHON                   = $(if $(VENV),$(CURDIR)/$(VENV)/bin/python3,python3)
AUTOMATE_HOME_BRANCH    ?=
AUTOMATE_KNX_BRANCH     ?=
AUTOMATE_LIFX_BRANCH    ?=
AUTOMATE_SONOS_BRANCH   ?=

prepare-venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install ".[dev]"
	$(if $(AUTOMATE_KNX_BRANCH),$(VENV)/bin/pip install --force-reinstall "git+https://github.com/majamassarini/automate-knx-plugin.git@$(AUTOMATE_KNX_BRANCH)")
	$(if $(AUTOMATE_LIFX_BRANCH),$(VENV)/bin/pip install --force-reinstall "git+https://github.com/majamassarini/automate-lifx-plugin.git@$(AUTOMATE_LIFX_BRANCH)")
	$(if $(AUTOMATE_SONOS_BRANCH),$(VENV)/bin/pip install --force-reinstall "git+https://github.com/majamassarini/automate-sonos-plugin.git@$(AUTOMATE_SONOS_BRANCH)")
	$(if $(AUTOMATE_HOME_BRANCH),$(VENV)/bin/pip install --force-reinstall "git+https://github.com/majamassarini/automate-home.git@$(AUTOMATE_HOME_BRANCH)")

test:
	$(PYTHON) -m coverage run -m unittest discover \
		-s ws/tests -p 'test*.py' -v

coverage: test
	$(PYTHON) -m coverage report -m
	$(PYTHON) -m coverage html
	open htmlcov/index.html

field-test:
	$(PYTHON) field_test/server.py

field-test-docker:
	docker compose -f field_test/docker-compose.yml up --build
