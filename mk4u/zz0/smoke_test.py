# POSIX specific
from ..has.__main__ import main as has
from ..__main__ import main as make
from ..test import curdir, eq_, relpath, Path, StringIO, TestCase
from os import close, dup, dup2, fork, pipe, read, wait

_EXPECTED00 = r'''
cstddef:=yes
cstdlib:=yes
'''[1:]

_EXPECTED01 = r'''
-lc:=yes
-lm:=yes
'''[1:]

_EXPECTED10 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: =.
'''[1:]

_EXPECTED11 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: ../=..
'''[1:]

_EXPECTED12 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s/zz0/a
: %(proj)s/%(pkg)s/zz0/a/b
: b/=b
'''[1:]

_EXPECTED13 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s
: %(proj)s/%(pkg)s/zz0
: ../../=../..
'''[1:]

_EXPECTED14 = r'''
: %(proj)s/mk
: %(proj)s/%(pkg)s/zz0/a
: %(proj)s/%(pkg)s/zz0/a/b
: =.
'''[1:]


class T0has(TestCase):
    def _test(self, feed, expected):
        b = StringIO()
        has(feed.split(r','), stdout=b)
        actual = b.getvalue()
        eq_(expected, actual)

    def test0headers(self):
        self._test(r'<>,-xc++,cstddef,no such header,cstdlib', _EXPECTED00)

    def test1libs(self):
        self._test(r'<>,--libs,c,no such lib,m', _EXPECTED01)


class T1mk(TestCase):
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
        self._test(r'<> -C%(infix)szz0 -f0.mk', _EXPECTED10)

    def test1(self):
        self._test(r'<> -C%(infix)szz0/a -f../0.mk', _EXPECTED11)

    def test2(self):
        self._test(r'<> -C%(infix)szz0/a -fb/0.mk', _EXPECTED12)

    def test3(self):
        self._test(r'<> -C%(infix)szz0/a/b -f../../0.mk', _EXPECTED13)

    def test4(self):
        self._test(r'<> -C%(infix)szz0/a/b -f0.mk', _EXPECTED14)
