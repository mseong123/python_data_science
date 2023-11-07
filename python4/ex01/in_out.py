def square(x: 'int | float') -> 'int | float':
    """square"""
    msg = "Argument is not int or float"
    try:
        assert type(x) is int or type(x) is float, msg
    except Exception as e:
        print(f"{e}")
    else:
        return x ** 2


def pow(x: 'int | float') -> 'int | float':
    """pow"""
    msg = "Argument is not int or float"
    try:
        assert type(x) is int or type(x) is float, msg
    except Exception as e:
        print(f"{e}")
    else:
        return x ** x


def outer(x: 'int | float', function) -> object:
    """outer"""
    count = 0

    def inner() -> float:
        """inner"""
        nonlocal count
        count += 1
        nonlocal x
        x = function(x)
        return x
    return inner
