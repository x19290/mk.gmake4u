def main(argv=None):
    r'''
    exec make --include-dir=$DIR /4U=$DIR ...

    $DIR is derived from __file__ and can be referenced as $(/4U) in makefiles.
    '''
    from os import access, environ, execvp, pathsep as colon, X_OK
    from pathlib import Path
    if argv is None:
        from sys import argv
    __path__ = Path(__file__).resolve().parent.parent  # $DIR
    bin = __path__ / r'bin'
    foryou = r'--include-dir=%s' % __path__, r'/4U=%s' % __path__
    argv = (argv[0], *foryou, *argv[1:])

    origlist = pathlist = environ[r'PATH'].split(colon)

    def macparano():
        # to prevent $(MAKE) from being ridiculously long on macOS
        parano0, parano1 = (Path(y).resolve() for y in
            (
                r'/Library/Developer/CommandLineTools/usr/bin/make',
                r'/usr/bin/make',
            )
        )
        if (access(parano1, X_OK) and access(parano0, X_OK)):
            parano0 = parano0.parent.__str__()
            for y in pathlist:
                if Path(y, r'make').resolve() == parano1:
                    yield parano0
                else:
                    yield y
        else:
            yield from pathlist

    pathlist = tuple(macparano())

    def which(stem):
        # which(1)like
        for y in pathlist:
            y = Path(y, stem)
            if access(y, X_OK):
                return y

    executable = None
    for stem in r'make', r'gmake':
        executable = which(stem)
        if executable:
            break
    if not executable:
        raise ValueError(stem)

    if bin not in origlist:
        environ[r'PATH'] = colon.join(y.__str__() for y in origlist + [bin])
    execvp(executable, argv)


if __name__ == r'__main__':
    main()
