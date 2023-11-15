import re

ccnum_re = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$')
for _ in range(int(input())):
    print('Valid' if ccnum_re.match(input()) else 'Invalid')
