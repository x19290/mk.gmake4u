def libs(libs, search=r'', lang=None):
    from ... import MK
    if lang is None:
        from . import LANG as lang
    args = r'gcc -x%(lang)s -o %(devnull)s %(c)s%(search)s %(y)s'
    from os.path import devnull
    from pathlib import Path
    from subprocess import call, DEVNULL
    __path__ = Path(__file__).resolve().parent
    c = MK / r'4u' / r'c' / r'0.c'
    devnull, c  # to avoid "not used" warnings
    for y in libs:
        y = r'-l%s' % y
        status = call(args % locals(), stderr=DEVNULL, shell=True)
        if status == 0:
            yield y
