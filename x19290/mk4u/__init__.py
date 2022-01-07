def __abspaths():
    from pathlib import Path

    __path__ = Path(__file__).resolve().parent.parent.parent
    yield from (__path__ / y for y in (r'bin', r'mk'))


BIN, MK = __abspaths()
