# POSIX specific
from .__main__ import main as make
from ..test import curdir, eq_, relpath, Path, StringIO, TestCase

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
    pkg = Path(__file__).resolve().parent
    proj, pkg = pkg.parent.parent, relpath(pkg, Path.cwd())
    infix = r'' if pkg == curdir else r'%s/' % pkg

    def _test(self, feed, expected):
        ns = self.__class__.__dict__
        feed %= ns
        expected %= ns
        b = StringIO()
        make(feed.split(), stdout=b)
        actual = b.getvalue()
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
