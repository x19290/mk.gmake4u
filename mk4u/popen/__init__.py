from subprocess import call, Popen


def xcall(args, **kwargs):
    kwargs[r'shell'] = isinstance(args, str)
    return call(args, **kwargs)


class XPopen(Popen):
    def __init__(self, args, **kwargs):
        kwargs[r'shell'] = isinstance(args, str)
        super(XPopen, self).__init__(args, **kwargs)

