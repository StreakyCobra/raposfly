# --------------------------------------------------------------------------- #
# Variables                                                                   #
# --------------------------------------------------------------------------- #

# Set shell to bash
SHELL := /usr/bin/bash

# List all modules in this folder by looking at "__init__.py" files
MODULES = $(dir $(wildcard */__init__.py))

# Set default target
default: style

# Define phony targets
.PHONY: default in_virtual_env install style pylint pep pep8 pep257 prettify

# --------------------------------------------------------------------------- #
# Targets                                                                     #
# --------------------------------------------------------------------------- #

in_virtual_env:
	@if [[ `basename "$$VIRTUAL_ENV"` = "venv" ]]; then \
			:; \
		else \
			echo This should be run from within a virtual environment; \
			exit 1; \
	fi

install: in_virtual_env
	@pip install -U -r requirements.txt; pip install -U pip

style: pylint pep pep

pylint: in_virtual_env
	-@pylint -r n -f colorized $(MODULES)

pep: pep8 pep257

pep8: in_virtual_env
	-@git ls-files | grep \.py$$ | grep -v /migrations/ | xargs pep8

pep257: in_virtual_env
	-@git ls-files | grep \.py$$ | grep -v /migrations/ | xargs pep257

prettify: in_virtual_env
	@git ls-files | grep \.py$$ | xargs autoflake --remove-all-unused-imports --remove-unused-variables -i
	@git ls-files | grep \.py$$ | xargs isort -y
