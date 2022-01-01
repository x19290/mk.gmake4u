from mk4u.test import (
    colon, environ, eq_, devnull, xcall, TestCase, XPopen, DEVNULL, PIPE,
)

(
    devnull, TestCase,
)  # to avoid "not used" warnings


class Smoke:
    enter = leave = r''

    @classmethod
    def setUpClass(cls):
        _bin = cls.bin.__str__()
        env = environ.copy()  # per subclass
        env[r'PATH'] = colon.join([_bin] + environ[r'PATH'].split(colon))
        cls.kwargs = dict(cwd=cls.cwd, env=env)

    def smoke(self, feed, expected):
        ns = self.__class__.__dict__
        try:
            feed %= ns
        except TypeError:
            feed = tuple(y % ns for y in feed)
        expected %= ns
        kwargs = self.kwargs
        xcall(self.enter, stderr=DEVNULL, stdout=DEVNULL, **kwargs)
        try:
            with XPopen(feed, stderr=PIPE, stdout=PIPE, **kwargs) as p:
                smoke = p.stderr.read().decode(r'UTF-8')
                if smoke:
                    raise AssertionError(smoke)
                actual = p.stdout.read().decode(r'UTF-8')
        finally:
            xcall(self.leave, stderr=DEVNULL, stdout=DEVNULL, **kwargs)
        eq_(expected, actual)
