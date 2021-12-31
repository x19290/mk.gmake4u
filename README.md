# GMake for You

An improved GNU make

- [bin/mk4u](bin/mk4u)  
  exec make --include-dir=[$DIR](./) /4U=[$DIR](./) ...  
  the make MUST be GNUmake
- [$DIR/4u/**/*.mk](4u/)  
  pre-written GNUmakefiles
- [mk4u/zz0/0.mk](mk4u/zz0/0.mk)  
  an example of GNUmakefile that references [4u/prologue.mk](4u/prologue.mk)  
  used by [mk4u/zz0smoke_t.py](mk4u/zz0smoke_t.py)
- [bin/0has](bin/0has)  
  a tiny command that prints if headers (libs) are installed:
    ```shell
    $ 0has cstddef "no such header" cstdlib
    cstddef:=yes
    cstdlib:=yes

    $ 0has --libs c "no such lib" m
    -c:=yes
    -m:=yes
    ```
  directly callable from GNUmakefiles under this make.
- [bin/0relpath](bin/0relpath)  
  a tiny command that prints relative path of given one:
    ```shell
    $ 0relpath /usr/bin /usr
    ..

    $ cd /usr/bin
    $ 0relpath /usr
    ..
    ```
  directly callable from GNUmakefiles under this make.
- [zzdemo](zzdemo/)  
  authentic demo.
  you can:
    ```shell
    mk4u +fetch +fix +all
    # or
    mk4u +fetch
    mk4u +fix
    mk4u
    ```
  here.

  See [zzdemo/README.md](zzdemo/README.md).
- \*\*/z[yz][0-9]*_t.py  
  unittests
