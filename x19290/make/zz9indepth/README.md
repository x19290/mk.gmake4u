# In-depth demo

In this directory, you can fetch two third-party projects, fix them,
and build an executable by:
```shell
mk4u +fetch +fix +all
```

## mk4u +fetch

fetches:
- https://github.com/rstemmer/id3edit.git
- https://github.com/rstemmer/libprinthex.git

## mk4u +fix

applies small patches to the former, adds small GNUmakefiles to them.

## mk4u +all

builds libprinthex/libprinthex.a and id3edit/id3edit (recursive make.)

## Testing

The outputs of the make can be tested by:
```shell
PYTHONPATH=.. python3 -m unittest discover -p 'zz[0-9]*_slowtest.py'
```

Such tests are excluded from settings.json because they are slow.

It is possible to do the same slow tests in vscode
adding this directory as a folder to your workspace.
