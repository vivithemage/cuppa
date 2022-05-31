package:
	make build
	zip dist-cuppa dist
	make clean

build:
	pyinstaller --paths cuppa --onefile main.py

clean:
	rm -rf dist build cuppa.spec

full-clean:
	rm -rf dist build cuppa.spec dist-cuppa.zip

install:
	pipenv install

activate:
	pipenv shell

test:
	pytest -s
