from .headers import headers
from .libs import libs


def main(argv=None, stdout=None):
    from . import LANG, LANGS
    from argparse import ArgumentParser
    if argv is None:
        from sys import argv
    if stdout is None:
        from sys import stdout
    argp = ArgumentParser()
    argp.add_argument(r'-x', r'--lang', choices=LANGS, default=LANG)
    argp.add_argument(r'-l', r'--libs', action=r'store_true')
    argp.add_argument(r'-L', r'--search', default=r'')
    argp.add_argument(r'args', nargs=r'*')
    argx = argp.parse_args(argv[1:])
    args = argx.args
    if not args:
        return
    if argx.libs:
        searchopt, handler = r' -L', libs
    else:
        searchopt, handler = r' -I', headers
    search = argx.search
    if search:
        search = searchopt + search
    lang = argx.lang
    for y in handler(args, search, lang):
        print(r'%s:=yes' % y, file=stdout)


if __name__ == r'__main__':
    main()
