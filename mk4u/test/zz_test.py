from . import eq_, raises, TestCase


class T0ng(TestCase):
    @raises(AssertionError)
    def test0(self):
        eq_(r'e', r'a' '\n')

    @raises(AssertionError)
    def test1(self):
        eq_(0, 1)


class T1ok(TestCase):
    def test0(self):
        expected = actual = r'a' '\n'
        eq_(expected, actual)
