.PHONY: run build sync deploy clean

run:
	@make build
	uv run mkdocs serve

build:
	@make sync
	uv run mkdocs build

sync:
	uv run lab sync
	uv run lab changelog

deploy: build
	rsync -e ssh --delete-after -avz site/ web@lab.abilian.com:/srv/web/lab.abilian.com/

clean:
	rm -rf docs site

format:
	ruff format src
