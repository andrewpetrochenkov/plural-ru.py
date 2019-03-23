<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/plural-ru.svg?longCache=True)](https://pypi.org/project/plural-ru/)
[![](https://img.shields.io/pypi/v/plural-ru.svg?maxAge=3600)](https://pypi.org/project/plural-ru/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/plural-ru.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/plural-ru.py/)

#### Installation
```bash
$ [sudo] pip install plural-ru
```

#### Functions
function|`__doc__`
-|-
`plural_ru.ru(value, quantitative)` |возвращает строку со склоненным существительным

#### CLI
usage|`__doc__`
-|-
`python -m plural_ru count quantitative1 quantitative2 quantitative3` |выводит строку со склоненным существительным

#### Examples
```python
>>> import plural_ru
>>> plural_ru.ru(1,["час","часа","часов"])
'час'
>>> ru(25,["минуту","минуты","минут"])
'минут'
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>