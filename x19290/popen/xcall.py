def xcall(args, **kwargs):
    from subprocess import call

    kwargs[r'shell'] = isinstance(args, str)
    return call(args, **kwargs)
