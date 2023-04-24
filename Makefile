.PHONY: run build sync

run: sync
	mkdocs serve

build: sync
	mkdocs build

sync:
	lab sync
	lab changelog

deploy: build
	rsync -e ssh --delete-after -avz site/ web@lab.abilian.com:/srv/web/lab.abilian.com/

clean:
	rm -rf docs site
