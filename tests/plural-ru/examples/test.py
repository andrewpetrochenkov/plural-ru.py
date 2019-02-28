#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plural_ru

try:
    print(plural_ru.ru(1, [u"час", u"часа", u"часов"]))
    print(plural_ru.ru(25, [u"минуту", u"минуты", u"минут"]))
except UnicodeEncodeError:
    print("UnicodeEncodeError, python2.7 :(")
