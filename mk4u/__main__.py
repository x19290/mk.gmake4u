def main(argv=None, stdout=None, stderr=None):
    r'''
    exec make --include-dir=$MK /MK=$MK ...

    $DIR is derived from __file__ and can be referenced as $(/MK) in makefiles.
    '''
    from . import BIN, MK
    from .osredirect import redirect, STDERR_BIT, STDOUT_BIT
    from os import access, environ, execvp, pathsep as colon, X_OK
    from pathlib import Path
    if argv is None:
        from sys import argv
    if stdout is None:
        from sys import stdout
    if stderr is None:
        from sys import stderr
    argv = (argv[0], r'--include-dir=%s' % MK, r'/MK=%s' % MK, *argv[1:])

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

    if BIN not in origlist:
        environ[r'PATH'] = colon.join(y.__str__() for y in origlist + [BIN])
    with redirect(STDOUT_BIT | STDERR_BIT, stdout, stderr) as iswriter:
        if iswriter:
            execvp(executable, argv)


if __name__ == r'__main__':
    main()
