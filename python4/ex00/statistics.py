from typing import Any
import numbers


def mean(args):
    """print mean"""
    if len(args) < 1:
        print("ERROR")
    else:
        print(f"mean : {sum(args) / len(args)}")


def median(args):
    """print median"""
    length = len(args)
    pos = int(length / 2)
    if length < 2:
        print("ERROR")
    elif length % 2 == 1:
        print(f"median : {args[pos]}")
    else:
        first = args[pos]
        second = args[pos - 1]
        print(f"median : {(first + second) / 2}")


def quartile(args):
    """print first and third quartile"""
    length = len(args)
    if length < 4:
        print("ERROR")
    else:
        first = args[int((length + 1) / 4)]
        third = args[(int(3 * (length + 1) / 4)) - 1]
        print(f"quartile : [{first}, {third}]")


def std(args):
    """print std deviation"""
    if len(args) < 2:
        print("ERROR")
    else:
        mean = sum(args) / len(args)
        new_list = [(i - mean) ** 2 for i in args]
        std = (sum(new_list) / len(args)) ** (1 / 2)
        print(f"std : {std}")


def var(args):
    """print variance"""
    if len(args) < 2:
        print("ERROR")
    else:
        mean = sum(args) / len(args)
        new_list = [(i - mean) ** 2 for i in args]
        var = (sum(new_list) / len(args))
        print(f"var : {var}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """receives arguments and prints statistical calculation"""
    errMsg = "Arguments not of number type"
    try:
        for i in args:
            assert isinstance(i, numbers.Number), errMsg
    except Exception as e:
        print(f"{e}")
    else:
        for key, value in kwargs.items():
            args = list(args)
            args.sort()
            if value == "mean":
                mean(args)
            elif value == "median":
                median(args)
            elif value == "quartile":
                quartile(args)
            elif value == "std":
                std(args)
            elif value == "var":
                var(args)
