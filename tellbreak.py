import os


def loop():
    retcode = None

    while True:
        path = yield retcode
        path += '.bat'

        if (retcode := unavailable(path)) is None:
            break


def unavailable(path):
    """
    >>> unavailable('pass.bat')
    0
    >>> unavailable('pass.bat')
    0
    >>> unavailable('quit.bat')
    """
    the_directory = 'contains'

    if path not in os.listdir(the_directory):
        return None  # break

    path = os.path.join(the_directory, path)
    return os.system(path)
