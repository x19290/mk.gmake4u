from .__main__ import main as has
from ..test import eq_, StringIO, TestCase

_EXPECTED0 = r'''
cstddef:=yes
cstdlib:=yes
'''[1:]

_EXPECTED1 = r'''
-lc:=yes
-lm:=yes
'''[1:]


class T0(TestCase):
    def _test(self, feed, expected):
        b = StringIO()
        has(feed.split(r','), stdout=b)
        actual = b.getvalue()
        eq_(expected, actual)

    def test0headers(self):
        self._test(r'<>,-xc++,cstddef,no such header,cstdlib', _EXPECTED0)

    def test1libs(self):
        self._test(r'<>,--libs,c,no such lib,m', _EXPECTED1)
