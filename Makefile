.PHONY: run build sync

run:
	mkdocs serve

build:
	mkdocs build

sync:
	python sync.py

