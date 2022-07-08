def representation(clsname, *a, **kw):
    """
    Representation and its evaluation...
     and representation to evaluation.
    """
    return f'{clsname}(*{a}, **{kw})'

# e = builtins.eval(r)
# e.representation = r
