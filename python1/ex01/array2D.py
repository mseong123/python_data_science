import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """function to slice list"""
    try:
        assert type(family) is list, "first arg is not a list"
        assert type(start) is int, "sec arg is not a int"
        assert type(end) is int, "third arg is not a int"
        npfamily = np.array(family)
    except AssertionError as message:
        print(message)
    except ValueError as e:
        print(f"ValueError:{e}")
    else:
        print("my shape is : " + str(npfamily.shape))
        npfamily = npfamily[start:end]
        print("my new shape is : " + str(npfamily.shape))
        return npfamily.tolist()
