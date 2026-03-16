all:
	python3 main.py

test:
	python3 -m unittest easter_test.py

git:
	git add .
	git commit -am hz

