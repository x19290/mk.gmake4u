from x19290.test import (
    colon, environ, eq_, devnull, xcall, StringIO, TestCase, DEVNULL,
)
from x19290.redirect import redirect, STDERR_BIT, STDOUT_BIT
from os import chdir, execvpe

devnull, TestCase  # to avoid "not used" warnings


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
        stdout, stderr = StringIO(), StringIO()
        xcall(self.enter, stderr=DEVNULL, stdout=DEVNULL, **kwargs)
        try:
            with redirect(STDOUT_BIT | STDERR_BIT, stdout, stderr) as iswriter:
                if iswriter:
                    chdir(self.cwd)
                    execvpe(r'/bin/sh', (r'sh', r'-c', feed), kwargs[r'env'])
        finally:
            xcall(self.leave, stderr=DEVNULL, stdout=DEVNULL, **kwargs)
        actual = stdout.getvalue()
        smoke = stderr.getvalue()
        if smoke:
            raise AssertionError(smoke)
        eq_(expected, actual)
