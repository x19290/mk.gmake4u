from ..popen import xcall, XPopen
from nose.tools import raises
from contextlib import redirect_stderr, redirect_stdout
from inspect import stack
from io import BytesIO, StringIO
from os.path import curdir, devnull, pardir, relpath
from os import pathsep as colon, environ, sep as slash
from pathlib import Path
from shutil import copyfile, copyfileobj
from subprocess import call, check_call, Popen, DEVNULL, PIPE
from sys import platform
from unittest import TestCase

(
    raises,
    redirect_stderr, redirect_stdout,
    stack,
    BytesIO, StringIO,
    curdir, devnull, pardir, relpath,
    colon, environ, slash,
    Path,
    copyfile, copyfileobj,
    call, check_call, Popen, DEVNULL, PIPE,
    platform,
    TestCase,
)  # to avoid "not used" warnings


def eq_(expected, actual, msg=None):
    if actual == expected:
        return
    def testid(name):
        i = None
        for i, y in enumerate(name):
            if y.isdigit():
                break
        try:
            return name[i:]
        except:
            raise AssertionError(name)
    sp = stack()
    frame = sp[1]
    testobj = frame.frame.f_locals[r'self']
    classid = testid(testobj.__class__.__name__)
    for i in range(1, 10):
        deeper = sp[i]
        filename, method = deeper[1], deeper[3]
        if filename.endswith(r'_t.py'):
            break
    def multilined(*g):
        try:
            return not all('\n' not in y for y in g)
        except TypeError:
            return False
    if multilined(expected, actual):
        __path__ = Path(filename)
        methodid = testid(method)
        e, a = (
            __path__.with_suffix(r'.%s.%s.0%ctmp' % (classid, methodid, y))
            for y in r'ea'
        )
        e.write_text(expected)
        a.write_text(actual)
        def chop(s):
            i = s.find('\n')
            return r'%s...' % s[:i] if 0 < i else s
        expected, actual = (chop(y) for y in (expected, actual))
    raise AssertionError(msg or "%r != %r" % (expected, actual))
