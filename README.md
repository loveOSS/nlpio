# NLP Tools : the simple Python library to clean text data

## How to use it ?

``
pip install nlptools
``

```python
from nlptools import strip_html_tags

print(strip_html_tags('<h1>Hello World</h1>')) # "Hello World"
```

## Deploy upgrade on PyPi

### Build

```
python setup.py sdist bdist_wheel
twine upload dist/*
```

### Test

```
python -m pip install -e .
python

>>> from nlptools import strip_html_tags
>>> print(strip_html_tags('<h1>Hello World</h1>'))
```

## LICENCE

This works is under MIT License.
