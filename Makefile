.PHONY: run test

run:
	python3 -m src.main --file data/stars.json

test:
	pytest
