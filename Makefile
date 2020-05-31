run:
	rm -rf submission
	cp -r sample-python submission
	python3 main.py

build:
	rm -rf submission
	cp -r sample-python submission
	docker build -t test .
