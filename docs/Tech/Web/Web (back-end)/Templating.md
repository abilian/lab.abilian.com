# Templating in Python

## Mainstream Python

- Django templates
- Jinja2
- ZPT / Chameleon
- Mako

Chameleon = faster ZPT by compiling to python bytecode.

(All are supported by PyCharm OOTB, except Mako).

## Exotic Python

- Pug / PyJade
- Dust / Ashes (https://github.com/mahmoud/ashes)
- Genshi (https://genshi.edgewall.org/)
- Clearsilver (https://github.com/blong42/clearsilver/) (dead)

More + benchmarks: https://github.com/marrow/cinje/wiki/Benchmarks


## Internal Python DSLs

### Using context managers

- https://github.com/galvez/xmlwitch (dead)
- https://www.yattag.org/
- https://github.com/tlonny/pdoo
- https://github.com/Knio/dominate
- https://github.com/Parnassius/domify
- https://github.com/bitplorer/uidom

### Using mutable objects

- https://tylerbakke.github.io/MarkupPy/
- LXML

### Using extended syntax (a la JSX)

- https://github.com/michaeljones/packed
- https://github.com/gvanrossum/pyxl3 (dead)
- https://github.com/pyxl4/pyxl4 (dead)
- https://github.com/twidi/mixt/ (semi-dead)

### Using functions

- https://github.com/byteface/domonic
    - https://github.com/byteface/htmlx (simpler fork)
- https://pypi.org/project/hyperpython/
- https://pypi.org/project/PyHTML/
- https://github.com/jviide/htm.py (see also: https://viewdom.readthedocs.io/)
- https://github.com/pcarbonn/fast_html
- https://github.com/MohammadrezaAmani/INUI
- https://github.com/scrussell24/hype-html
- https://github.com/Hrabal/TemPy
- https://github.com/tvst/htbuilder
- https://github.com/mosquito/tagz

### Multi-paradigm

- https://github.com/BrainStormYourWayIn/sierra

## More

- https://wiki.python.org/moin/Templating
- https://github.com/stars/legout/lists/py-html/

## Not Python

### ZPT-likes

- Thymeleaf: Similar to ZPT. Java only. https://www.thymeleaf.org Very complete. Not sure how popular.
- https://davidcana.github.io/ZPT-JS/ 

### Others

- Armin is working on a port of Jinja to Rust (-> compilation to WASM)
    - https://docs.rs/minijinja/latest/minijinja/
    - There is a Python package for it
- Vue templates
- Nuejs templates: https://nuejs.org/docs/reference/template-syntax.html

<!-- Keywords -->
#pycharm #templates #django
<!-- /Keywords -->
