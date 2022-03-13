package:
	make build
	zip dist-cuppa dist/cuppa
	make clean

build:
	pyinstaller --paths cuppa --onefile cuppa/cuppa.py

test:
	python cuppa/cuppa.py

clean:
	rm -rf dist build cuppa.spec

full-clean:
	rm -rf dist build cuppa.spec dist-cuppa.zip

install:
	pipenv install

activate:
	pipenv shell

test:
	pytest
