# TODO: remove the POSIX dependency

from mk4u.zz9indepth import (
    devnull, xcall, Smoke, TestCase, XPopen, DEVNULL, PIPE,
)
from pathlib import Path
from sys import path as pythonpath
__path__ = Path(__file__).resolve().parent.with_name(r'zz9indepth')
_SMOKE = __path__
_PROJECT = _SMOKE.parent.parent
pythonpath[:0] = _SMOKE.__str__(),

_FEED0 = r'''
set -eu

cd id3edit
mkdir -p dig/dig
cd dig/dig

mk4u --no-print-directory -C . -f ../../GNUmakefile +remake
mk4u --no-print-directory -C .. -f ../GNUmakefile +remake
mk4u --no-print-directory -C ../.. -f GNUmakefile +remake
mk4u --no-print-directory -C ../../.. -f %(hub)s/GNUmakefile +remake

mk4u --no-print-directory -C . -f ../../GNUmakefile +clean!
mk4u --no-print-directory -C ../../.. -f %(hub)s/GNUmakefile +clean!
mk4u --no-print-directory -C ../../.. -f %(lib)s/GNUmakefile +clean! # different from above!
'''[1:]

_EXPECTED0 = r'''
%(mk4u)s -C../../../%(lib)s +clean!
mk4u[1]: %(nothing_forclean)s
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../crc32.o ../../crc32.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../extheader.o ../../extheader.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../id3v2.o ../../id3v2.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../id3v2frame.o ../../id3v2frame.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../main.o ../../main.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../rawfile.o ../../rawfile.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../encoding/crc.o ../../encoding/crc.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../encoding/size.o ../../encoding/size.c
gcc --std=gnu99 -Wno-multichar -g -c -I../.. -I../../../%(lib)s --include=endian%(endianfix)s.h -o ../../encoding/text.o ../../encoding/text.c
%(mk4u)s -C../../../%(lib)s libprinthex.a
gcc --std=gnu99 -Wno-multichar -g -c -I. -o printhex.o printhex.c
ar r libprinthex.a printhex.o 2> /dev/null
gcc --std=gnu99 -g -o ../../id3edit ../../crc32.o ../../extheader.o ../../id3v2.o ../../id3v2frame.o ../../main.o ../../rawfile.o ../../encoding/crc.o ../../encoding/size.o ../../encoding/text.o -L../../../%(lib)s -lprinthex -lz%(liconv)s
rm ../crc32.o ../encoding/crc.o ../encoding/size.o ../encoding/text.o ../extheader.o ../id3edit ../id3v2.o ../id3v2frame.o ../main.o ../rawfile.o
%(mk4u)s -C../../%(lib)s +clean!
rm libprinthex.a printhex.o
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../crc32.o ../crc32.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../extheader.o ../extheader.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../id3v2.o ../id3v2.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../id3v2frame.o ../id3v2frame.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../main.o ../main.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../rawfile.o ../rawfile.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../encoding/crc.o ../encoding/crc.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../encoding/size.o ../encoding/size.c
gcc --std=gnu99 -Wno-multichar -g -c -I.. -I../../%(lib)s --include=endian%(endianfix)s.h -o ../encoding/text.o ../encoding/text.c
%(mk4u)s -C../../%(lib)s libprinthex.a
gcc --std=gnu99 -Wno-multichar -g -c -I. -o printhex.o printhex.c
ar r libprinthex.a printhex.o 2> /dev/null
gcc --std=gnu99 -g -o ../id3edit ../crc32.o ../extheader.o ../id3v2.o ../id3v2frame.o ../main.o ../rawfile.o ../encoding/crc.o ../encoding/size.o ../encoding/text.o -L../../%(lib)s -lprinthex -lz%(liconv)s
rm crc32.o encoding/crc.o encoding/size.o encoding/text.o extheader.o id3edit id3v2.o id3v2frame.o main.o rawfile.o
%(mk4u)s -C../%(lib)s +clean!
rm libprinthex.a printhex.o
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o crc32.o crc32.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o extheader.o extheader.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o id3v2.o id3v2.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o id3v2frame.o id3v2frame.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o main.o main.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o rawfile.o rawfile.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o encoding/crc.o encoding/crc.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o encoding/size.o encoding/size.c
gcc --std=gnu99 -Wno-multichar -g -c -I. -I../%(lib)s --include=endian%(endianfix)s.h -o encoding/text.o encoding/text.c
%(mk4u)s -C../%(lib)s libprinthex.a
gcc --std=gnu99 -Wno-multichar -g -c -I. -o printhex.o printhex.c
ar r libprinthex.a printhex.o 2> /dev/null
gcc --std=gnu99 -g -o id3edit crc32.o extheader.o id3v2.o id3v2frame.o main.o rawfile.o encoding/crc.o encoding/size.o encoding/text.o -L../%(lib)s -lprinthex -lz%(liconv)s
rm %(hub)s/crc32.o %(hub)s/encoding/crc.o %(hub)s/encoding/size.o %(hub)s/encoding/text.o %(hub)s/extheader.o %(hub)s/id3edit %(hub)s/id3v2.o %(hub)s/id3v2frame.o %(hub)s/main.o %(hub)s/rawfile.o
%(mk4u)s -C%(hub)s/../%(lib)s +clean!
rm libprinthex.a printhex.o
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/crc32.o %(hub)s/crc32.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/extheader.o %(hub)s/extheader.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/id3v2.o %(hub)s/id3v2.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/id3v2frame.o %(hub)s/id3v2frame.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/main.o %(hub)s/main.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/rawfile.o %(hub)s/rawfile.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/encoding/crc.o %(hub)s/encoding/crc.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/encoding/size.o %(hub)s/encoding/size.c
gcc --std=gnu99 -Wno-multichar -g -c -I%(hub)s -I%(lib)s --include=endian%(endianfix)s.h -o %(hub)s/encoding/text.o %(hub)s/encoding/text.c
%(mk4u)s -C%(hub)s/../%(lib)s libprinthex.a
gcc --std=gnu99 -Wno-multichar -g -c -I. -o printhex.o printhex.c
ar r libprinthex.a printhex.o 2> /dev/null
gcc --std=gnu99 -g -o %(hub)s/id3edit %(hub)s/crc32.o %(hub)s/extheader.o %(hub)s/id3v2.o %(hub)s/id3v2frame.o %(hub)s/main.o %(hub)s/rawfile.o %(hub)s/encoding/crc.o %(hub)s/encoding/size.o %(hub)s/encoding/text.o -L%(lib)s -lprinthex -lz%(liconv)s
rm ../../crc32.o ../../encoding/crc.o ../../encoding/size.o ../../encoding/text.o ../../extheader.o ../../id3edit ../../id3v2.o ../../id3v2frame.o ../../main.o ../../rawfile.o
%(mk4u)s -C../../../%(lib)s +clean!
rm libprinthex.a printhex.o
%(mk4u)s -C%(hub)s/../%(lib)s +clean!
mk4u[1]: %(nothing_forclean)s
mk4u: %(nothing_forclean)s
'''[1:]


def _headerfix(h):
    args = r'gcc -xc -fsyntax-only --include=%s %s' % (h, devnull)
    return r'' if xcall(args, stderr=DEVNULL) == 0 else r'-fix'


class T0(Smoke, TestCase):
    enter = r'mk4u +fetch +fix'
    leave = r'mk4u +clean'
    cwd = _SMOKE
    hub, lib = r'id3edit', r'libprinthex'
    bin = _PROJECT / r'bin'
    mk4u = bin / r'mk4u'
    endianfix = _headerfix(r'endian.h')

    @classmethod
    def setUpClass(cls):
        super(T0, cls).setUpClass()
        kw = cls.kwargs
        with XPopen(r'0has --libs iconv', stdout=PIPE, **kw) as p:
            cls.liconv = r' -liconv' if p.stdout.read() else r''
        with XPopen(r'mk4u -f - +clean!', stdin=PIPE, stdout=PIPE, **kw) as p:
            oobj = p.stdin
            oobj.write(br'+clean!:' b'\n')
            oobj.close()
            nothing = p.stdout.read()[:-1].decode(r'UTF-8')
            cls.nothing_forclean = nothing[6:]  # drop "^mk4u: "

    def test0(self):
        self.smoke(_FEED0, _EXPECTED0)
