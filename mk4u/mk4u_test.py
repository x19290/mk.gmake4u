# POSIX specific
from .__main__ import main as make
from .test import curdir, eq_, relpath, Path, StringIO, TestCase
from os import close, dup, dup2, fork, pipe, read, wait

_EXPECTED0 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: =.
'''[1:]

_EXPECTED1 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: ../=..
'''[1:]

_EXPECTED2 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s/zz0/a
: %(proj)s/%(pkg)s/zz0/a/b
: b/=b
'''[1:]

_EXPECTED3 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: ../../=../..
'''[1:]

_EXPECTED4 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s/zz0/a
: %(proj)s/%(pkg)s/zz0/a/b
: =.
'''[1:]


class T0(TestCase):
    pkg = Path(__file__).resolve().parent.parent
    proj, pkg, infix = pkg.parent, pkg.name, relpath(pkg, Path.cwd())
    infix = r'' if infix == curdir else r'%s/' % infix

    def _test(self, feed, expected):
        # testing `make` is not so easy because:
        # - it has nothing like `stdout=` parameter
        # - it `exec`s
        ns = self.__class__.__dict__
        feed %= ns
        expected %= ns
        outfd = 1
        saved = dup(outfd)
        try:
            r, w = pipe()
            dup2(w, outfd)
            close(w)
            pid = fork()
            if pid == 0:
                make(feed.split())
                raise AssertionError
        finally:
            dup2(saved, outfd)
        close(saved)
        wait()
        enough = 8192
        actual = read(r, enough).decode(r'UTF-8')
        eq_(expected, actual)

    def test0(self):
        self._test(r'<> -C%(infix)szz0 -f0.mk', _EXPECTED0)

    def test1(self):
        self._test(r'<> -C%(infix)szz0/a -f../0.mk', _EXPECTED1)

    def test2(self):
        self._test(r'<> -C%(infix)szz0/a -fb/0.mk', _EXPECTED2)

    def test3(self):
        self._test(r'<> -C%(infix)szz0/a/b -f../../0.mk', _EXPECTED3)

    def test4(self):
        self._test(r'<> -C%(infix)szz0/a/b -f0.mk', _EXPECTED4)
