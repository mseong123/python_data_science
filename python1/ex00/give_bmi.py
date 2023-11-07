import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """calculate bmi and return list of calculated bmi"""
    errMsg = "elements inside list is not a float or int"
    try:
        assert type(height) is list, "first arg is not a list"
        assert type(weight) is list, "second arg is not a list"
        assert len(height) > 0, "empty list"
        assert len(weight) > 0, "empty list"
        for x in height:
            assert type(x) is float or type(x) is int, errMsg
        for y in weight:
            assert type(y) is float or type(y) is int, errMsg
        npheight = np.array(height)
        npweight = np.array(weight)
        assert len(npheight[npheight < 0]) == 0, "negative numbers invalid"
        assert len(npweight[npweight < 0]) == 0, "negative numbers invalid"
        assert npheight.size == npweight.size, "list is not same size"
    except AssertionError as message:
        print(message)
    else:
        return list(npweight / (npheight * npheight))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """compares element in list with limit (True if above
    limit) and returns a boolean list"""
    try:
        assert type(bmi) is list, "first arg is not a list"
        assert len(bmi) > 0, "empty list"
        assert type(limit) is int, "second arg is not a integer"
        assert limit > 0, "second arg cannot be negative"
    except AssertionError as message:
        print(message)
    else:
        npbmi = np.array(bmi)
        return list(npbmi > limit)
