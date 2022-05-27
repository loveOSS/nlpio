# NLP.io : the simple Python library to clean text data

## How to use it ?

``
pip install nlpio
``

```python
from nlpio import strip_html_tags

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

>>> from nlpio import strip_html_tags
>>> print(strip_html_tags('<h1>Hello World</h1>'))
```

## LICENCE

This works is under MIT License.
