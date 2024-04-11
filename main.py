# How to clear all variables in a Python script

import sys

site = 'bobbyhadz.com'

sys.modules[__name__].__dict__.clear()

# 👇️ accessing int() built-in
int = (5).__class__

print(int('100'))  # 👉️ 100

# 👇️ accessing str() built-in
str = ''.__class__

print(str(100))  # 👉️ '100'