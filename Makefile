all: install

install:
	virtualenv .venv && .venv/bin/pip install -r requirements.txt

test:
	.venv/bin/python -m pytest tests