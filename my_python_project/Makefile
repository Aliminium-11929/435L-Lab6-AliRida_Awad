.DEFAULT_GOAL := all
PYTHON ?= python
PYB ?= pyb

.PHONY: all clean install install_deps test lint build package
all:
	$(MAKE) clean
	$(MAKE) install_deps
	$(MAKE) test
	$(MAKE) lint
	$(MAKE) build

install: install_deps

install_deps:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYB) run_unit_tests

lint:
	$(PYTHON) -m flake8 src build.py --max-line-length=99

build:
	$(PYB) publish

package: build

clean:
	$(PYB) clean
