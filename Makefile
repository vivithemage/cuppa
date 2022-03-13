package:
	make build
	zip dist-cuppa dist/cuppa
	make clean

build:
	pyinstaller --onefile cuppa/cuppa.py

test:
	python cuppa/cuppa.py

clean:
	rm -rf dist build cuppa.spec

install:
	pipenv install

activate:
	pipenv shell

test:
	pytest
