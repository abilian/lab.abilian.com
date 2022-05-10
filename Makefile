.PHONY: run build sync

run: sync
	mkdocs serve

build: sync
	mkdocs build

sync:
	python sync.py

deploy: build
	rsync -e ssh -avz site/ web@lab.abilian.com:/srv/web/lab.abilian.com/
