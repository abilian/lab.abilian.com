.PHONY: run build sync deploy clean

run:
	lab sync
	lab changelog
	mkdocs build
	mkdocs serve

build:
	lab sync
	lab changelog
	mkdocs build

sync:
	lab sync
	lab changelog

deploy: build
	rsync -e ssh --delete-after -avz site/ web@lab.abilian.com:/srv/web/lab.abilian.com/

clean:
	rm -rf docs site
