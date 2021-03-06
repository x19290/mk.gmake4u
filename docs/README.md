# GMake For You

An improved GNU make

- [bin/mk4u](../bin/mk4u)  
  It does `exec make --include-dir=$MK /MK=$MK ...`  
  `$MK` is the absolute path of [mk/](../mk/)
  derived from [mk4u/_\_main__.py](../mk4u/__main__.py).  
  `make` MUST be GNU make.
- [mk/4u/**/*.mk](../mk/4u/)  
  pre-written GNUmakefile fragments
- [mk4u/zz0/0.mk](../mk4u/zz0/0.mk) [mk4u/zz0/a/b/0.mk](../mk4u/zz0/a/b/0.mk)  
  These files are examples of GNUmakefile that reference
  [mk/4u/prologue.mk](../mk/4u/prologue.mk).  
  [mk4u/mk4u_test.py](../mk4u/mk4u_test.py) and
  [mk4u/zz0.bash](../mk4u/zz0.bash) use them.
- [bin/0has](../bin/0has)  
  a tiny command that prints whether headers (libs) are installed:
    ```shell
    $ 0has --lang=c++ cstddef "no such header" cstdlib
    cstddef:=yes
    cstdlib:=yes

    $ 0has --libs c "no such lib" m
    -lc:=yes
    -lm:=yes
    ```
  directly callable from GNUmakefiles under [bin/mk4u](../bin/mk4u).
- [bin/0relpath](../bin/0relpath)  
  a tiny command that prints relative path of given one:
    ```shell
    $ 0relpath /usr/bin /usr
    ..

    $ cd /usr/bin
    $ 0relpath /usr
    ..
    ```
  directly callable from GNUmakefiles under [bin/mk4u](../bin/mk4u).
- [mk4u/zz9indepth/](../mk4u/zz9indepth/)  
  in-depth demo.
  you can:
    ```shell
    mk4u +fetch +fix +all
    # or
    mk4u +fetch
    mk4u +fix
    mk4u
    ```
  here.

- [mk4u/zz9indepth/0fix/](../mk4u/zz9indepth/0fix/)  
  There are good examples of GNUmakefile and its fragment under this dir.  
  You should know that:  
  [.../id3edit/0cp/GNUmakefile](
    ../mk4u/zz9indepth/0fix/id3edit/0cp/GNUmakefile
  ) and
  [.../libprinthex/0cp/GNUmakefile](
    ../mk4u/zz9indepth/0fix/libprinthex/0cp/GNUmakefile
  )
  are extremely short.

  See [mk4u/zz9indepth/README.md](../mk4u/zz9indepth/README.md).

- **/*_test.py  
  unittests

- **/*_slowtest.py  
  unittests (slow)

- [mk4u/PORTS.md](../mk4u/PORTS.md)  
  to overcome the weakness of the python's package system
