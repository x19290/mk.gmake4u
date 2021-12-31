def headers(headers, search=r'', lang=None):
    if lang is None:
        from . import LANG as lang
    args = (
        r'gcc -x%(lang)s -fsyntax-only%(search)s '
        r'--include=%(header)s %(devnull)s'
    )
    from os.path import devnull
    from subprocess import call, DEVNULL
    devnull  # to avoid "not used" warnings
    for header in headers:
        if call(args % locals(), stderr=DEVNULL, shell=True) != 0:
            continue
        yield header
