.PHONY: run build sync deploy clean

run:
	@make build
	poetry run mkdocs serve

build:
	@make sync
	poetry run mkdocs build

sync:
	poetry run lab sync
	poetry run lab changelog

deploy: build
	rsync -e ssh --delete-after -avz site/ web@lab.abilian.com:/srv/web/lab.abilian.com/

clean:
	rm -rf docs site
