def ft_filter(fn, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for
    which function(item) is true. If function is None,
    return the items that are true.
    """
    if fn is None:
        return [x for x in iterable if x is True]
    else:
        return [x for x in iterable if fn(x) is True]
