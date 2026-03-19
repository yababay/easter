all:
	python3 main.py

git:
	git add .
	git commit -am hz
	git push origin sun

act:
	@echo 'source .venv/bin/activate'

