
A Python binary that runs on Linux, MacOS, Windows, FreeBSD, OpenBSD, and NetBSD for both the ARM64 and AMD64 architectures.

```bash
cd /tmp
wget https://cosmo.zip/pub/cosmos/bin/python
chmod 755 python
./python -c 'print("Hello world")'
```

## Making your own executables

Example (from: https://github.com/tekknolagi/scrapscript/blob/e38210f7aa8ce375a7e615b301922bd7b9710d37/build-com)

```bash
#!/bin/sh
set -eux
PREV="$(pwd)"
DIR="$(mktemp -d)"
cp scrapscript.py "$DIR"
cp .args "$DIR"
cp repl.html "$DIR"
cp style.css "$DIR"
cd "$DIR"
wget https://cosmo.zip/pub/cosmos/bin/python
wget https://cosmo.zip/pub/cosmos/bin/zip
chmod +x python
chmod +x zip
./python -m compileall scrapscript.py
mkdir Lib
cp __pycache__/scrapscript.*.pyc Lib/scrapscript.pyc
cp style.css repl.html Lib
cp python scrapscript.com
./zip -r scrapscript.com Lib .args
echo "Testing..."
./scrapscript.com apply "1+2"
cd "$PREV"
cp "$DIR"/scrapscript.com .
```

## More info

- https://justine.lol/ape.html
- https://cosmo.zip/