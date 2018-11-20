[![](https://img.shields.io/pypi/pyversions/plural-ru.svg?longCache=True)](https://pypi.org/pypi/plural-ru/)
[![](https://img.shields.io/pypi/v/plural-ru.svg?maxAge=3600)](https://pypi.org/pypi/plural-ru/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/plural-ru.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/plural-ru.py/)

#### Install
```bash
$ [sudo] pip install plural-ru
```

#### Functions
function|description
-|-
`plural_ru.ru(value, quantitative)`|возвращает строку со склоненным существительным

#### CLI
usage|description
-|-
`python -m plural_ru count quantitative1 quantitative2 quantitative3`|выводит строку со склоненным существительным

#### Examples
```python
>>> import plural_ru
>>> plural_ru.ru(1,["час","часа","часов"])
'час'
>>> ru(25,["минуту","минуты","минут"])
'минут'
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>